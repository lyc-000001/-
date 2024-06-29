# Author:曾格
from Conf.config import Config
from Pages.Base import BasePage
import allure
from Utils.tools import *


class CopyPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.log = Msg('test_get_copy_page')

    @allure.step("打开Ko测试页面")
    def open_url_(self):
        self.open_url('https://www.pre.webullbroker.com/ko-builder/1691389061325-d3d8bf/e5c3d2')

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
    def load_copy(self):
        """
        :param base_page:
        :return:
        """
        # 获取一次性弹框元素
        element_tk_only_one = self.wait_for_selector_('//*[@id="994bcb_e5c3d2"]')
        assert element_tk_only_one is not None
        self.log.info('获取一次性弹框')
        # 关闭一次性弹框
        self.wait_for_selector_('//*[@id="994bcb_e5c3d2"]/div[2]/img').click()
        self.log.info('关闭一次性弹框')

        self.page.reload()
        self.waits()
        # 刷新页面不再弹出一次性弹框
        element_tk_only_one = self.select_element('//*[@id="994bcb_e5c3d2"]')
        assert element_tk_only_one is None
        self.log.info('刷新页面不再弹出一次性弹框')

        # 点击按钮弹出一次性弹框
        self.wait_for_selector_('//*[@id="43f51b_e5c3d2"]/span').click()
        # 获取一次性弹框
        element_tk_only_one = self.wait_for_selector_('//*[@id="994bcb_e5c3d2"]')
        assert element_tk_only_one is not None
        # 点击按钮关闭一次性弹框
        self.wait_for_selector_('//*[@id="994bcb_e5c3d2"]/div[2]/img').click()
        self.log.info('点击按钮关闭一次性弹框')

        # 测试复制邀请链接模块
        self.wait_for_selector_('//*[@id="2421d6_e5c3d2"]/span').click()
        # 获取剪切板内容
        copied_invite_link = self.page.evaluate("navigator.clipboard.readText()")
        self.waits()
        # print(f'获取邀请链接:{copied_invite_link}')
        assert 'https://www.pre.webullbroker.com/s/V4yk6hrXeIJIiLC' in copied_invite_link
        self.log.info(f'获取复制的邀请链接并断言:{copied_invite_link}')

        # 测试复制当前内容模块
        self.wait_for_selector_('//*[@id="4b6e10_e5c3d2"]/span').click()
        # 获取剪切板内容
        copied_current = self.page.evaluate("navigator.clipboard.readText()")
        self.waits()
        assert copied_current == '复制当前内容'
        self.log.info(f'获取复制的当前内容并断言:{copied_current}')

        # 测试自定义复制模块
        self.wait_for_selector_('//*[@id="94e654_e5c3d2"]').click()
        # 获取剪切板内容
        copied_custom = self.page.evaluate("navigator.clipboard.readText()")
        self.waits()
        assert copied_custom == '77777777'
        self.log.info(f'获取复制的自定义内容并断言：{copied_custom}')
        self.waits()
