# -*- coding:utf-8 -*-
# Author:曾格
import time
import allure
import re
from Pages.Base import BasePage
from playwright.sync_api import expect
from Utils.tools import *
from Utils import tools
from Utils.Log import Msg
from Utils.db import *


class InvitePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.log = Msg('test_invite_page')
        msg = get_base('pre', 'us')
        self.mysql = Mysql(host=msg['mysql_host'], user=msg['mysql_user'], pwd=msg['mysql_pwd'])

    @allure.step("打开Ko测试页面")
    def open_url_(self, url):
        self.open_url(url)

    @allure.step("获取昵称")
    def isnickname_exist(self):
        """
        :return:返回邀请人昵称
        """
        # element = self.page.get_by_text("邀请人昵称-urlParams：NAH****JMA")
        element = self.wait_for_selector_('//*[@id="272d1e_3e6809"]/span')
        # self.waits()
        if element is not None:
            nick_name = element.inner_text()
            self.log.info(f'获取邀请人昵称信息成功：{nick_name}')
        else:
            nick_name = ''
        return nick_name

    def assert_invite_sql(self, invited_user_id, invite_code_source, invite_code):
        """

        :param invited_user_id:
        :return:
        """
        sql = f'SELECT id,user_id,invite_code_source,invite_code FROM wl_activity.wla_user_invite_log WHERE invited_user_id in({invited_user_id});'
        ret = self.mysql.select_sql(sql, data='all')
        self.waits()
        assert str(ret[0][1]) == '1970001583' and len(ret) == 1 and ret[0][2] == invite_code_source and ret[0][3] == invite_code
        self.log.info(f'{invite_code_source}邀请关系建立完成')


    @allure.step("点击跳官网注册并判断回调地址")
    def gw_zc(self):
        """
        :return: 返回被邀请人userid
        """
        with self.page.expect_popup() as page2_info:
            self.page.get_by_text("官网注册").click()
        page2 = page2_info.value
        phone = tools.random_phone_("us")
        time.sleep(2)
        url1 = page2.url
        page2.locator("span").filter(has_text="+1").get_by_role("textbox").click()
        page2.locator("span").filter(has_text="+1").get_by_role("textbox").fill(phone.split('-')[1])
        page2.get_by_label("").check()
        page2.get_by_text("Send code").click()
        self.waits()
        tk = page2.query_selector('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/div[2]/div/p')
        p2 = BasePage(page2)
        time.sleep(2)
        if tk is None:
            print("没有图形验证码")
        else:
            print('有图形验证码')
            p2.select_element('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/span[2]').click()
        code = str(888888)
        page2.locator("input[type=\"text\"]").fill(code)
        time.sleep(2)
        # 进入下一步设置密码页面
        page2.get_by_role("button", name="Next").click()
        time.sleep(2)
        page2.get_by_role("textbox").first.click()
        page2.get_by_role("textbox").first.fill("Aa123456")
        page2.get_by_role("textbox").nth(1).click()
        page2.get_by_role("textbox").nth(1).fill("Aa123456")
        page2.get_by_role("button", name="Sign Up").click()
        self.waits()
        # 断言回跳地址是否匹配
        expect(page2).to_have_url(re.compile(".*1664432437800-6d5cf0"))
        # 获取注册用户userid
        invited_user_id = get_user_id('pre', phone)
        if not isinstance(invited_user_id, str):
            invited_user_id = get_user_id('pre', phone)
        page2.close()
        return invited_user_id




    def testinvitecode(self):
        # table_user = 'wl_activity.wla_user_invite_code_user_'
        # table_code = 'wl_activity.wla_user_invite_code_code_'
        # sql_user = 'select count(a) from ' + table_user
        # sql_code = 'select count(b) from ' + table_code
        # count_user = 0
        # count_code = 0
        # for i in (0, 1):
        #     sql = sql_code + str(i)
        #     a = self.mysql.select_sql(sql)
        #     print(a)
        sql = 'wl_activity.wla_user_invite_code_user_29;'
        a = self.mysql.select_sql(sql)
        print(a)
