"""
@Author: Zeng Ge
@Date: 2024/3/8 17:12
@FileName: page_data_format.py
"""
from Conf.config import Config
from Pages.Base import BasePage
import allure
from Utils.tools import *


class DataFormatPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.log = Msg('test_data_format_page')

    @allure.step("打开数据格式页面")
    def open_url_(self):
        self.open_url('https://ca.pre.webullbroker.com/zh/ko-builder/1705303533263-8ac135')

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

    @allure.step('copy页面的操作')
    def load_data_format(self):
        # 获取两位小数补零元素
        element_two_decimal_with_zero = self.wait_for_selector_('//*[@id="61dcdf_d81e23"]/span')
        # 获取内容
        value_two_decimal_with_zero = element_two_decimal_with_zero.inner_text()
        self.log.info(f'两位小数补零的值:{value_two_decimal_with_zero}')
        assert value_two_decimal_with_zero == '121.90'

        # 获取两位小数不补零元素
        element_two_decimal_with_nozero = self.wait_for_selector_('//*[@id="a3be8c_d81e23"]/span')
        # 获取内容
        value_two_decimal_with_nozero = element_two_decimal_with_nozero.inner_text()
        self.log.info(f'两位小数不补零的值:{value_two_decimal_with_nozero}')
        assert value_two_decimal_with_nozero == '121.9'

        # 获取四位小数补零元素
        element_four_decimal_with_zero = self.wait_for_selector_('//*[@id="f69201_d81e23"]/span')
        # 获取内容
        value_four_decimal_with_zero = element_four_decimal_with_zero.inner_text()
        self.log.info(f'四位小数补零的值:{value_four_decimal_with_zero}')
        assert value_four_decimal_with_zero == '121.9000'

        # 获取四位小数不补零元素
        element_four_decimal_with_nozero = self.wait_for_selector_('//*[@id="ae3707_d81e23"]/span')
        # 获取内容
        value_four_decimal_with_nozero = element_four_decimal_with_nozero.inner_text()
        self.log.info(f'四位小数不补零的值:{value_four_decimal_with_nozero}')
        assert value_four_decimal_with_nozero == '121.9'

        # 获取两位小数向上取整元素
        element_two_decimal_up = self.wait_for_selector_('//*[@id="d2c9d8_d81e23"]/span')
        # 获取内容
        value_two_decimal_up = element_two_decimal_up.inner_text()
        self.log.info(f'两位小数向上取整的值:{value_two_decimal_up}')
        assert value_two_decimal_up == '71.52'

        # 获取两位小数向下取整元素
        element_two_decimal_down = self.wait_for_selector_('//*[@id="0416dc_d81e23"]/span')
        # 获取内容
        value_two_decimal_down = element_two_decimal_down.inner_text()
        self.log.info(f'两位小数向下取整的值:{value_two_decimal_down}')
        assert value_two_decimal_down == '71.51'

        # 获取四舍五入进位元素
        element_rounding_up = self.wait_for_selector_('//*[@id="3e19ad_d81e23"]/span')
        # 获取内容
        value_rounding_up = element_rounding_up.inner_text()
        self.log.info(f'四舍五入进位的值:{value_rounding_up}')
        assert value_rounding_up == '71.52'

        # 获取四舍五入退位元素
        element_rounding_down = self.wait_for_selector_('//*[@id="77781d_d81e23"]/span')
        # 获取内容
        value_rounding_down = element_rounding_down.inner_text()
        self.log.info(f'四舍五入退位的值:{value_rounding_down}')
        assert value_rounding_down == '71.51'

        # 获取后缀%元素
        element_suffix_hundred = self.wait_for_selector_('//*[@id="d2bfb3_d81e23"]/span')
        # 获取内容
        value_suffix_hundred = element_suffix_hundred.inner_text()
        self.log.info(f'后缀%的值:{value_suffix_hundred}')
        assert value_suffix_hundred == '+5,123,645.6711%'

        # 获取后缀‰元素
        element_suffix_thousand = self.wait_for_selector_('//*[@id="3a0de1_d81e23"]/span')
        # 获取内容
        value_suffix_thousand = element_suffix_thousand.inner_text()
        self.log.info(f'后缀%的值:{value_suffix_thousand}')
        assert value_suffix_thousand == '-15113.3‰'

        # 获取后缀‱元素
        element_suffix__ten_thousand = self.wait_for_selector_('//*[@id="193990_d81e23"]/span')
        # 获取内容
        value_suffix_ten_thousand = element_suffix__ten_thousand.inner_text()
        self.log.info(f'后缀%的值:{value_suffix_ten_thousand}')
        assert value_suffix_ten_thousand == '+512,364,567.11‱'
