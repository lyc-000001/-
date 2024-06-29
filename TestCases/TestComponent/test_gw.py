# encoding=utf-8
import time

import allure

from Pages.PageComponent.page_gw import GWPage
from Utils.Log import Msg


class TestGW:

    def step(self, msg=''):
        self.log.info(msg)
        return allure.step(msg)

    def test_dl(self, base_page):
        self.log = Msg('test_dl')

        with self.step("步骤一：打开浏览器"):
            new_page = GWPage(base_page)
            new_page.get_token()
            new_page.open_url("https://www.pre.webullbroker.com/ko-builder/1691465556269-158f6a")
        # with self.step("步骤二：去官网登录+判断地址"):
        # button = "点击跳官网登录"
        # result_url = new_page.gw_dl(button, "zengge_23@163.com", "auto1234")
        # # time.sleep(2)
        # # assert "https://passport.pre.webullbroker.com/auth/simple/login" in result_url[0]
        # assert "https://www.pre.webullbroker.com/ko-builder/1691465556269-158f6a" in result_url[1]

    def test_award(self, base_page):
        self.log = Msg('test_open_account')
        with self.step("步骤一：打开浏览器"):
            new_page = GWPage(base_page)
            # new_page.get_token()
            new_page.open_url("https://www.pre.webullbroker.com/ko-builder/1691465556269-158f6a")
        with self.step("步骤二：点击跳转至奖励中心"):
            page = new_page.gw_get_page("点击跳奖励中心")
            assert "https://act.pre.webullbroker.com/actv3/my-reward" in page.url

    def test_center(self, base_page):
        self.log = Msg('test_center')
        with self.step('步骤一：打开浏览器'):
            new_page = GWPage(base_page)
            # new_page.get_token()
            new_page.open_url("https://www.pre.webullbroker.com/ko-builder/1691465556269-158f6a")
        with self.step("步骤二：跳转至个人中心"):
            button = '跳官网个人中心'
            page = new_page.gw_get_page(button)
            assert 'https://www.pre.webullbroker.com/center' in page.url

    def test_open_cash(self, base_page):
        self.log = Msg('test_open_account')
        with self.step('步骤一：打开浏览器'):
            new_page = GWPage(base_page)
            # new_page.get_token()
            new_page.open_url("https://act.pre.webullbroker.com/ko-builder/1691465556269-158f6a")
        with self.step("步骤二：跳官网入金"):
            button = '跳官网入金'
            page = new_page.gw_get_page(button)
            assert 'https://www.pre.webullbroker.com/center' in page.url

    def test_quote_nasdaq(self, base_page):
        self.log = Msg('test_open_account')
        with self.step('步骤一：打开浏览器'):
            new_page = GWPage(base_page)
            # new_page.get_token()
            new_page.open_url("https://www.pre.webullbroker.com/ko-builder/1691465556269-158f6a")
        with self.step("步骤二：跳官网标的详情页面"):
            with new_page.page.expect_popup() as page1_info:
                new_page.page.get_by_text("跳官网标的详情页面").click()
            page1 = page1_info.value
            time.sleep(3)
            url = page1.url
            assert 'https://www.pre.webullbroker.com/quote/nasdaq-ncmi' in url

    def test_invite(self, base_page):
        self.log = Msg('test_open_account')
        with self.step('步骤一：打开浏览器'):
            new_page = GWPage(base_page)
            # new_page.get_token()
            new_page.open_url("https://www.pre.webullbroker.com/ko-builder/1691465556269-158f6a")
        with self.step("步骤二：点击跳邀请人列表"):
            page = new_page.gw_get_page("邀请人列表")
            assert "https://act.pre.webullbroker.com/actv3/invite-list" in page.url

    def test_activity(self, base_page):
        self.log = Msg('test_open_account')
        with self.step("步骤一：打开浏览器"):
            new_page = GWPage(base_page)
            new_page.get_token()
            new_page.open_url("https://www.pre.webullbroker.com/ko-builder/1691465556269-158f6a")
        with self.step("步骤二：去活动中心"):
            with new_page.page.expect_popup() as page1_info:
                new_page.page.get_by_text("跳活动中心").click()
            page1 = page1_info.value
            time.sleep(2)
            assert "https://act.pre.webullbroker.com/actv3/activity-center" in page1.url
