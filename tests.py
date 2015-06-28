#!/usr/bin/python
# encoding=UTF-8

# Copyright © 2011-2012
#   Jakub Wilk <jwilk@jwilk.net>.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License, version 2, as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.

try:
    import unittest2 as unittest
except ImportError:
    import unittest

import os

import utils

class test_split_host(unittest.TestCase):

    def test_domain(self):
        self.assertEqual(
            utils.split_host('news.icm.edu.pl', 119),
            ('news.icm.edu.pl', 119)
        )

    def test_domain_and_port(self):
        self.assertEqual(
            utils.split_host('news.icm.edu.pl:42', 119),
            ('news.icm.edu.pl', 42)
        )

    def test_ipv4(self):
        self.assertEqual(
            utils.split_host('213.135.51.10', 119),
            ('213.135.51.10', 119)
        )

    def test_ipv4_and_port(self):
        self.assertEqual(
            utils.split_host('213.135.51.10:42', 119),
            ('213.135.51.10', 42)
        )

    def test_ipv6(self):
        self.assertEqual(
            utils.split_host('2001:4de0:1::1:1', 119),
            ('2001:4de0:1::1:1', 119)
        )

    def test_ipv6_in_brackets(self):
        self.assertEqual(
            utils.split_host('[2001:4de0:1::1:1]', 119),
            ('2001:4de0:1::1:1', 119)
        )

    def test_ipv6_and_port(self):
        self.assertEqual(
            utils.split_host('[2001:4de0:1::1:1]:42', 119),
            ('2001:4de0:1::1:1', 42)
        )

class test_xdg(unittest.TestCase):

    def setUp(self):
        self._default_xdg_data_home = \
            os.path.join(os.path.expanduser('~'), '.local', 'share')

    def _check_xdg_data_home(self, expected_path=None):
        if expected_path is None:
            expected_path = self._default_xdg_data_home
        reload(utils)
        self.assertEqual(
            utils.xdg.xdg_data_home,
            expected_path,
        )

    def test_XDG_DATA_HOME_unset(self):
        os.environ['XDG_DATA_HOME'] = ''
        del os.environ['XDG_DATA_HOME']
        self._check_xdg_data_home()

    def test_XDG_DATA_HOME_empty(self):
        os.environ['XDG_DATA_HOME'] = ''
        self._check_xdg_data_home()

    def test_XDG_DATA_HOME_relative(self):
        os.environ['XDG_DATA_HOME'] = 'eggs'
        self._check_xdg_data_home()

    def test_XDG_DATA_HOME_absolute(self):
        os.environ['XDG_DATA_HOME'] = '/eggs'
        self._check_xdg_data_home('/eggs')

if __name__ == '__main__':
    unittest.main()

# vim:ts=4 sts=4 sw=4 et
