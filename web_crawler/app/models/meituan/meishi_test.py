#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

import os, sys
lib_path = os.path.abspath(os.path.join('./app/'))
sys.path.append(lib_path)

from common.testing.base_test import BaseTest
from meishi import Meishi

class MeishiTest(BaseTest):
    mock_meishi =  {
        "poiId": 160349852,                                                                                                                                               
        "frontImg": "http://p1.meituan.net/600.600/mogu/82c4123a64cf53d53f84fc7c64038aa1247292.jpg",                                                                      
        "title": "茶颜观色——新中式鲜茶（南沙万达店）",                                                                                                                    
        "avgScore": 5,                                                                                                                                                    
        "allCommentNum": 86,
        "address": "南沙万达广场环市大道东25号万达金街二楼208〔7号门对面〕",
        "avgPrice": 16.43,
    }

    def setUp(self):
        super().setUp()
        self.meishi_obj = Meishi.load_or_create(
                                poiId=self.mock_meishi.get('poiId'),
                                frontImg=self.mock_meishi.get('frontImg'),
                                title=self.mock_meishi.get('title'),
                                avgScore=self.mock_meishi.get('avgScore'),
                                allCommentNum=self.mock_meishi.get('allCommentNum'),
                                address=self.mock_meishi.get('address'),
                                avgPrice=self.mock_meishi.get('avgPrice'),
                          )
        self.assertEqual(self.meishi_obj.poiId, self.mock_meishi.get('poiId'))
        self.assertEqual(self.meishi_obj.frontImg, self.mock_meishi.get('frontImg'))
        self.assertEqual(self.meishi_obj.title, self.mock_meishi.get('title'))
        self.assertEqual(self.meishi_obj.avgScore, self.mock_meishi.get('avgScore'))
        self.assertEqual(self.meishi_obj.allCommentNum, self.mock_meishi.get('allCommentNum'))
        self.assertEqual(self.meishi_obj.address, self.mock_meishi.get('address'))
        self.assertEqual(self.meishi_obj.avgPrice, self.mock_meishi.get('avgPrice'))

    def tearDown(self):
        super().tearDown()
        Meishi.del_by_id(self.meishi_obj.poiId)
        self.assertEqual(Meishi.by_id(self.meishi_obj.poiId), None)

    def test_by_id(self):
        meishi_load_obj = Meishi.by_id(self.meishi_obj.poiId)
        self.assertEqual(self.meishi_obj.poiId, self.mock_meishi.get('poiId'))
        self.assertEqual(self.meishi_obj.frontImg, self.mock_meishi.get('frontImg'))
        self.assertEqual(self.meishi_obj.title, self.mock_meishi.get('title'))
        self.assertEqual(self.meishi_obj.avgScore, self.mock_meishi.get('avgScore'))
        self.assertEqual(self.meishi_obj.allCommentNum, self.mock_meishi.get('allCommentNum'))
        self.assertEqual(self.meishi_obj.address, self.mock_meishi.get('address'))
        self.assertEqual(self.meishi_obj.avgPrice, self.mock_meishi.get('avgPrice'))

if __name__ == '__main__':
    unittest.main()
