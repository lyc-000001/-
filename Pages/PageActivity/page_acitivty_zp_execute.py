# -*- coding:utf-8 -*-
import time
import allure
import re

from Conf.config import Config
from Pages.Base import BasePage
from playwright.sync_api import expect
from Utils.tools import *
from Utils.db import *


class ActivityZpExecute(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.log = Msg('test_activity_zp_execute')
        msg = get_base('pre', 'us')
        self.mysql = Mysql(host=msg['mysql_host'], user=msg['mysql_user'], pwd=msg['mysql_pwd'])

    @allure.step("打开Ko测试页面")
    def open_url_(self):
        """
        :param url:
        :return:
        """
        self.open_url('https://www.pre.webullbroker.com/ko-builder/1692155351756-166b0d')

    @allure.step("获取转盘活动的所有chanceid记录")
    def init_all_chance(self, user_id):
        """
        :param user_id: 邀请人userid
        :return: 被邀请人userid数组
        """
        sql = f'SELECT invited_user_id from  wl_oas.`wlo_reward_rule_chance` where activity_id IN(2943) and user_id in({user_id}) ORDER BY create_time desc limit 1000'
        ret = self.mysql.select_sql(sql, data=all) # type: ignore
        for i in ret: # type: ignore
            sql1 = f'UPDATE  wl_oas.`wlo_reward_rule_chance` set chance_status=0,reward_info=NULL,pool_id=1500 where invited_user_id = {i[0]} AND activity_id IN(2943);'
            self.mysql.sql_perform(sql1)
            sql2 = f'DELETE from wl_oas.`wlo_reward_rule_record`  where chance_id IN (SELECT id from  wl_oas.`wlo_reward_rule_chance` where invited_user_id in({i[0]}) AND activity_id IN(2943));'
            self.mysql.sql_perform(sql2)
        return ret

    @allure.step("获取token并且注入浏览器")
    def get_token(self):
        token = tokens(environment=Config.environment, area=Config.area, user=Config.pre_webull_user_21,
                       pwd=Config.pre_webull_pwd_21)
        self.page.context.add_cookies([{
            'name': 'web_lt_pre',
            'value': f'{token}',
            'url': 'https://www.pre.webullbroker.com'
        }])

    @allure.step("设置邀请人数")
    def set_invite_i(self, pool_id, invited_user_id):
        """
        :param pool_id:奖励池id
        :param invited_user_id:被邀请人userid
        :return:
        """
        sql = f'UPDATE  wl_oas.`wlo_reward_rule_chance` set chance_status=0,reward_info=NULL,pool_id={pool_id} where invited_user_id={invited_user_id} AND activity_id IN(2943);'
        self.mysql.sql_perform(sql)
        updated_pool_id = self.mysql.select_sql(
            f'SELECT pool_id from  wl_oas.`wlo_reward_rule_chance` where activity_id IN(2943) and invited_user_id={invited_user_id}')
        if str(updated_pool_id[0]) == pool_id: # type: ignore
            self.log.info(f'初始化邀请人数成功-{invited_user_id}--{updated_pool_id[0]}') # type: ignore
            return True
        else:
            self.log.info(f'初始化邀请人数失败-{invited_user_id}--{updated_pool_id[0]}') # type: ignore
            return False

    @allure.step("邀请0人")
    def case_invite_zero(self):
        """
        :return:
        """
        self.page.reload()
        #time.sleep(1)
        #self.waits()
        # 邀请0人的弹框
        #element_0_tk = self.page.locator('//*[@id="914a56_858230"]/span')
        element_tk_zero = self.wait_for_selector_('//*[@id="914a56_858230"]/span')
        if element_tk_zero is not None:
            self.log.info('邀请0人弹框存在')
            # 获取邀请0人弹框的文本
            #time.sleep(1)
            #self.waits()
            text_zero = element_tk_zero.inner_text()
            self.log.info(f'邀请0人弹框的文本内容：{text_zero}')
            # 断言文案
            assert "You've successfully invited 0 friend(s) to funded their new Webull account! Just 3 more" in text_zero
            # 关闭弹框
            element_close_btn = self.wait_for_selector_('//*[@id="66a9de_858230"]/div[5]/img')
            element_close_btn.click()

        # 获取首页邀请人数弹框
        element_number_zero = self.wait_for_selector_('//*[@id="efe5be_858230"]/span')
        number_zero = element_number_zero.inner_text()
        assert number_zero == '0'
        element_refer = self.wait_for_selector_('//*[@id="fca44a_858230"]/span')
        #time.sleep(5)
        #self.waits()
        self.log.info('滑到Refer more, get more!')
        element_refer.scroll_into_view_if_needed()
        # 获取进度条节点1元素，第一个节点不能点亮
        element_jdt_zero = self.wait_for_selector_('//*[@id="ca55f0_858230_node"]')
        #time.sleep(1)
        #self.waits()
        assert element_jdt_zero is not None

    @allure.step("邀请1人")
    def case_invite_one(self, ):
        """
        :return:
        """
        self.page.reload()
        #time.sleep(1)
        #self.waits()
        # 邀请1人的弹框里的文本元素
        element_one_tk = self.wait_for_selector_('//*[@id="914a56_858230"]/span')
        if element_one_tk is not None:
            self.log.info('邀请1人弹框存在')
            # 获取邀请1人弹框的文本
            text_one = element_one_tk.inner_text()
            self.log.info(f'邀请0人弹框的文本内容：{text_one}')
            # time.sleep(1)
            #self.waits()
            # 断言文案
            assert "You've successfully invited 1 friend(s) to funded their new Webull account! Just 2 more" in text_one
            # 关闭弹框
            element_close_btn = self.wait_for_selector_('//*[@id="66a9de_858230"]/div[5]/img')
            element_close_btn.click()
        # 获取首页邀请人数文本值
        element_number_one = self.wait_for_selector_('//*[@id="efe5be_858230"]/span')
        number_one = element_number_one.inner_text()
        assert number_one == '1'
        element_refer = self.wait_for_selector_('//*[@id="fca44a_858230"]/span')
        #time.sleep(5)
        #self.waits()
        self.log.info('滑到Refer more, get more!')
        element_refer.scroll_into_view_if_needed()
        # 获取进度条节点1元素，第一个节点需要点亮
        element_jdt_one = self.wait_for_selector_('//*[@id="6a40c5_858230_node"]')
        # time.sleep(1)
        #self.waits()
        assert element_jdt_one is not None

    @allure.step("邀请2人")
    def case_invite_two(self):
        """
        :return:
        """
        self.page.reload()
        # time.sleep(1)
        #self.waits()
        element_two_tk = self.wait_for_selector_('//*[@id="914a56_858230"]/span')
        if element_two_tk is not None:
            self.log.info('邀请2人弹框存在')
            # print('邀请2人弹框存在')
            # 获取邀请2人弹框的文本
            text_two = element_two_tk.inner_text()
            # print(text_2)
            # time.sleep(1)
            # self.waits()
            # 断言文案
            assert "You've successfully invited 2 friend(s) to funded their new Webull account! Just 1 more" in text_two
            # 关闭弹框
            element_close_btn = self.wait_for_selector_('//*[@id="66a9de_858230"]/div[5]/img')
            element_close_btn.click()
        # self.waits()
        # 获取首页邀请人数文本值
        element_number_two = self.wait_for_selector_('//*[@id="efe5be_858230"]/span')
        number_two = element_number_two.inner_text()
        # print(number_2)
        assert number_two == '2'
        element_refer = self.wait_for_selector_('//*[@id="fca44a_858230"]/span')
        # time.sleep(5)
        # self.waits()
        self.log.info('滑到Refer more, get more!')
        element_refer.scroll_into_view_if_needed()
        # 获取进度条节点2元素，第2个节点需要点亮
        element_jdt_two = self.wait_for_selector_('//*[@id="e16c1e_858230_node"]')
        # time.sleep(1)
        # self.waits()
        assert element_jdt_two is not None

    @allure.step("邀请3人")
    def case_invite_three(self):
        """
        :return:
        """
        self.page.reload()
        # time.sleep(1)
        # self.waits()
        element_three_tk = self.wait_for_selector_('//*[@id="c07800_858230"]/span')
        if element_three_tk is not None:
            self.log.info('邀请3人弹框存在')
            text_three = element_three_tk.inner_text()
            # time.sleep(1)
            # self.waits()
            # 断言文案
            assert "You now have a chance to spin the wheel to get up to 20 shares of AAPL" in text_three
            # 关闭弹框
            element_close_btn = self.wait_for_selector_('//*[@id="5b1165_858230"]/div[3]/img')
            element_close_btn.click()
        # self.waits()
        # 获取首页邀请人数文本值
        element_number_three = self.wait_for_selector_('//*[@id="efe5be_858230"]/span')
        number_three = element_number_three.inner_text()        # print(number_3)
        assert number_three == '3'
        # 进度条容器组件
        element_refer = self.wait_for_selector_('//*[@id="fca44a_858230"]/span')
        # time.sleep(5)
        # self.waits()
        self.log.info('滑到Refer more, get more!')
        element_refer.scroll_into_view_if_needed()
        # 获取进度条节点3元素，第3个节点需要点亮
        element_jdt_three = self.wait_for_selector_('//*[@id="df2ac3_858230_node"]')
        # time.sleep(1)
        # self.waits()
        element_jdt_three.scroll_into_view_if_needed()
        assert element_jdt_three is not None
        # 点击开始抽奖
        element_draw = self.wait_for_selector_('//*[@id="58f054_858230"]/div[1]')
        element_draw.click()
        # self.page.locator('//*[@id="58f054_858230"]/div[1]').click()
        # self.waits()
        element_draw_tk = self.wait_for_selector_('//*[@id="47117f_858230"]/span')
        assert element_draw_tk is not None

    @allure.step("查询抽奖数据")
    def execute_(self, invited_user_id):
        """
        :param invited_user_id:被邀请人userid
        :return:
        """
        sql = f'select chance_status from wl_oas.`wlo_reward_rule_chance` where pool_id = 1572 and invited_user_id = {invited_user_id};'
        # 获取奖励机会的chance_status字段
        ret = self.mysql.select_sql(sql, data=all) # type: ignore
        # print(ret[0][0])
        # 抽奖结果弹框
        element_draw_tk = self.page.locator('//*[@id="47117f_858230"]/span')
        # time.sleep(1)
        self.waits()
        assert element_draw_tk is not None and str(ret[0][0]) == "1" # type: ignore
        self.log.info('第一次转盘抽奖成功')
