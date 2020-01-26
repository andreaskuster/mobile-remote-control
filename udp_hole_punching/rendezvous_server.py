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

__description__ = "Public Rendezvous Server for the UDP Hole Punching protocol."
__author__ = "Andreas Kuster"
__copyright__ = "Copyright 2020, Mobile Remote Control"
__license__ = "GPL"

import argparse
import asyncio
import sys


class RendezvousServer:

    def __init__(self):
        pass

    def connection_made(self, transport):
        print("start", transport)
        self.transport = transport

    def datagram_received(self, data, addr):
        # simple echo server
        print("data received:", data, addr)
        self.transport.sendto(data, addr)

    def error_received(self, ex):
        print("error received:", ex)

    def connection_lost(self, ex):
        print("stop", ex)


def start_server(loop, addr):
    t = asyncio.Task(loop.create_datagram_endpoint(RendezvousServer, local_addr=addr))
    transport, server = loop.run_until_complete(t)
    return transport


if __name__ == "__main__":

    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--hostname", default="0.0.0.0")
    parser.add_argument("--port", default="8080")
    args = parser.parse_args()

    # create event loop
    loop = asyncio.get_event_loop()

    # start udp rendezvous server
    server = start_server(loop, (args.hostname, args.port))

    try:
        # run event loop
        loop.run_forever()
    finally:
        # clean up
        server.close()
        loop.close()

    # exit ok
    sys.exit(0)
