#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tests to compare the ini and yaml based inventorys.
#
# This script was written by Stefan Berggren <nsg@nsg.cc>
# This code is released under the MIT license.
#
# The MIT License (MIT)
# 
# Copyright (c) 2015 Stefan Berggren
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import print_function
import os
import unittest
import operator

from ansible import errors
from ansible.inventory import Inventory

class AnsibleInventoryTests(unittest.TestCase):

    yml_inv = Inventory("{}/inv.sh".format(os.path.dirname(__file__)))

    def test_check_group_vars_host1(self):
        yml = self.yml_inv.get_variables("myhost1.example.com")
        result = {
            'inventory_hostname': u'myhost1.example.com',
            'group_names': [u'com', u'example', u'myhost', u'root', u'root-docker'],
            'inventory_hostname_short': u'myhost1'
            }
        self.assertDictEqual(yml, result, msg="\nGot:    {}\nExpect: {}".format(yml, result))

    def test_check_group_vars_host2(self):
        yml = self.yml_inv.get_variables("myhost2.example.com")
        result = {
            'inventory_hostname': u'myhost2.example.com',
            'group_names': [u'com', u'example', u'myhost', u'root', u'root-docker', u'root-docker-site_a'],
            'inventory_hostname_short': u'myhost2'
            }
        self.assertDictEqual(yml, result, msg="\nGot:    {}\nExpect: {}".format(yml, result))

    def test_check_group_vars_host3(self):
        yml = self.yml_inv.get_variables("myhost3.example.com")
        result = {
            'inventory_hostname': u'myhost3.example.com',
            'group_names': [u'com', u'example', u'myhost', u'root', u'root-docker', u'root-docker-site_b', u'root-docker-site_b-my_foo_group'],
            'inventory_hostname_short': u'myhost3'
            }
        self.assertDictEqual(yml, result, msg="\nGot:    {}\nExpect: {}".format(yml, result))

    def test_list_hosts(self):
        yml = sorted(self.yml_inv.list_hosts())
        result = [u'myhost1.example.com', u'myhost2.example.com', u'myhost3.example.com']
        self.assertListEqual(yml, result, msg="\nGot:    {}\nExpect: {}".format(yml, result))

if __name__ == '__main__':
    print("\n### Execute test {}\n".format( __file__))
    unittest.main(verbosity=2)