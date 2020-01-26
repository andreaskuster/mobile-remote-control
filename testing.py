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

__description__ = "Continuous Integration testing."
__author__ = "Andreas Kuster"
__copyright__ = "Copyright 2020, Mobile Remote Control"
__license__ = "GPL"

import unittest
from udp_hole_punching.network_helper import network_msg_to_str, str_to_network_msg


class UDPHolePunching(unittest.TestCase):

    def test_helper_functions(self):
        message = "hello world!"
        self.assertEqual(message, network_msg_to_str(str_to_network_msg(message)))


if __name__ == "__main__":
    # run all tests
    unittest.main()
