# encoding=utf-8
import allure

from Pages.PageComponent.page_gw import GWPage
from Utils.Log import Msg


class TestZC:

    def step(self, msg=''):
        self.log.info(msg)
        return allure.step(msg)

    def test_zc(self, base_page):
        self.log = Msg('test_zc')
        with self.step("步骤一：打开浏览器"):
            new_page = GWPage(base_page)
            new_page.open_url("https://www.pre.webullbroker.com/ko-builder/1691465556269-158f6a")
        with self.step("步骤二：去官网注册+判断地址"):
            url = new_page.gw_zc()
            assert "https://passport.pre.webullbroker.com/auth/simple/signup" in url[0]
            assert "https://www.pre.webullbroker.com/ko-builder/1691465556269-158f6a" in url[1]

    def test_open_account(self, base_page):
        self.log = Msg('test_open_account')
        with self.step('步骤一：打开浏览器'):
            new_page = GWPage(base_page)
            new_page.open_url("https://www.pre.webullbroker.com/ko-builder/1691465556269-158f6a")
        with self.step("步骤二：跳转官网开户交易"):
            button = '跳官网开户交易'
            page = new_page.gw_get_page(button)
            new_page.waits()
            assert 'https://www.pre.webullbroker.com/open-account' in page.url
