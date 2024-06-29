# Author:曾格
from Conf.config import Config
from Pages.Base import BasePage
import allure
import time
from Utils.Log import Msg
from playwright.sync_api import expect
import re
from Utils.tools import *
from Utils.tools import *

class TimeComputePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.log = Msg('test_get_TimeCompute_page')

    @allure.step("打开Ko测试页面")
    def open_url_(self):
        self.open_url('https://www.pre.webullbroker.com/ko-builder/1691389061325-d3d8bf/286fa3')

    @allure.step("等待")
    def wait_(self):
        self.waits()

    @allure.step("获取token并且注入浏览器")
    def get_token(self):
        token = tokens(environment=Config.environment, area=Config.area, user=Config.pre_webull_user_21,
                       pwd=Config.pre_webull_pwd_21)
        self.page.context.add_cookies([{
            'name': 'web_lt_pre',
            'value': f'{token}',
            'url': 'https://www.pre.webullbroker.com'
        }])

    @allure.step('页面加载后显示时间计算的所有结果')
    def load_time_compute(self):
        """
        :param base_page:
        :return:
        """
        # 获取元素：注册时间-时间戳
        self.waits()
        element_regist_time = self.wait_for_selector_('//*[@id="d70606_286fa3"]/span')
        regist_time = element_regist_time.inner_text()
        self.log.info(f'获取注册时间戳元素:{regist_time}')
        # 断言注册时间数据
        assert element_regist_time is not None and regist_time == '2021/11/21 19:11'

        # 获取元素：注册时间加七天
        element_regist_time_plus_seven = self.wait_for_selector_('//*[@id="deacbf_286fa3"]/span')
        regist_time_plus_seven = element_regist_time_plus_seven.inner_text()
        self.log.info(f'获取注册时间加七天元素:${regist_time_plus_seven}')
        # 断言数据
        assert element_regist_time_plus_seven is not None and regist_time_plus_seven == '2021/11/28 06:11'

        # 获取元素：固定时间
        element_fixed_time = self.wait_for_selector_('//*[@id="de3255_286fa3"]/span')
        fixed_time = element_fixed_time.inner_text()
        self.log.info(f'获取固定时间元素:${fixed_time}')
        # 断言数据
        assert element_fixed_time is not None and fixed_time == '2020/01/07 21:00'

        # 获取元素：时间相减计算-日期变量
        element_minus_time_date = self.wait_for_selector_('//*[@id="5c97c6_286fa3"]/span')
        minus_time_date = element_minus_time_date.inner_text()
        self.log.info(f'获取时间相减计算-日期变量元素:${minus_time_date}')
        # 断言数据
        assert element_minus_time_date is not None and minus_time_date == '59044271000'

        # 获取元素：时间相减计算-数字
        element_minus_time_number = self.wait_for_selector_('//*[@id="9ff6fd_286fa3"]/span')
        minus_time_number = element_minus_time_number.inner_text()
        self.log.info(f'获取时间相减计算-数字变量元素:${minus_time_number}')
        # 断言数据
        assert element_minus_time_number is not None and minus_time_number == '59044271000'

        # 获取元素：活动开始时间
        element_act_start_time = self.wait_for_selector_('//*[@id="a1af02_286fa3"]/span')
        act_start_time = element_act_start_time.inner_text()
        self.log.info(f'获取活动开始时间元素:${act_start_time}')
        # 断言数据
        assert element_act_start_time is not None and act_start_time == '2022/08/28 12:00'

        # 获取元素：活动结束时间
        element_act_end_time = self.wait_for_selector_('//*[@id="8edb40_286fa3"]/span')
        act_end_time = element_act_end_time.inner_text()
        self.log.info(f'获取活动结束时间元素:${act_end_time}')
        # 断言数据
        assert element_act_end_time is not None and act_end_time == '2022/10/29'

        # 获取元素：日期带时区转换
        element_date_with_switch_zone = self.wait_for_selector_('//*[@id="0f7b95_286fa3"]/span')
        date_with_switch_zone = element_date_with_switch_zone.inner_text()
        self.log.info(f'获取日期带时区转换元素:${date_with_switch_zone}')
        # 断言数据
        assert element_date_with_switch_zone is not None and date_with_switch_zone == 'Wednesday, October 9, 2024 12:00 PM'

        # 获取元素：日期不带时区转换
        element_date_without_switch_zone = self.wait_for_selector_('//*[@id="d22723_286fa3"]/span')
        date_without_switch_zone = element_date_without_switch_zone.inner_text()
        self.log.info(f'获取日期不带时区转换元素:${date_without_switch_zone}')
        # 断言数据
        assert element_date_without_switch_zone is not None and date_without_switch_zone == 'Thursday, October 10, 2024 12:00 AM'

    @allure.step('点击按钮交互事件用到日期变量')
    def click_button_time_compute(self):
        element_hide_time = self.select_element('//*[@id="e193ea_286fa3"]')
        element_hide_time.click()
        self.waits()
        element_hide_time_ = self.select_element('//*[@id="e193ea_286fa3"]')
        self.log.info('点击按钮交互事件用到日期变量:交互生效隐藏自身')
        assert element_hide_time_ is None

        element_not_hide_time = self.wait_for_selector_('//*[@id="51b83c_286fa3"]')
        element_not_hide_time.click()
        self.log.info('点击按钮交互事件用到日期变量:交互不生效不影响展示')
        assert element_not_hide_time is not None
        self.waits()
