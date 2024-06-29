# Author:曾格
from Conf.config import Config
from Pages.Base import BasePage
import allure
import time
from Utils.Log import Msg
from playwright.sync_api import expect
import re
from Utils.tools import *

class LunbotuPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.log = Msg('test_get_KMB_page')

    @allure.step("打开Ko测试页面")
    def open_url_(self):
        self.open_url('https://www.pre.webullbroker.com/ko-builder/1691389061325-d3d8bf/06cbdc')

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

    @allure.step('页面加载后开始验证第一个轮播图')
    def load_lunbotu_first(self):
        """
        :param base_page:
        :return:
        """
        self.waits()
        #第一个轮播图：非自动播放，第一张图
        element_first_lunbotu_firstpic = self.wait_for_selector_('//*[@id="d73097_06cbdc"]/img')
        self.log.info('获取第一个轮播图的第一张图片元素')
        # 断言获取第一个轮播图的第一张图片
        assert element_first_lunbotu_firstpic is not None and element_first_lunbotu_firstpic.is_visible()
        self.log.info('获取第一个轮播图的第一张图片对应指示器节点元素')
        element_first_lunbotu_firstpoint = self.wait_for_selector_('//*[@id="982ea2_06cbdc"]/div/div/div[4]/div[1]')
        self.log.info('获取第一个轮播图的第一张图片对应指示器节点元素的rgb')
        color_first_lunbotu_firstpoint = self.get_color('//*[@id="982ea2_06cbdc"]/div/div/div[4]/div[1]')
        assert element_first_lunbotu_firstpoint is not None and color_first_lunbotu_firstpoint == 'rgb(49, 49, 49)'
        self.log.info('断言第一个轮播图的第一张图片以及第一个指示器节点变亮')
        self.wait_for_selector_('//*[@id="982ea2_06cbdc"]/div/div/div[3]').click()
        self.log.info('点击切换到下一张轮播图')

        # 第一个轮播图：非自动播放，第二张图
        self.waits()
        element_first_lunbotu_secondpic = self.wait_for_selector_('//*[@id="e11307_06cbdc"]/img')
        self.log.info('获取第一个轮播图的第二张图片元素')
        # 断言获取第一个轮播图的第二张图片
        assert element_first_lunbotu_secondpic is not None and element_first_lunbotu_secondpic.is_visible()
        self.log.info('获取第一个轮播图的第二张图片对应指示器节点元素')
        element_first_lunbotu_secondpoint = self.wait_for_selector_('//*[@id="982ea2_06cbdc"]/div/div/div[4]/div[2]')
        self.log.info('获取第一个轮播图的第二张图片对应指示器节点元素的rgb')
        color_first_lunbotu_secondpoint = self.get_color('//*[@id="982ea2_06cbdc"]/div/div/div[4]/div[2]')
        assert element_first_lunbotu_secondpoint is not None and color_first_lunbotu_secondpoint == 'rgb(49, 49, 49)'
        self.log.info('断言第一个轮播图的第二张图片以及第二个指示器节点变亮')
        self.wait_for_selector_('//*[@id="982ea2_06cbdc"]/div/div/div[3]').click()
        self.log.info('点击切换到下一张轮播图')

        # 第一个轮播图：非自动播放，第三张图
        self.waits()
        element_first_lunbotu_thirdpic = self.wait_for_selector_('//*[@id="08045e_06cbdc"]/img')
        self.log.info('获取第一个轮播图的第三张图片元素')
        # 断言获取第一个轮播图的第三张图片
        assert element_first_lunbotu_thirdpic is not None and element_first_lunbotu_thirdpic.is_visible()
        self.log.info('获取第一个轮播图的第三张图片对应指示器节点元素')
        element_first_lunbotu_thirdpoint = self.wait_for_selector_('//*[@id="982ea2_06cbdc"]/div/div/div[4]/div[3]')
        self.log.info('获取第一个轮播图的第三张图片对应指示器节点元素的rgb')
        color_first_lunbotu_thirdpoint = self.get_color('//*[@id="982ea2_06cbdc"]/div/div/div[4]/div[3]')
        assert element_first_lunbotu_thirdpoint is not None and color_first_lunbotu_thirdpoint == 'rgb(49, 49, 49)'
        self.log.info('断言第一个轮播图的第三张图片以及第三个指示器节点变亮')
        self.wait_for_selector_('//*[@id="982ea2_06cbdc"]/div/div/div[3]').click()
        self.log.info('点击切换到下一张轮播图')

        # 第一个轮播图：非自动播放，第四张图
        self.waits()
        element_first_lunbotu_fourthpic = self.wait_for_selector_('//*[@id="0f9e74_06cbdc"]/img')
        self.log.info('获取第一个轮播图的第四张图片元素')
        # 断言获取第一个轮播图的第四张图片
        assert element_first_lunbotu_fourthpic is not None and element_first_lunbotu_fourthpic.is_visible()
        self.log.info('获取第一个轮播图的第四张图片对应指示器节点元素')
        element_first_lunbotu_fourthpoint = self.wait_for_selector_('//*[@id="982ea2_06cbdc"]/div/div/div[4]/div[4]')
        self.log.info('获取第一个轮播图的第四张图片对应指示器节点元素的rgb')
        color_first_lunbotu_fourthpoint = self.get_color('//*[@id="982ea2_06cbdc"]/div/div/div[4]/div[4]')
        assert element_first_lunbotu_fourthpoint is not None and color_first_lunbotu_fourthpoint == 'rgb(49, 49, 49)'
        self.log.info('断言第一个轮播图的第二张图片以及第四个指示器节点变亮')
        self.wait_for_selector_('//*[@id="982ea2_06cbdc"]/div/div/div[3]').click()
        self.log.info('点击切换到下一张轮播图')

        self.waits()
        # 第一个轮播图：非自动播放，第一张图
        element_first_lunbotu_firstpic = self.wait_for_selector_('//*[@id="d73097_06cbdc"]/img')
        self.log.info('获取第一个轮播图的第一张图片元素')
        # 断言获取第一个轮播图的第一张图片
        assert element_first_lunbotu_firstpic is not None and element_first_lunbotu_firstpic.is_visible()
        self.log.info('获取第一个轮播图的第一张图片对应指示器节点元素')
        element_first_lunbotu_firstpoint = self.wait_for_selector_('//*[@id="982ea2_06cbdc"]/div/div/div[4]/div[1]')
        self.log.info('获取第一个轮播图的第一张图片对应指示器节点元素的rgb')
        color_first_lunbotu_firstpoint = self.get_color('//*[@id="982ea2_06cbdc"]/div/div/div[4]/div[1]')
        assert element_first_lunbotu_firstpoint is not None and color_first_lunbotu_firstpoint == 'rgb(49, 49, 49)'
        self.log.info('断言第一个轮播图的第一张图片以及第一个指示器节点变亮')
        self.waits()
