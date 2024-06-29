"""
@Author: Zeng Ge
@Date: 2024/3/8 17:12
@FileName: page_data_compute.py
"""
from Conf.config import Config
from Pages.Base import BasePage
import allure
from Utils.tools import *


class DataComputePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.log = Msg('test_data_compute_page')

    @allure.step("打开数据计算页面")
    def open_url_(self):
        self.open_url('https://ca.pre.webullbroker.com/zh/ko-builder/1705303533263-8ac135/d0378c')

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
            'url': 'https://ca.pre.webullbroker.com/'
        }])

    def get_compute_result(self):
        # 获取邀请总数元素
        element_invite_num = self.wait_for_selector_('//*[@id="2580a6_d0378c"]/span')
        value_invite_num = element_invite_num.inner_text()
        self.log.info(f'邀请人总数:{value_invite_num}')
        # self.waits()
        if value_invite_num:
            add = int(value_invite_num) + 3.5
            self.log.info(f'加法计算值:{add}')
            subtract = int(value_invite_num) - 6.66
            self.log.info(f'减法计算值:{subtract}')
            multiply = add * subtract
            self.log.info(f'乘法计算值:{multiply}')
            divide = int(value_invite_num) / 5
            divide_result = ''
            if isinstance(divide, float):
                if divide.is_integer():
                    divide_result = int(divide)
                else:
                    divide_result = divide
                self.log.info(f'除法计算值:{divide_result}')
            return add, subtract, multiply, divide_result
        else:
            self.log.info(f'邀请总数获取失败:{value_invite_num}')

    @allure.step('数据增强操作')
    def load_data_compute_strong(self):
        # 获取数组增强元素
        element_arrry_strong = self.wait_for_selector_('//*[@id="93995e_d0378c"]/span')
        # 获取内容
        value_arrry_strong = element_arrry_strong.inner_text()
        self.log.info(f'数组增强文本的值:{value_arrry_strong}')
        assert value_arrry_strong == '2'

        # 获取对象增强元素
        element_json_strong = self.wait_for_selector_('//*[@id="351c1b_d0378c"]/span')
        # 获取内容
        value_json_strong  = element_json_strong.inner_text()
        self.log.info(f'数组增强文本的值:{value_json_strong }')
        assert value_json_strong == '0'

    @allure.step('数据计算操作')
    def load_data_compute(self):
        compute_result = self.get_compute_result()

        # 获取加法元素
        element_add = self.wait_for_selector_('//*[@id="2fe4c9_d0378c"]/span')
        # 获取内容
        value_add = element_add.inner_text()
        self.log.info(f'加法文本的值:{value_add}')
        add = compute_result[0]
        assert value_add == str(add)

        # 获取减法元素
        element_subtract = self.wait_for_selector_('//*[@id="e5b594_d0378c"]/span')
        # 获取内容
        value_subtract = element_subtract.inner_text()
        self.log.info(f'减法文本的值:{value_subtract}')
        subtract = compute_result[1]
        assert value_subtract == str(subtract)

        # 获取乘法元素
        element_multiply = self.wait_for_selector_('//*[@id="b0115f_d0378c"]/span')
        # 获取内容
        value_multiply = element_multiply.inner_text()
        self.log.info(f'乘法文本的值:{value_multiply}')
        multiply = compute_result[2]
        assert value_multiply == str(multiply)

        # 获取除法元素
        element_divide = self.wait_for_selector_('//*[@id="9036ae_d0378c"]/span')
        # 获取内容
        value_divide = element_divide.inner_text()
        self.log.info(f'除法文本的值:{value_divide}')
        self.waits()
        divide = compute_result[3]
        assert value_divide == str(divide)
