# -*- coding: utf-8 -*-

# built-in package
from __future__ import print_function
import argparse

# third-party package
from .. import app
# from dashboard import app

# user-defined package


parser = argparse.ArgumentParser(description='Start your IPython-Dashboard server ...')
parser.add_argument('-H', '--host', type=str, default='0.0.0.0', help='server host, default localhost')
parser.add_argument('-p', '--port', type=int, default=9090, help='server port, default 9090')
parser.add_argument('-d', '--debug', type=bool, default=True, help='server port, default true')

args = parser.parse_args()
print(args)


def run():
    app.run(host=args.host, port=args.port, debug=args.debug)


if __name__ == '__main__':
    run()
