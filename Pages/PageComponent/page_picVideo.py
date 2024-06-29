# Author:曾格
from Conf.config import Config
from Pages.Base import BasePage
import allure
import time
from Utils.Log import Msg
from playwright.sync_api import expect
import re
from Utils.tools import *

class PicVideoPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.log = Msg('test_get_picvideo_page')

    @allure.step("打开Ko测试页面")
    def open_url_(self):
        self.open_url('https://www.pre.webullbroker.com/ko-builder/1691389061325-d3d8bf/2821ee')

    @allure.step("获取token并且注入浏览器")
    def get_token(self):
        token = tokens(environment=Config.environment, area=Config.area, user=Config.pre_webull_user_21,
                       pwd=Config.pre_webull_pwd_21)
        self.page.context.add_cookies([{
            'name': 'web_lt_pre',
            'value': f'{token}',
            'url': 'https://www.pre.webullbroker.com'
        }])

    @allure.step('页面加载执行交互事件后显示图片')
    def load_show_pic(self):
        """
        :param base_page:
        :return:
        """
        # 获取本地图片
        element_pic_local = self.wait_for_selector_('//*[@id="ba1b0a_2821ee"]/img')
        self.log.info('加载页面时通过加载事件显示本地图片')
        # 断言本地图片元素存在且本地图片可见
        assert element_pic_local is not None and element_pic_local.is_visible()
        # 获取素材库图片
        element_pic_sucai = self.wait_for_selector_('//*[@id="c10b6d_2821ee"]/img')
        self.log.info('加载页面时通过加载事件素材库图片')
        # 断言素材库图片元素存在且素材库图片可见
        assert element_pic_sucai is not None and element_pic_local.is_visible()
        # 获取接口返回的图片
        element_pic_link = self.wait_for_selector_('//*[@id="576b9b_2821ee"]/img')
        self.log.info('加载页面时通过加载事件链接图片')
        # 断言接口返回的图片元素存在且链接图片可见
        assert element_pic_link is not None and element_pic_local.is_visible()

    def click_button_hide_pic(self):
        """

        :return:
        """
        # 获取【点击隐藏本地图片】按钮元素
        element_btn_local = self.wait_for_selector_('//*[@id="97d86c_2821ee"]/span')
        # 点击【点击隐藏本地图片】按钮元素
        element_btn_local.click()
        self.waits()
        pic_local = self.select_element('//*[@id="ba1b0a_2821ee"]/img')
        self.log.info('点击按钮隐藏本地图片')
        assert pic_local is None

        # 获取【点击隐藏素材库图片】按钮元素
        element_btn_sucaiku = self.wait_for_selector_('//*[@id="9695fc_2821ee"]/span')
        element_btn_sucaiku.click()
        self.waits()
        pic_sucaiku = self.select_element('//*[@id="c10b6d_2821ee"]/img')
        self.log.info('点击按钮隐藏素材库图片')
        assert pic_sucaiku is None

        # 获取【点击隐藏链接图片】按钮元素
        element_btn_link = self.wait_for_selector_('//*[@id="0b6020_2821ee"]/span')
        element_btn_link.click()
        self.waits()
        pic_link = self.select_element('//*[@id="576b9b_2821ee"]/img')
        self.log.info('点击按钮隐藏链接图片')
        assert pic_link is None

    def click_button_show_video(self):
        """

        :return:
        """
        #点击显示非透明视频
        element_btn_transparent = self.wait_for_selector_('//*[@id="d46bb3_2821ee"]/span')
        element_btn_transparent.click()
        self.log.info('按钮点击事件显示非透明视频')
        element_video_transparent = self.wait_for_selector_('//*[@id="b74b09_2821ee"]/video')
        assert element_video_transparent is not None and element_video_transparent.is_visible()
        self.waits()
        # 点击显示透明视频
        element_btn_nottransparent = self.wait_for_selector_('//*[@id="0df46b_2821ee"]/span')
        element_btn_nottransparent.click()
        self.log.info('按钮点击事件显示透明视频')
        element_video_nottransparent = self.wait_for_selector_('//*[@id="canvas"]')
        assert element_video_nottransparent is not None and element_video_nottransparent.is_visible()
        self.waits()
