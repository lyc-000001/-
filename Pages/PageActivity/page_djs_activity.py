from Pages.Base import BasePage
from Utils.db import Mongo, Mysql, Redis

import allure
import time
from datetime import datetime
from Utils.tools import get_base, tokens
from Conf.config import Config


class DjsPage(BasePage):
    def __init__(self, page, log):
        super().__init__(page)
        self.log = log
        msg = get_base("pre", "us")
        self.mysql = Mysql(host=msg["mysql_host"], user=msg["mysql_user"], pwd=msg["mysql_pwd"], port=3306)

    @allure.step("初始化未满48小时数据")
    def initialization_data(self):
        # 链接数据库
        self.mysql.connect()
        # 获取当前时间
        current_timestamp = int(time.time())
        datetime_obj1 = datetime.fromtimestamp(current_timestamp)
        date_string1 = datetime_obj1.strftime("%Y-%m-%d %H:%M:%S")
        # 清除23用户的奖励机会
        sql1 = 'UPDATE  wl_oas.`wlo_reward_rule_chance` set chance_status=0,reward_info=NULL,user_id =194000020,create_time =\'' + str(
            date_string1) + '\'where id=624601923194880;'
        sql3 = 'DELETE from wl_oas.`wlo_reward_rule_record`  where user_id =1940000209 AND activity_id =4433;'
        self.mysql.sql_perform(sql1)
        self.mysql.sql_perform(sql3)
        # 清除23用户的奖励活动步骤
        mongo = Mongo(host='10.70.1.69', table_name='oas_mkt_step_option_33', db_name='oas')
        mongo.delete_(filters={'activityId': 4433, 'stepId': '08JO2MDU9232CK2PLGCT7F9NPA.4433'})
        mongo.update_one(filters={'activityId': 4433, 'stepId': 'O4IAAQ80IHCE36DUHFL6UM1VG8.4433'},
                         up_date={'bizTime': current_timestamp * 1000, 'userId': 194000020})
        mongo.update_one(filters={'activityId': 4433, 'stepId': 'L1JMC0VG73DCD9HM0CKHS6PV18.4433'},
                         up_date={'bizTime': current_timestamp * 1000, 'userId': 194000020})
        mongo.close()
        # 修改活动参数时间
        msg = get_base('pre', 'us')
        if (current_timestamp > 1710000000) and (current_timestamp < 1730563200):
            # 夏令时时间因为减少了一个小时，这里多加一个小时
            act_time = int(current_timestamp + 90000)
        else:
            # 冬令时时间
            act_time = int(current_timestamp + 86400)
        datetime_obj = datetime.fromtimestamp(act_time)
        date_string = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
        print(act_time)
        sql = 'UPDATE wl_oas.`oas_act_sys_param` set extend=\'{"startTime":"2023-08-28 00:00:00","endTime":"' + date_string + '","timeZone":"America/New_York","regionId":6,"actId":4433,"awardPoolId":[1853],"reportActList":[]}\' WHERE act_type =\'act_eedd\';'
        self.mysql.sql_perform(sql)
        # 删除活动时间的redis缓存
        redis = Redis(host=msg['redis'])
        redis.delete_(key="oas.activity.act_eedd")
        return current_timestamp

    @allure.step("模拟步骤二完成")
    def simulation_steps_2(self):
        # 获取当前时间
        current_timestamp = int(time.time())
        # 完成步骤二
        mongo = Mongo(host='10.70.1.69', table_name='oas_mkt_step_option_33', db_name='oas')
        mongo.update_one(filters={'activityId': 4433, 'stepId': 'L1JMC0VG73DCD9HM0CKHS6PV18.4433'},
                         up_date={'bizTime': current_timestamp * 1000, 'userId': 1940000209})
        mongo.close()

    @allure.step("模拟步骤三完成")
    def simulation_steps_3(self):
        # 获取当前时间
        current_timestamp = int(time.time())
        # 完成步骤二
        mongo = Mongo(host='10.70.1.69', table_name='oas_mkt_step_option_33', db_name='oas')
        mongo.update_one(filters={'activityId': 4433, 'stepId': 'O4IAAQ80IHCE36DUHFL6UM1VG8.4433'},
                         up_date={'bizTime': current_timestamp * 1000, 'userId': 1940000209})
        mongo.close()

    @allure.step("模拟获得奖励")
    def simulation_steps_4(self):
        # 链接数据库
        self.mysql.connect()
        # 获取当前时间
        current_timestamp = int(time.time())
        datetime_obj1 = datetime.fromtimestamp(current_timestamp)
        date_string1 = datetime_obj1.strftime("%Y-%m-%d %H:%M:%S")
        # 23用户获得奖励机会
        sql1 = 'UPDATE  wl_oas.`wlo_reward_rule_chance` set chance_status=0,reward_info=NULL,user_id =1940000209,create_time =\'' + str(
            date_string1) + '\'where id=624601923194880;'
        sql3 = 'DELETE from wl_oas.`wlo_reward_rule_record`  where user_id =1940000209 AND activity_id =4433;'
        self.mysql.sql_perform(sql1)
        self.mysql.sql_perform(sql3)

    @allure.step("初始化超过48小时数据")
    def initialization_data_48(self):
        # 链接数据库
        self.mysql.connect()
        # 获取当前时间
        current_timestamp = int(time.time())
        datetime_obj1 = datetime.fromtimestamp(current_timestamp)
        date_string1 = datetime_obj1.strftime("%Y-%m-%d %H:%M:%S")
        # 清除23用户的奖励机会
        sql1 = 'UPDATE  wl_oas.`wlo_reward_rule_chance` set chance_status=0,reward_info=NULL,user_id =194000020,create_time =\'' + str(
            date_string1) + '\'where id=624601923194880;'
        sql3 = 'DELETE from wl_oas.`wlo_reward_rule_record`  where user_id =1940000209 AND activity_id =4433;'
        self.mysql.sql_perform(sql1)
        self.mysql.sql_perform(sql3)
        # 清除23用户的奖励活动步骤
        mongo = Mongo(host='10.70.1.69', table_name='oas_mkt_step_option_33', db_name='oas')
        mongo.delete_(filters={'activityId': 4433, 'stepId': '08JO2MDU9232CK2PLGCT7F9NPA.4433'})
        mongo.update_one(filters={'activityId': 4433, 'stepId': 'O4IAAQ80IHCE36DUHFL6UM1VG8.4433'},
                         up_date={'bizTime': current_timestamp * 1000, 'userId': 194000020})
        mongo.update_one(filters={'activityId': 4433, 'stepId': 'L1JMC0VG73DCD9HM0CKHS6PV18.4433'},
                         up_date={'bizTime': current_timestamp * 1000, 'userId': 194000020})
        mongo.close()
        # 修改活动参数时间
        msg = get_base('pre', 'us')
        act_time = int(current_timestamp + 172800)
        datetime_obj = datetime.fromtimestamp(act_time)
        date_string = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
        print(date_string)
        sql = 'UPDATE wl_oas.`oas_act_sys_param` set extend=\'{"startTime":"2023-08-28 00:00:00","endTime":"' + date_string + '","timeZone":"America/New_York","regionId":6,"actId":4433,"awardPoolId":[1853],"reportActList":[]}\' WHERE act_type =\'act_eedd\';'
        self.mysql.sql_perform(sql)
        # 删除活动时间的redis缓存
        redis = Redis(host=msg['redis'])
        redis.delete_(key="oas.activity.act_eedd")
        return current_timestamp

    @allure.step("获取token并且注入浏览器")
    def get_token(self):
        token = tokens(environment=Config.environment, area=Config.area, user=Config.pre_webull_user_23,
                       pwd=Config.pre_webull_pwd_23)
        self.page.context.add_cookies([{
            'name': 'web_lt_pre',
            'value': f'{token}',
            'url': 'https://www.pre.webullbroker.com'
        }])

    @allure.step("打开url")
    def open_url_(self):
        self.open_url("https://www.pre.webullbroker.com/ko-builder/1699256682656-1834f0")

    @allure.step("查找入场弹窗")
    def wait_for_selector_01(self):
        return self.wait_for_selector_('//*[@id="0893a6_a3b053"]/img')

    @allure.step("点击关闭弹窗")
    def click_element_01(self):
        self.click_element('//*[@id="7e58a2_a3b053"]/div[2]/img')

    @allure.step("查找happy组件")
    def wait_for_selector_02(self):
        return self.wait_for_selector_('//*[@id="a4e4cb_a3b053"]/img')

    @allure.step("点击打开HowTo")
    def click_element_02(self):
        self.click_element('//*[@id="8ab4b3_a3b053"]/img')

    @allure.step("获取倒计时组件")
    def wait_for_selector_03(self):
        h = self.wait_for_selector_('//*[@id="3c5591_a3b053"]')
        m = self.wait_for_selector_('//*[@id="1e9870_a3b053"]')
        s = self.wait_for_selector_('//*[@id="647266_a3b053"]')
        return h, m, s

    @allure.step("获取人物头像")
    def wait_for_selector_04(self):
        return self.wait_for_selector_('//*[@id="297f6c_a3b053"]/img')

    @allure.step("点击报名")
    def click_element_03(self):
        self.click_button(element='Get started', exact=True)

    @allure.step("获取报名后的倒计时弹窗")
    def wait_for_selector_05(self):
        return self.wait_for_selector_('//*[@id="486f23_a3b053"]')

    @allure.step("获取弹窗倒计时的时间")
    def get_text_01(self):
        self.waits()
        h = self.get_text('//*[@id="62a64d_a3b053"]/span')
        m = self.get_text('//*[@id="3985ef_a3b053"]/span')
        s = self.get_text('//*[@id="9c643b_a3b053"]/span')
        djs_time = int(h) * 3600 + int(m) * 60 + int(s)
        return djs_time

    @allure.step("点击关闭倒计时弹窗")
    def click_element_04(self):
        self.click_element('//*[@id="5e4f83_a3b053"]/div[3]/img')

    @allure.step("获取主页面倒计时时间")
    def get_text_02(self):
        self.waits()
        h = self.get_text('//*[@id="709ccb_a3b053"]/span')
        m = self.get_text('//*[@id="094b85_a3b053"]/span')
        s = self.get_text('//*[@id="076f2c_a3b053"]/span')
        djs_time = int(h) * 3600 + int(m) * 60 + int(s)
        return djs_time

    @allure.step("点击打开HOW TO")
    def click_element_05(self):
        self.click_element('//*[@id="8ab4b3_a3b053"]/img')

    @allure.step("获取HOW TO的人物头像")
    def wait_for_selector_06(self):
        return self.wait_for_selector_('//*[@id="297f6c_a3b053"]/img')

    @allure.step("获取HOW TO中的倒计时时间")
    def get_text_03(self):
        self.waits()
        h = self.get_text('//*[@id="1430a6_a3b053"]/span')
        m = self.get_text('//*[@id="727b86_a3b053"]/span')
        s = self.get_text('//*[@id="f3fa08_a3b053"]/span')
        djs_time = int(h) * 3600 + int(m) * 60 + int(s)
        return djs_time

    @allure.step("获取HOW TO的人数文案")
    def get_text_04(self):
        return self.get_text('//*[@id="f86180_a3b053"]/span')

    @allure.step("点击关闭HOW TO")
    def click_element_06(self):
        self.click_element('//*[@id="53f25f_a3b053"]/img')

    @allure.step("点击打开Cash弹窗")
    def click_element_07(self):
        self.click_element('//*[@id="9e5b54_a3b053"]/img')

    @allure.step("获取Cash弹窗的人数文案")
    def get_text_05(self):
        return self.get_text('//*[@id="be0c1a_a3b053"]/span')

    @allure.step("获取报名后Cash弹窗中的倒计时")
    def get_text_06(self):
        self.waits()
        h = self.get_text('//*[@id="e306e6_a3b053"]/span')
        m = self.get_text('//*[@id="0f48a8_a3b053"]/span')
        s = self.get_text('//*[@id="a50663_a3b053"]/span')
        djs_time = int(h) * 3600 + int(m) * 60 + int(s)
        return djs_time

    @allure.step("获取入场弹窗的人数文案")
    def get_text_07(self):
        return self.get_text('//*[@id="be0c1a_a3b053"]/span')

    @allure.step("获取报名后入场弹窗中的倒计时")
    def get_text_08(self):
        self.waits()
        h = self.get_text('//*[@id="e306e6_a3b053"]/span')
        m = self.get_text('//*[@id="0f48a8_a3b053"]/span')
        s = self.get_text('//*[@id="a50663_a3b053"]/span')
        djs_time = int(h) * 3600 + int(m) * 60 + int(s)
        return djs_time

    @allure.step("点击关闭入场倒计时弹窗")
    def click_element_08(self):
        self.click_element('//*[@id="0fa822_a3b053"]/div[5]/img')

    @allure.step("点击抽奖按钮")
    def click_element_09(self):
        self.click_element('//*[@id="3eeb0e_a3b053"]')

    @allure.step("获取抽奖按钮弹窗的人数文案")
    def get_text_09(self):
        return self.get_text('//*[@id="be0c1a_a3b053"]/span')

    @allure.step("获取报名后抽奖按钮弹窗中的倒计时的时间")
    def get_text_10(self):
        self.waits()
        h = self.get_text('//*[@id="e306e6_a3b053"]/span')
        m = self.get_text('//*[@id="0f48a8_a3b053"]/span')
        s = self.get_text('//*[@id="a50663_a3b053"]/span')
        djs_time = int(h) * 3600 + int(m) * 60 + int(s)
        return djs_time

    @allure.step("获取报名+邀请注册后的入场弹窗")
    def wait_for_selector_07(self):
        return self.wait_for_selector_('//*[@id="cc9632_a3b053"]')

    @allure.step("点击关闭报名+邀请注册后的入场弹窗")
    def click_element_10(self):
        self.click_element('//*[@id="ead22c_a3b053"]/div[3]/img')

    @allure.step("点击打开报名+邀请注册后的HOW TO页面")
    def click_element_11(self):
        self.click_element('//*[@id="8ab4b3_a3b053"]/img')

    @allure.step("获取报名+邀请注册后的入场弹窗")
    def wait_for_selector_08(self):
        return self.wait_for_selector_('//*[@id="9ae0c1_a3b053"]/img')

    @allure.step("点击关闭HOW TO页面")
    def click_element_12(self):
        self.click_element('//*[@id="53f25f_a3b053"]/img')

    @allure.step("点击打开Cash弹窗")
    def click_element_13(self):
        self.click_element('//*[@id="9e5b54_a3b053"]/img')

    @allure.step("获取报名+邀请注册后的Cash弹窗")
    def wait_for_selector_09(self):
        return self.wait_for_selector_('//*[@id="89b932_a3b053"]')

    @allure.step("点击打开HOW TO")
    def click_element_14(self):
        self.click_element('//*[@id="8ab4b3_a3b053"]/img')

    @allure.step("获取报名+邀请注册+入金后How To中的人物头像")
    def wait_for_selector_10(self):
        return self.wait_for_selector_('//*[@id="9ae0c1_a3b053"]/img')

    @allure.step("点击关闭HOW TO")
    def click_element_15(self):
        self.click_element('//*[@id="53f25f_a3b053"]/img')

    @allure.step("点击打开报名+邀请注册+入金后cash弹窗")
    def click_element_16(self):
        self.click_element('//*[@id="9e5b54_a3b053"]/img')

    @allure.step("获取报名+邀请注册+入金后cash弹窗")
    def wait_for_selector_11(self):
        return self.wait_for_selector_('//*[@id="89b932_a3b053"]')

    @allure.step("点击关闭cash弹窗")
    def click_element_17(self):
        self.click_element('//*[@id="0383f7_a3b053"]/div[3]/img')

    @allure.step("点击抽奖按钮")
    def click_element_18(self):
        self.click_element('//*[@id="3eeb0e_a3b053"]')

    @allure.step("获取获奖弹窗")
    def wait_for_selector_12(self):
        return self.wait_for_selector_('//*[@id="2ddf72_a3b053"]/span')

    # 超过48小时
    @allure.step("获取入场弹窗")
    def wait_for_selector_13(self):
        return self.wait_for_selector_('//*[@id="50ef79_a3b053"]/img')

    @allure.step("点击关闭弹窗")
    def click_element_19(self):
        self.click_element('//*[@id="7e58a2_a3b053"]/div[2]/img')

    @allure.step("获取主页倒计时组件")
    def wait_for_selector_14(self):
        return self.wait_for_selector_('//*[@id="1d0c2f_a3b053"]')

    @allure.step("点击打开HOW TO")
    def click_element_20(self):
        self.click_element('//*[@id="8ab4b3_a3b053"]/img')

    @allure.step("获取报名后抽奖按钮弹窗中的倒计时的时间")
    def get_text_11(self):
        self.waits()
        h = self.get_text('//*[@id="3d967b_a3b053"]/span')
        m = self.get_text('//*[@id="e50aab_a3b053"]/span')
        s = self.get_text('//*[@id="2fd91b_a3b053"]/span')
        return h, m, s

    @allure.step("获取HOW TO的人物头像")
    def wait_for_selector_15(self):
        return self.wait_for_selector_('//*[@id="297f6c_a3b053"]/img')

    @allure.step("获取HOW TO的邀请人数")
    def get_text_12(self):
        return self.get_text('//*[@id="f86180_a3b053"]/span')

    @allure.step("点击报名")
    def click_element_21(self):
        self.click_button(element='Get started', exact=True)

    @allure.step("获取报名后的倒计时弹窗")
    def wait_for_selector_16(self):
        return self.wait_for_selector_('//*[@id="486f23_a3b053"]')

    @allure.step("获取报名后弹窗中的倒计时的时间")
    def get_text_13(self):
        self.waits()
        h = self.get_text('//*[@id="d896e9_a3b053"]/span')
        m = self.get_text('//*[@id="96e2d1_a3b053"]/span')
        s = self.get_text('//*[@id="b6e32f_a3b053"]/span')
        djs_time = int(h) * 3600 + int(m) * 60 + int(s)
        return djs_time

    @allure.step("点击关闭弹窗")
    def click_element_22(self):
        self.click_element('//*[@id="5e4f83_a3b053"]/div[3]/img')

    @allure.step("获取报名后主页中的倒计时时间")
    def get_text_14(self):
        self.waits()
        h = self.get_text('//*[@id="409482_a3b053"]/span')
        m = self.get_text('//*[@id="057ad1_a3b053"]/span')
        s = self.get_text('//*[@id="409a4e_a3b053"]/span')
        djs_time = int(h) * 3600 + int(m) * 60 + int(s)
        return djs_time

    @allure.step("点击打开HOW TO")
    def click_element_23(self):
        self.click_element('//*[@id="8ab4b3_a3b053"]/img')

    @allure.step("获取HOW TO的人物头像")
    def wait_for_selector_17(self):
        return self.wait_for_selector_('//*[@id="297f6c_a3b053"]/img')

    @allure.step("获取报名后HOW TO中的倒计时时间")
    def get_text_15(self):
        self.waits()
        h = self.get_text('//*[@id="3d967b_a3b053"]/span')
        m = self.get_text('//*[@id="e50aab_a3b053"]/span')
        s = self.get_text('//*[@id="2fd91b_a3b053"]/span')
        djs_time = int(h) * 3600 + int(m) * 60 + int(s)
        print('--------------------', h, m, s)
        return djs_time

    @allure.step("获取报名后HOW TO人数文案")
    def get_text_16(self):
        return self.get_text('//*[@id="f86180_a3b053"]/span')

    @allure.step("点击关闭HOW TO")
    def click_element_24(self):
        self.click_element('//*[@id="53f25f_a3b053"]/img')

    @allure.step("点击打开Cash弹窗")
    def click_element_25(self):
        self.click_element('//*[@id="9e5b54_a3b053"]/img')

    @allure.step("获取Cash弹窗的人数文案")
    def get_text_17(self):
        return self.get_text('//*[@id="be0c1a_a3b053"]/span')

    @allure.step("获取报名后HOW TO中的倒计时时间")
    def get_text_18(self):
        self.waits()
        h = self.get_text('//*[@id="32727d_a3b053"]/span')
        m = self.get_text('//*[@id="b7cc1f_a3b053"]/span')
        s = self.get_text('//*[@id="a94366_a3b053"]/span')
        djs_time = int(h) * 3600 + int(m) * 60 + int(s)
        return djs_time

    @allure.step("获取入场弹窗的人数文案")
    def get_text_19(self):
        return self.get_text('//*[@id="be0c1a_a3b053"]/span')

    @allure.step("获取报名后入场弹窗中的倒计时时间")
    def get_text_20(self):
        self.waits()
        h = self.get_text('//*[@id="32727d_a3b053"]/span')
        m = self.get_text('//*[@id="b7cc1f_a3b053"]/span')
        s = self.get_text('//*[@id="a94366_a3b053"]/span')
        djs_time = int(h) * 3600 + int(m) * 60 + int(s)
        return djs_time

    @allure.step("点击关闭入场弹窗")
    def click_element_26(self):
        self.click_element('//*[@id="0fa822_a3b053"]/div[5]/img')

    @allure.step("点击抽奖按钮")
    def click_element_27(self):
        self.click_element('//*[@id="3eeb0e_a3b053"]')

    @allure.step("获取抽奖按钮弹窗的人数文案")
    def get_text_21(self):
        return self.get_text('//*[@id="be0c1a_a3b053"]/span')

    @allure.step("获取报名后抽奖按钮弹窗中的倒计时")
    def get_text_22(self):
        self.waits()
        h = self.get_text('//*[@id="32727d_a3b053"]/span')
        m = self.get_text('//*[@id="b7cc1f_a3b053"]/span')
        s = self.get_text('//*[@id="a94366_a3b053"]/span')
        djs_time = int(h) * 3600 + int(m) * 60 + int(s)
        return djs_time

    @allure.step("获取报名+邀请注册后的入场弹窗")
    def wait_for_selector_18(self):
        return self.wait_for_selector_('//*[@id="cc9632_a3b053"]')

    @allure.step("点击关闭入场弹窗")
    def click_element_28(self):
        self.click_element('//*[@id="ead22c_a3b053"]/div[3]/img')

    @allure.step("点击打开HOW TO")
    def click_element_29(self):
        self.click_element('//*[@id="8ab4b3_a3b053"]/img')

    @allure.step("获取报名+邀请注册后的HOW TO页面")
    def wait_for_selector_19(self):
        return self.wait_for_selector_('//*[@id="9ae0c1_a3b053"]/img')

    @allure.step("点击关闭HOW TO")
    def click_element_30(self):
        self.click_element('//*[@id="53f25f_a3b053"]/img')

    @allure.step("点击打开Cash弹窗")
    def click_element_31(self):
        self.click_element('//*[@id="9e5b54_a3b053"]/img')

    @allure.step("获取报名+邀请注册后的Cash弹窗")
    def wait_for_selector_20(self):
        return self.wait_for_selector_('//*[@id="89b932_a3b053"]')

    @allure.step("点击打开HOW TO")
    def click_element_32(self):
        self.click_element('//*[@id="8ab4b3_a3b053"]/img')

    @allure.step("获取报名+邀请注册+入金后How To中的人物头像")
    def wait_for_selector_21(self):
        return self.wait_for_selector_('//*[@id="9ae0c1_a3b053"]/img')

    @allure.step("点击关闭HOW TO")
    def click_element_33(self):
        self.click_element('//*[@id="53f25f_a3b053"]/img')

    @allure.step("点击打开报名+邀请注册+入金后cash弹窗")
    def click_element_34(self):
        self.click_element('//*[@id="9e5b54_a3b053"]/img')

    @allure.step("获取报名+邀请注册+入金后cash弹窗")
    def wait_for_selector_22(self):
        return self.wait_for_selector_('//*[@id="89b932_a3b053"]')

    @allure.step("点击关闭cash弹窗")
    def click_element_35(self):
        self.click_element('//*[@id="0383f7_a3b053"]/div[3]/img')

    @allure.step("点击抽奖按钮")
    def click_element_36(self):
        self.click_element('//*[@id="3eeb0e_a3b053"]')

    @allure.step("获取获奖弹窗")
    def wait_for_selector_23(self):
        return self.wait_for_selector_('//*[@id="ea9227_a3b053"]')


if __name__ == '__main__':
    djs = DjsPage(BasePage, log=11)
    djs.initialization_data()
    # djs.initialization_data_48()
