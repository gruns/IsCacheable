#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# iscacheable - A simple tool to determine if a URL is cacheable or not.
#
# Ansgar Grunseid
# grunseid.com
# grunseid@gmail.com
#
# License: MIT
#

import sys

from cachecontrol import CacheControl
from cachecontrol.adapter import CacheControlAdapter
from docopt import docopt
import requests


VERSION = '0.1'


__doc__ = """iscacheable - Determine if a URL is URL cacheable or not

Usage:
  iscacheable <url>
  iscacheable -h | --help
  iscacheable --version

Options:
  -h --help             Show this help information.
  --version             Show version.
"""


sess = CacheControl(requests.session())
adapter = CacheControlAdapter(
    cache_etags=True, cacheable_methods=('GET', 'HEAD'))
sess.mount('http://', adapter)
sess.mount('https://', adapter)


def determineCacheability(url):
    resp = sess.head(url, allow_redirects=True)
    adapter.controller.cache_response(resp.request, resp.raw)

    if adapter.controller.cached_request(resp.request):
        return True
    return False


def main():
    args = docopt(__doc__, version=VERSION)  # Raises SystemExit.
    url = args.get('<url>')

    isCacheable = determineCacheability(url)

    if isCacheable:
        print('Cacheable.')
        sys.exit(0)
    print('Not cacheable.')
    sys.exit(1)


if __name__ == '__main__':
    main()
