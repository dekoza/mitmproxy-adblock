# mitmproxy-adblock

[![ci](https://github.com/dekoza/mitmproxy-adblock/workflows/ci/badge.svg)](https://github.com/dekoza/mitmproxy-adblock/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://dekoza.github.io/mitmproxy-adblock/)
[![pypi version](https://img.shields.io/pypi/v/mitmproxy-adblock.svg)](https://pypi.org/project/mitmproxy-adblock/)
[![gitter](https://badges.gitter.im/join%20chat.svg)](https://gitter.im/mitmproxy-adblock/community)

Ad blocker for [mitmproxy](http://mitmproxy.org/) using popular AdBlockPlus blocklists. Inspired by [mitm-adblock](https://github.com/epitron/mitm-adblock).
Created because [pi-hole](https://pi-hole.net/) does not work for YouTube ads.

## Requirements

mitmproxy-adblock requires Python 3.8 or above.

<details>
<summary>To install Python 3.8, I recommend using <a href="https://github.com/pyenv/pyenv"><code>pyenv</code></a>.</summary>

```bash
# install pyenv
git clone https://github.com/pyenv/pyenv ~/.pyenv

# setup pyenv (you should also put these three lines in .bashrc or similar)
export PATH="${HOME}/.pyenv/bin:${PATH}"
export PYENV_ROOT="${HOME}/.pyenv"
eval "$(pyenv init -)"

# install Python 3.8
pyenv install 3.8.6

# make it available globally
pyenv global system 3.8.6
```
</details>

## Installation

With `pip`:
```bash
python3.8 -m pip install mitmproxy-adblock
```
