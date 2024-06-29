"""
@Author: Li Yu Cai
@Date: 2024/3/12 21:25
@FileName: test_userJourney.py
"""
import time

import allure

from Pages.PageComponent.page_userJourney import UJPage
from Utils.Log import Msg


class TestUJComponent:

    def step(self, msg=''):
        self.log.info(msg)
        return allure.step(msg)

    def test_UJ(self, base_page):
        news_urls = []
        self.log = Msg('内容资料库接口按照列表地址跳转')
        new_page = UJPage(base_page, self.log)
        self.step('获取内容资料库接口返回数据')
        news_urls1 = new_page.listening_response(news_urls)
        self.step('获取登录信息')
        new_page.get_token()
        self.step('打开测试页面')
        new_page.open_url_()
        self.step('断言第一条新闻链接')
        new_page.waits()
        url1 = new_page.get_url_1()
        assert new_page.split_and_compare(url1, news_urls1[0])
        self.step('断言第二条新闻链接')
        new_page.waits()
        url2 = new_page.get_url_2()
        assert new_page.split_and_compare(url2, news_urls1[1])
        self.step('断言第三条新闻链接')
        new_page.waits()
        url3 = new_page.get_url_3()
        assert new_page.split_and_compare(url3, news_urls1[2])
        self.step('断言第四条新闻链接')
        new_page.waits()
        url4 = new_page.get_url_4()
        assert new_page.split_and_compare(url4, news_urls1[3])
