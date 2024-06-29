# Author:曾格
from Conf.config import Config
from Pages.Base import BasePage
import allure
import time
from Utils.Log import Msg
from playwright.sync_api import expect
import re
from Utils.tools import *

class KMBPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.log = Msg('test_get_KMB_page')

    @allure.step("打开Ko测试页面")
    def open_url_(self):
        self.open_url('https://www.pre.webullbroker.com/ko-builder/1691389061325-d3d8bf/a16f81')

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

    @allure.step('页面加载后显示KMB计算结果')
    def load_kmb(self):
        """
        :param base_page:
        :return:
        """
        # 获取元素：888888888.12
        # time.sleep(1)
        element_data_one = self.wait_for_selector_('//*[@id="4f7044_a16f81"]/span')
        data_one = element_data_one.inner_text()
        self.log.info(f'获取888888888.12元素:{data_one}')
        # 断言888888888.12数据
        assert element_data_one is not None and data_one == '+888.89M'

        # 获取元素：77777777
        # time.sleep(1)
        element_data_two = self.wait_for_selector_('//*[@id="33a6c5_a16f81"]/span')
        data_two = element_data_two.inner_text()
        self.log.info(f'77777777:{data_two}')
        # 断言77777777数据
        assert element_data_two is not None and data_two == '+77.7778M'

        # 获取元素：3333
        # time.sleep(1)
        element_data_three = self.wait_for_selector_('//*[@id="eab105_a16f81"]/span')
        data_three = element_data_three.inner_text()
        self.log.info(f'获取3333元素:{data_three}')
        # 断言3333数据
        assert element_data_three is not None and data_three == '3.34K'

        # 获取元素：99.99
        # time.sleep(1)
        element_data_four = self.wait_for_selector_('//*[@id="a8a2e6_a16f81"]/span')
        data_four = element_data_four.inner_text()
        self.log.info(f'获取99.99元素:{data_four}')
        # 断言99.99数据
        assert element_data_four is not None and data_four == '+99.99'

        # 获取元素：998877

        element_data_five = self.wait_for_selector_('//*[@id="7e18bd_a16f81"]/span')
        data_five = element_data_five.inner_text()
        self.log.info(f'获取998877元素:{data_five}')
        # 断言998877数据
        assert element_data_five is not None and data_five == '+998.88K'
        self.waits()


