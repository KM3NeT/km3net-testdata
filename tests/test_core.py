#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from km3net_testdata import data_path


class TestDataPath(unittest.TestCase):
    def test_access(self):
        assert data_path("km3net_offline.root").endswith("km3net_offline.root")
