# Author:曾格

import time
import allure
from Pages.PageComponent.page_invite import InvitePage
import Utils.tools


class TestInvite:

    def step(self, msg=''):
        self.log.info(msg)
        return allure.step(msg)

    def test_invite(self, base_page):
        self.log = Utils.tools.Msg('invite')

        with self.step("步骤一：打开分享落地页"):
            new_page = InvitePage(base_page)
            new_page.open_url("https://www.pre.webullbroker.com/s/V4yk6hrXeIJIiLC1cJ")
            new_page.waits()
            ret = new_page.isnickname_exist()
            assert ret == '邀请人昵称-urlParams：NAH****JMA'
            new_page.waits()

        with self.step("步骤二：点击跳官网注册并判断回调地址以及邀请关系"):
            invited_user_id = new_page.gw_zc()
            new_page.waits()
            new_page.assert_invite_sql(invited_user_id, 'invite_default', 'k6hrXeIJIiLC')
