#!/usr/bin/env python3
# encoding: utf-8

"""
    Mobile Remote Control
    Copyright (C) 2020  Andreas Kuster

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__description__ = "Client behind a NAT."
__author__ = "Andreas Kuster"
__copyright__ = "Copyright 2020, Mobile Remote Control"
__license__ = "GPL"

import argparse
import asyncio
import sys


class Client:
    message = "dummy message"

    def connection_made(self, transport):
        self.transport = transport
        print("sending {}".format(self.message))
        self.transport.sendto(self.message.encode())
        print("waiting to receive")

    def datagram_received(self, data, addr):
        print("received {}".format(data.decode()))
        self.transport.close()

    def error_received(self, ex):
        print("error received:", ex)

    def connection_lost(self, ex):
        print("closing transport", ex)
        loop = asyncio.get_event_loop()
        loop.stop()


def start_client(loop, addr):
    task = asyncio.Task(loop.create_datagram_endpoint(Client, remote_addr=addr))
    loop.run_until_complete(task)


if __name__ == "__main__":

    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostname", default="127.0.0.1")
    parser.add_argument("--port", default="8080")
    args = parser.parse_args()

    # create event loop
    loop = asyncio.get_event_loop()

    # start udp client
    start_client(loop, (args.hostname, args.port))

    try:
        # run event loop
        loop.run_forever()
    finally:
        # clean up
        loop.close()

    # exit ok
    sys.exit(0)
