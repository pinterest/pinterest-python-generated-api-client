#!/usr/bin/env python

"""OpenAPI specification processing tool used to
create a spec for generating an SDK Client by filtering
some endpoints from v5 external.yaml"""

from __future__ import annotations
import sys

try:
    from urllib import request
except ImportError as e:
    print(f"{e}. To fix: `pip install urllib`", file=sys.stderr)
    sys.exit(1)


def main(args):
    if len(args) < 2:
        raise 'Need to specified the url and the name'
    url = args[0]
    path = args[1]
    # Download and create the file
    request.urlretrieve(url, path)


if __name__ == '__main__':
    main(sys.argv[1:])
