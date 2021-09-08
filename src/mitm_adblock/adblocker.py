import logging
from glob import glob

import re2
from adblockparser import AdblockRules
from mitmproxy import http
from mitmproxy.proxy.layers.http import HttpRequestHook
from mitmproxy.script import concurrent
from .utils import combine

IMAGE_MATCHER = re2.compile(r"\.(png|jpe?g|gif)$")
SCRIPT_MATCHER = re2.compile(r"\.(js)$")
STYLESHEET_MATCHER = re2.compile(r"\.(css)$")

logger = logging.getLogger(__name__)


class AdBlocker(HttpRequestHook):
    def __init__(self):
        blocklists = glob("blocklists/*")  # TODO use interactive method method & fallback
        self.rules = self.parse(blocklists)

    def parse(self, blocklists):
        return AdblockRules(
            combine(blocklists),
            use_re2=True,
            max_mem=512 * 1024 * 1024,
        )

    @concurrent
    def request(self, flow):
        req = flow.request

        options = {"domain": req.host}

        if IMAGE_MATCHER.search(req.path):
            options["image"] = True
        elif SCRIPT_MATCHER.search(req.path):
            options["script"] = True
        elif STYLESHEET_MATCHER.search(req.path):
            options["stylesheet"] = True

        if self.rules.should_block(req.url, options):
            message = f'BLOCKED! accept: {flow.request.headers.get("Accept")} ; blocked-url: {flow.request.url}'
            logger.info(message)
            print(message)

            flow.response = http.Response.make(200, b"BLOCKED.", {"Content-Type": "text/html"})
        else:
            message = f"url: {flow.request.url}"
            logger.info(message)
            print(message)
