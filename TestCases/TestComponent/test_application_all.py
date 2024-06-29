# Author:曾格
import time

import allure
from Pages.PageComponent.page_picVideo import PicVideoPage
from Pages.PageComponent.page_time_compute import TimeComputePage
from Pages.PageComponent.page_kmb import KMBPage
from Pages.PageComponent.page_lunbotu import LunbotuPage
from Pages.PageComponent.page_copy import CopyPage
from Pages.PageComponent.page_data_format import DataFormatPage
from Pages.PageComponent.page_data_compute import DataComputePage
from Pages.PageComponent.page_multimodal import MultilingualPage
from Utils.Log import Msg


class TestApplicationAll:

    def step(self, msg=''):
        self.log.info(msg)
        return allure.step(msg)

    def test_page_pic_video(self, base_page):
        self.log = Msg('test_pic')
        with self.step("步骤1：打开浏览器访问视频与图片页面"):
            new_page = PicVideoPage(base_page)
            new_page.get_token()
            new_page.open_url_()
            new_page.waits()
        with self.step("步骤1：加载图片与视频页面时显示图片元素"):
            new_page.load_show_pic()
        with self.step('步骤2：点击隐藏按钮隐藏图片'):
            new_page.click_button_hide_pic()
        with self.step('步骤3：点击显示视频按钮显示视频'):
            new_page.click_button_show_video()

    def test_page_time_compute(self, base_page):
        self.log = Msg('test_time_compute')
        with self.step("步骤1：跳到时间计算页面"):
            new_page = TimeComputePage(base_page)
            new_page.get_token()
            new_page.open_url_()
            new_page.waits()
        with self.step('步骤1：显示时间计算所有元素'):
            new_page.load_time_compute()
        with self.step('步骤2：通过按钮点击交互事件判断日期计算是否准确'):
            new_page.click_button_time_compute()

    def test_page_kmb(self, base_page):
        self.log = Msg('test_kmb')
        with self.step("跳转KMB"):
            new_page = KMBPage(base_page)
            new_page.get_token()
            new_page.open_url_()
        with self.step('步骤1：显示KMB所有元素'):
            new_page.load_kmb()

    def test_page_lunbotu(self, base_page):
        self.log = Msg('test_lunbotu')
        with self.step("跳转轮播图"):
            new_page = LunbotuPage(base_page)
            new_page.get_token()
            new_page.open_url_()
        with self.step('步骤1：验证轮播图元素'):
            new_page.load_lunbotu_first()

    def test_page_copy(self, base_page):
        self.log = Msg('test_copy')
        with self.step("跳复制与弹框界面"):
            new_page = CopyPage(base_page)
            new_page.get_token()
            new_page.open_url_()
            new_page.waits()
        with self.step('步骤1：验证复制与弹框页面功能'):
            new_page.load_copy()

    def test_page_data_format(self, base_page):
        self.log = Msg('data_format')
        with self.step('跳数据格式页面'):
            new_page = DataFormatPage(base_page)
            new_page.get_token()
            new_page.open_url_()
            new_page.waits()
        with self.step('步骤1：验证数据格式元素'):
            new_page.load_data_format()

    def test_page_data_compute(self, base_page):
        self.log = Msg('data_compute')
        with self.step('跳数据计算页面'):
            new_page = DataComputePage(base_page)
            new_page.get_token()
            new_page.open_url_()
            new_page.waits()
        with self.step('步骤1：验证数据增强'):
            new_page.load_data_compute_strong()
        with self.step('步骤2：验证数据计算'):
            new_page.load_data_compute()

    def test_page_multilingual_en(self, base_page):
        self.log = Msg('multilingual_text_en')
        with self.step('打开多语言页面英文'):
            new_page = MultilingualPage(base_page)
            new_page.get_token()
            new_page.open_url_('en')
        with self.step('多语言页面校验英文文本'):
            new_page.multilingual_text('en')
        with self.step('校验页面英文标题'):
            new_page.multilingual_title('en')
        with self.step('校验按钮名称多语言-英文'):
            new_page.multilingual_btn_spn('en')
        with self.step('校验复制当前内容按钮toast多语言-英文'):
            new_page.multilingual_btn_copy_current_click('en')
        with self.step('校验自定义复制按钮toast多语言-英文'):
            new_page.multilingual_btn_copy_custom_click('en')
        with self.step('校验复制分享链接toast多语言-英文'):
            share = new_page.multilingual_btn_copy_link_click('en')
        with self.step('校验提示交互toast多语言-英文'):
            new_page.multilingual_btn_tip_click('en')
        with self.step('校验交互为英文的场景-英文'):
            new_page.multilingual_btn_en_click()
        with self.step('校验分隔符场景-英文'):
            new_page.multilingual_separate('en')
        with self.step('校验转义多语言-英文'):
            new_page.multilingual_escape('en')
        with self.step('校验分享多语言-页面标题-英文'):
            new_page.multilingual_get_share_title('en', share)
        with self.step('校验分享多语言-页面描述-英文'):
            new_page.multilingual_get_share_description('en', share)
        with self.step('校验分享多语言-分享twitter图片-英文'):
            new_page.multilingual_get_twitter_img('en', share)
        with self.step('校验分享多语言-分享webull图片-英文'):
            new_page.multilingual_get_webull_img('en', share)

    def test_page_multilingual_fr(self, base_page):
        self.log = Msg('multilingual_text_fr')
        with self.step('打开多语言页面法语'):
            new_page = MultilingualPage(base_page)
            new_page.get_token()
            new_page.open_url_('fr')
        with self.step('多语言页面校验法语文本'):
            new_page.multilingual_text('fr')
        with self.step('校验页面法语标题'):
            new_page.multilingual_title('fr')
        with self.step('校验按钮名称多语言-法语'):
            new_page.multilingual_btn_spn('fr')
        with self.step('校验复制当前内容按钮toast多语言-法语'):
            new_page.multilingual_btn_copy_current_click('fr')
        with self.step('校验自定义复制按钮toast多语言-法语'):
            new_page.multilingual_btn_copy_custom_click('fr')
        with self.step('校验复制分享链接toast多语言-法语'):
            share = new_page.multilingual_btn_copy_link_click('fr')
        with self.step('校验提示交互toast多语言-法语'):
            new_page.multilingual_btn_tip_click('fr')
        with self.step('校验交互为法语的场景'):
            new_page.multilingual_btn_fr_click()
        with self.step('校验分隔符场景-法语'):
            new_page.multilingual_separate('fr')
        with self.step('校验转义多语言-法语'):
            new_page.multilingual_escape('fr')
        with self.step('校验分享多语言-页面标题-法语'):
            new_page.multilingual_get_share_title('fr', share)
        with self.step('校验分享多语言-页面描述-法语'):
            new_page.multilingual_get_share_description('fr', share)
        with self.step('校验分享多语言-分享twitter图片-法语'):
            new_page.multilingual_get_twitter_img('fr', share)
        with self.step('校验分享多语言-分享webull图片-法语'):
            new_page.multilingual_get_webull_img('fr', share)
