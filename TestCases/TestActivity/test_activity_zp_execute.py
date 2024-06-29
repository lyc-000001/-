
# Author:曾格

import allure
from Pages.PageActivity.page_acitivty_zp_execute import ActivityZpExecute
import Utils.tools


class TestActivityZpExecute:

    def step(self, msg=''):
        self.log.info(msg)
        return allure.step(msg)

    def test_activity_zp_execute(self, base_page):
        self.log = Utils.tools.Msg('invite')
        global new_page
        new_page = ActivityZpExecute(base_page)
        new_page.get_token()

        with self.step('初始化db数据'):
            ret = new_page.init_all_chance('1970001583')
            new_page.waits()
        with self.step('打开活动链接'):
            new_page.open_url_()
        with self.step('开始邀请第0人'):
            if ret is not None:
                self.log.info('开始邀请第0人')
                new_page.case_invite_zero()
        with self.step('开始邀请第1人'):
            invite_one = new_page.set_invite_i('1439', ret[0][0])  # type: ignore
            if invite_one:
                self.log.info('开始邀请第一个人')
                new_page.case_invite_one()
        with self.step('开始邀请第2人'):
            invite_two = new_page.set_invite_i('1439', ret[1][0])  # type: ignore
            if invite_two:
                self.log.info('开始邀请第二个人')
                new_page.case_invite_two()
        with self.step('开始邀请第3人'):
            invite_three = new_page.set_invite_i('1572', ret[2][0])  # type: ignore
            if invite_three:
                self.log.info('邀请第三个人，开始转盘抽奖')
                new_page.case_invite_three()
                new_page.execute_(ret[2][0])  # type: ignore
                new_page.waits()
