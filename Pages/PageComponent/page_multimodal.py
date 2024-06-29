"""
@Author: Zeng Ge
@Date: 2024/3/11 19:40
@FileName: page_multimodal.py
"""
from Conf.config import Config
from Pages.Base import BasePage
import allure
from Utils.tools import *


class MultilingualPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.log = Msg('test_multimodal_page')

    @allure.step("打开多语言英文页面")
    def open_url_(self, hl):
        url = 'https://ca.pre.webullbroker.com/ko-builder/1705303533263-8ac135/732a8a?hl=' + hl
        self.open_url(url)

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

    @allure.step('多语言文本')
    def multilingual_text(self, hl):
        # 获取数组增强元素
        element_text = self.wait_for_selector_('//*[@id="74cf2b_732a8a"]/span')
        # 获取内容
        text = element_text.inner_text()
        self.log.info(f'{hl}文本内容:{text}')
        if hl == 'en':
            assert text == '英文-多语言测试'
        if hl == 'fr':
            assert text == '法语-多语言测试'

    @allure.step('多语言页面标题')
    def multilingual_title(self, hl):
        # 获取数组增强元素
        page_title = self.page.title()
        self.log.info(f'{hl}页面标题内容:{page_title}')
        if hl == 'en':
            assert page_title == '英文页面多语言'
        if hl == 'fr':
            assert page_title == '法语页面多语言'

    @allure.step('按钮名称多语言')
    def multilingual_btn_spn(self, hl):
        # 获取复制当前内容按钮的按钮名称
        element_btn_copy_current_span = self.wait_for_selector_('//*[@id="0d9272_732a8a"]/span')
        text_btn_copy_current_span = element_btn_copy_current_span.inner_text()
        self.log.info(f'{hl}复制当前内容按钮内容:{text_btn_copy_current_span}')
        if hl == 'en':
            assert text_btn_copy_current_span == '英文复制-当前内容'
        if hl == 'fr':
            assert text_btn_copy_current_span == '法语复制-当前内容'

        # 获取复制自定义内容按钮的按钮名称
        element_btn_copy_custom_span = self.wait_for_selector_('//*[@id="d07ea3_732a8a"]/span')
        text_btn_copy_custom_span = element_btn_copy_custom_span.inner_text()
        self.log.info(f'{hl}复制自定义内容按钮的内容:{text_btn_copy_custom_span}')
        if hl == 'en':
            assert text_btn_copy_custom_span == '英文复制-自定义'
        if hl == 'fr':
            assert text_btn_copy_custom_span == '法语复制-自定义'

        # 获取复制当前内容按钮的按钮名称
        element_btn_copy_link_span = self.wait_for_selector_('//*[@id="240b27_732a8a"]/span')
        text_btn_copy_link_span = element_btn_copy_link_span.inner_text()
        self.log.info(f'{hl}复制当前内容按钮的内容:{text_btn_copy_link_span}')
        if hl == 'en':
            assert text_btn_copy_link_span == '英文复制-分享链接'
        if hl == 'fr':
            assert text_btn_copy_link_span == '法语复制-分享链接'

        # 获取提示按钮名称
        element_btn_tip_span = self.wait_for_selector_('//*[@id="8dc10b_732a8a"]/span')
        text_btn_tip_span = element_btn_tip_span.inner_text()
        self.log.info(f'{hl}提示按钮的内容:{text_btn_tip_span}')
        self.waits()
        if hl == 'en':
            assert text_btn_tip_span == '提示多语言-英文'
        if hl == 'fr':
            assert text_btn_tip_span == '提示多语言-法语'

    @allure.step('按钮复制当前内容多语言')
    def multilingual_btn_copy_current_click(self, hl):
        # 获取复制当前内容按钮的按钮名称
        element_btn_copy_current_click = self.wait_for_selector_('//*[@id="0d9272_732a8a"]')
        element_btn_copy_current_click.click()
        # 获取toast提示元素
        element_toast_copy_current = self.wait_for_selector_('//*[@id="ko-layout"]/div/span')
        toast_copy_current = element_toast_copy_current.inner_text()
        self.log.info(f'{hl}按钮复制当前内容toast:{toast_copy_current}')
        self.waits()
        if hl == 'en':
            assert toast_copy_current == '复制英文当前内容'
        if hl == 'fr':
            assert toast_copy_current == '复制法语当前内容'

    @allure.step('按钮自定义复制多语言')
    def multilingual_btn_copy_custom_click(self, hl):
        # 获取复制当前内容按钮的按钮名称
        element_btn_copy_custom_click = self.wait_for_selector_('//*[@id="d07ea3_732a8a"]')
        element_btn_copy_custom_click.click()
        # 获取toast提示元素
        element_toast_copy_custom = self.wait_for_selector_('//*[@id="ko-layout"]/div/span')
        toast_copy_custom = element_toast_copy_custom.inner_text()
        self.log.info(f'{hl}按钮自定义复制内容toast:{toast_copy_custom}')
        self.waits()
        if hl == 'en':
            assert toast_copy_custom == '英文复制自定义'
        if hl == 'fr':
            assert toast_copy_custom == '法语复制自定义'

    @allure.step('按钮复制分享链接多语言')
    def multilingual_btn_copy_link_click(self, hl):
        # 获取复制当前内容按钮的按钮名称
        element_btn_copy_link_click = self.wait_for_selector_('//*[@id="240b27_732a8a"]')
        element_btn_copy_link_click.click()
        # 获取toast提示元素
        element_toast_copy_link = self.wait_for_selector_('//*[@id="ko-layout"]/div/span')
        toast_copy_link = element_toast_copy_link.inner_text()
        self.log.info(f'{hl}按钮复制分享链接内容toast:{toast_copy_link}')
        copied_custom = self.page.evaluate("navigator.clipboard.readText()")
        print(copied_custom)
        self.waits()
        if hl == 'en':
            assert toast_copy_link == '英文复制分享链接'
        if hl == 'fr':
            assert toast_copy_link == '法语复制分享链接'
        return copied_custom

    @allure.step('按钮提示多语言')
    def multilingual_btn_tip_click(self, hl):
        # 获取复制当前内容按钮的按钮名称
        element_btn_tip_click = self.wait_for_selector_('//*[@id="8dc10b_732a8a"]')
        element_btn_tip_click.click()
        # 获取toast提示元素
        element_toast_tip = self.wait_for_selector_('//*[@id="ko-layout"]/div/span')
        toast_tip = element_toast_tip.inner_text()
        self.log.info(f'{hl}按钮提示内容toast:{toast_tip}')
        self.waits()
        if hl == 'en':
            assert toast_tip == '提示多语言英文'
        if hl == 'fr':
            assert toast_tip == '提示多语言法语'

    @allure.step('语言交互-英文')
    def multilingual_btn_en_click(self):
        # 获取复制当前内容按钮的按钮名称
        element_btn_en_click = self.wait_for_selector_('//*[@id="cc4ffd_732a8a"]')
        element_btn_en_click.click()
        self.waits()
        # 获取弹框的文本
        element_tk_text = self.wait_for_selector_('//*[@id="3d2803_732a8a"]/span')
        # 获取弹框的图片
        element_tk_pic = self.wait_for_selector_('//*[@id="4e7619_732a8a"]/img')
        self.waits()
        assert element_tk_text, element_tk_pic is not None
        self.log.info(f'语言为英文时交互校验弹框文本和图片')
        self.wait_for_selector_('//*[@id="7a46b9_732a8a"]/div[3]/img').click()

    @allure.step('语言交互-法语')
    def multilingual_btn_fr_click(self):
        # 获取复制当前内容按钮的按钮名称
        element_btn_fr_click = self.wait_for_selector_('//*[@id="e80498_732a8a"]')
        element_btn_fr_click.click()
        self.waits()
        # 获取弹框的文本
        element_tk_text = self.wait_for_selector_('//*[@id="e9825c_732a8a"]/span')
        # 获取弹框的图片
        element_tk_pic = self.wait_for_selector_('//*[@id="c327f4_732a8a"]/img')
        self.waits()
        assert element_tk_text, element_tk_pic is not None
        self.log.info(f'语言为法语时交互校验弹框文本和图片')
        self.wait_for_selector_('//*[@id="27a8a7_732a8a"]/div[3]/img').click()

    @allure.step('分隔符多语言')
    def multilingual_separate(self, hl):
        # 获取千分位元素
        element_separate_thousand = self.wait_for_selector_('//*[@id="1483d2_732a8a"]/span')
        value_separate_thousand = element_separate_thousand.inner_text()
        self.log.info(f'{hl}千分位值：{value_separate_thousand}')
        # 获取万分位元素
        element_separate_ten_thousand = self.wait_for_selector_('//*[@id="90092c_732a8a"]/span')
        value_separate_ten_thousand = element_separate_ten_thousand.inner_text()
        self.log.info(f'{hl}万分位值：{value_separate_ten_thousand}')
        self.waits()
        if hl == 'en':
            assert value_separate_thousand == '51,236.456711' and value_separate_ten_thousand == '5,1236.456711'
        if hl == 'fr':
            assert value_separate_thousand == '51 236,456711' and value_separate_ten_thousand == '5 1236,456711'

    @allure.step('转义多语言')
    def multilingual_escape(self, hl):
        # 获取字符串转义元素
        element_escape_string = self.wait_for_selector_('//*[@id="e5226d_732a8a"]/span')
        value_escape_string = element_escape_string.inner_text()
        self.log.info(f'{hl}字符串转义：{value_escape_string}')
        # 获取数字转义元素
        element_escape_num = self.wait_for_selector_('//*[@id="336723_732a8a"]/span')
        value_escape_num = element_escape_num.inner_text()
        self.log.info(f'{hl}数字转义：{value_escape_num}')
        # 获取对象转义元素
        element_escape_json = self.wait_for_selector_('//*[@id="a6a46b_732a8a"]/span')
        value_escape_json = element_escape_json.inner_text()
        self.log.info(f'{hl}对象转义：{value_escape_json}')
        # 获取数组转义元素
        element_escape_array = self.wait_for_selector_('//*[@id="406532_732a8a"]/span')
        value_escape_array = element_escape_array.inner_text()
        self.log.info(f'{hl}数组转义：{value_escape_array}')
        self.waits()
        if hl == 'en':
            assert value_escape_string == '英文字符串转义' and value_escape_num == '英文数字转义' and value_escape_json == '英文对象转义' and value_escape_array == '英文数组转义'
        if hl == 'fr':
            assert value_escape_string == '法语字符串转义' and value_escape_num == '法语数字转义' and value_escape_json == '法语对象转义' and value_escape_array == '法语数组转义'

    @allure.step('分享多语言-标题')
    def multilingual_get_share_title(self, hl, url):
        url_ = url + '?hl=' + hl
        self.open_url(url_)
        og_title_content = self.page.evaluate(
            '(property) => document.querySelector(`meta[property="${property}"]`).content', 'og:title')
        self.log.info(f'{hl}分享标题：{og_title_content}')
        if hl == 'en':
            assert og_title_content == '英文分享标题'
        if hl == 'fr':
            assert og_title_content == '法语分享标题'

    @allure.step('分享多语言-描述')
    def multilingual_get_share_description(self, hl, url):
        url_ = url + '?hl=' + hl
        self.open_url(url_)
        og_description_content = self.page.evaluate(
            '(property) => document.querySelector(`meta[property="${property}"]`).content', 'og:description')
        self.log.info(f'{hl}分享描述：{og_description_content}')
        if hl == 'en':
            assert og_description_content == '英文分享描述'
        if hl == 'fr':
            assert og_description_content == '法语分享描述'

    @allure.step('分享多语言-获取twitter图片地址')
    def multilingual_get_twitter_img(self, hl, url):
        url_ = url + '?hl=' + hl
        self.open_url(url_)
        twitter_content = self.page.evaluate('(name) => document.querySelector(`meta[name="${name}"]`).content', 'twitter:image')
        self.log.info(f'{hl}twitter分享图片地址：{twitter_content}')
        if hl == 'en':
            assert twitter_content == 'https://pre-social-video.webullbroker.com/oas/f0719ce7b1544834a701b107b9d4aafc.jpg'
        if hl == 'fr':
            assert twitter_content == 'https://pre-social-video.webullbroker.com/oas/71339d36dabc4a5e88bf3c74aed29350.jpg'

    @allure.step('分享多语言-获取webull图片地址')
    def multilingual_get_webull_img(self, hl, url):
        url_ = url + '?hl=' + hl
        self.open_url(url_)
        webull_content = self.page.evaluate('(name) => document.querySelector(`meta[name="${name}"]`).content',
                                             'webull:image')
        self.log.info(f'{hl}webull分享图片地址：{webull_content}')
        if hl == 'en':
            assert webull_content == 'https://pre-social-video.webullbroker.com/oas/be3e3151099a40388f483cf759cf7b38.jpg'
        if hl == 'fr':
            assert webull_content == 'https://pre-social-video.webullbroker.com/oas/3439a06271bd469583e7256dd6618ff3.png'
