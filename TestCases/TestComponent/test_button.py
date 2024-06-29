# encoding=utf-8
import time
import allure
from Pages.PageComponent.page_button import ButtonPage
from Utils.Log import Msg


class TestButton:

    def step(self, msg=''):
        self.log.info(msg)
        return allure.step(msg)
    def test_button(self, base_page):
        self.log = Msg('test_button')
        with self.step("步骤一：打开浏览器访问固定链接"):
            new_page = ButtonPage(base_page)
            new_page.get_token()
            new_page.openurl()
        with self.step("步骤二：预先登录"):
            assert new_page.page.url == "https://www.pre.webullbroker.com/ko-builder/auto"

    # def test_time(self, base_page):
    #     self.log = Msg('test_button')
    #     new_page = ButtonPage(base_page)
    #     with self.step('页面时间与接口返回时间对比'):
    #         page_time = new_page.select_time()
    #         time_1 = []
    #         time_1 = new_page.listening_response(time_1)
    #         assert time_1[0] == page_time
    def test_hide(self, base_page):
        self.log = Msg('test_hide')
        new_page = ButtonPage(base_page)
        with self.step("隐藏图片交互"):
            new_page.click()
            jpg = new_page.selectelement()
            assert jpg is None
    def test_show(self, base_page):
        self.log = Msg('test_show')
        new_page = ButtonPage(base_page)
        with self.step("显示图片交互"):
            time.sleep(2)
            new_page.click_button("显示图片")
            jpg1 = new_page.select_element('//*[@id="513675_f802d5"]/img')
            assert jpg1 is not None

    def test_change_style(self, base_page):
        self.log = Msg('test_change_style')
        new_page = ButtonPage(base_page)
        with self.step("更改样式交互"):
            time.sleep(2)
            new_page.click_button("更改样式")
            color = new_page.get_background_color('//*[@id="edcc23_f802d5"]')
            assert color == 'rgb(254, 225, 95)'

    def test_refresh(self, base_page):
        self.log = Msg('test_refresh')
        new_page = ButtonPage(base_page)
        with self.step("刷新组件交互"):
            text_1 = new_page.get_text('//*[@id="049401_f802d5"]/span')
            time.sleep(2)
            new_page.click_button('刷新组件')
            time.sleep(2)
            text_2 = new_page.get_text('//*[@id="049401_f802d5"]/span')
            assert text_1 != text_2

    def test_refresh_variables(self, base_page):
        self.log = Msg('test_refresh_variables')
        new_page = ButtonPage(base_page)
        with self.step("刷新变量交互"):
            text_2 = new_page.get_text('//*[@id="049401_f802d5"]/span')
            time.sleep(2)
            new_page.click_button('刷新变量')
            time.sleep(2)
            text_3 = new_page.get_text('//*[@id="049401_f802d5"]/span')
            assert text_3 != text_2

    def test_change_data(self, base_page):
        self.log = Msg('test_change_data')
        new_page = ButtonPage(base_page)
        with self.step("修改数据交互"):
            time.sleep(2)
            new_page.click_button('修改时间')
            time.sleep(2)
            text_4 = new_page.get_text('//*[@id="049401_f802d5"]/span')
            assert text_4 == '1'

    def test_list(self, base_page):
        self.log = Msg('test_list')
        new_page = ButtonPage(base_page)
        with self.step("步骤一：跳内部列表页面"):
            page = new_page.get_page('跳内部页面')
            time.sleep(2)
            assert '314f7a' in page.url
            global new_page1
            new_page1 = ButtonPage(page)

    def test_list_1(self):
        self.log = Msg('test_list_1')
        with self.step("步骤一：点击展示更多列表项"):
            new_page1.click_button('View more↓')
            text_5 = new_page1.get_text('//*[@id="6884e0_314f7a_0"]/span')
            color_5 = new_page1.get_color('//*[@id="6884e0_314f7a_0"]/span')
            number_5 = new_page1.get_float(text_5)
        with self.step("步骤二：断言列表项颜色"):
            if number_5 < 0:
                assert color_5 == 'rgb(242, 79, 91)'
            elif number_5 > 0:
                assert color_5 == 'rgb(38, 181, 138)'

            time.sleep(2)
            text_6 = new_page1.get_text('//*[@id="6884e0_314f7a_1"]/span')
            color_6 = new_page1.get_color('//*[@id="6884e0_314f7a_1"]/span')
            number_6 = new_page1.get_float(text_6)
            if number_6 < 0:
                assert color_6 == 'rgb(242, 79, 91)'
            elif number_6 > 0:
                assert color_6 == 'rgb(38, 181, 138)'

            time.sleep(2)
            text_7 = new_page1.get_text('//*[@id="6884e0_314f7a_2"]/span')
            color_7 = new_page1.get_color('//*[@id="6884e0_314f7a_2"]/span')
            number_7 = new_page1.get_float(text_7)
            if number_7 < 0:
                assert color_7 == 'rgb(242, 79, 91)'
            elif number_7 > 0:
                assert color_7 == 'rgb(38, 181, 138)'

            time.sleep(2)
            text_8 = new_page1.get_text('//*[@id="6884e0_314f7a_3"]/span')
            color_8 = new_page1.get_color('//*[@id="6884e0_314f7a_3"]/span')
            number_8 = new_page1.get_float(text_8)
            if number_8 < 0:
                assert color_8 == 'rgb(242, 79, 91)'
            elif number_8 > 0:
                assert color_8 == 'rgb(38, 181, 138)'

            time.sleep(2)
            text_9 = new_page1.get_text('//*[@id="6884e0_314f7a_4"]/span')
            color_9 = new_page1.get_color('//*[@id="6884e0_314f7a_4"]/span')
            number_9 = new_page1.get_float(text_9)
            if number_9 < 0:
                assert color_9 == 'rgb(242, 79, 91)'
            elif number_9 > 0:
                assert color_9 == 'rgb(38, 181, 138)'

    def test_list_2(self):
        self.log = Msg('test_list_3')
        with self.step("步骤一：切换至'Short'列表数据"):
            new_page1.page.get_by_text("Short", exact=True).click()
            # text_5 = None
            # text_6 = None
            # text_7 = None
            # text_8 = None
            # text_9 = None
            # color_5 = None
            # color_6 = None
            # color_7 = None
            # color_8 = None
            # color_9 = None
            # number_5 = None
            # number_6 = None
            # number_7 = None
            # number_8 = None
            # number_9 = None
            text_5 = new_page1.get_text('//*[@id="6884e0_314f7a_0"]/span')
            color_5 = new_page1.get_color('//*[@id="6884e0_314f7a_0"]/span')
            number_5 = new_page1.get_float(text_5)
        with self.step("步骤二：断言列表项颜色"):
            if number_5 < 0:
                assert color_5 == 'rgb(242, 79, 91)'
            elif number_5 > 0:
                assert color_5 == 'rgb(38, 181, 138)'

            time.sleep(2)
            text_6 = new_page1.get_text('//*[@id="6884e0_314f7a_1"]/span')
            color_6 = new_page1.get_color('//*[@id="6884e0_314f7a_1"]/span')
            number_6 = new_page1.get_float(text_6)
            if number_6 < 0:
                assert color_6 == 'rgb(242, 79, 91)'
            elif number_6 > 0:
                assert color_6 == 'rgb(38, 181, 138)'

            time.sleep(2)
            text_7 = new_page1.get_text('//*[@id="6884e0_314f7a_2"]/span')
            color_7 = new_page1.get_color('//*[@id="6884e0_314f7a_2"]/span')
            number_7 = new_page1.get_float(text_7)
            if number_7 < 0:
                assert color_7 == 'rgb(242, 79, 91)'
            elif number_7 > 0:
                assert color_7 == 'rgb(38, 181, 138)'

            time.sleep(2)
            text_8 = new_page1.get_text('//*[@id="6884e0_314f7a_3"]/span')
            color_8 = new_page1.get_color('//*[@id="6884e0_314f7a_3"]/span')
            number_8 = new_page1.get_float(text_8)
            if number_8 < 0:
                assert color_8 == 'rgb(242, 79, 91)'
            elif number_8 > 0:
                assert color_8 == 'rgb(38, 181, 138)'

            time.sleep(2)
            text_9 = new_page1.get_text('//*[@id="6884e0_314f7a_4"]/span')
            color_9 = new_page1.get_color('//*[@id="6884e0_314f7a_4"]/span')
            number_9 = new_page1.get_float(text_9)
            if number_9 < 0:
                assert color_9 == 'rgb(242, 79, 91)'
            elif number_9 > 0:
                assert color_9 == 'rgb(38, 181, 138)'

    def test_list_3(self):
        self.log = Msg('test_list_3')
        with self.step("步骤一：切换至'Bond'列表数据"):
            new_page1.click_button('Bond')
            # text_5 = None
            # text_6 = None
            # text_7 = None
            # text_8 = None
            # text_9 = None
            # color_5 = None
            # color_6 = None
            # color_7 = None
            # color_8 = None
            # color_9 = None
            # number_5 = None
            # number_6 = None
            # number_7 = None
            # number_8 = None
            # number_9 = None
            text_5 = new_page1.get_text('//*[@id="6884e0_314f7a_0"]/span')
            color_5 = new_page1.get_color('//*[@id="6884e0_314f7a_0"]/span')
            number_5 = new_page1.get_float(text_5)
        with self.step("步骤二：断言列表项颜色"):
            if number_5 < 0:
                assert color_5 == 'rgb(242, 79, 91)'
            elif number_5 > 0:
                assert color_5 == 'rgb(38, 181, 138)'

            time.sleep(2)
            text_6 = new_page1.get_text('//*[@id="6884e0_314f7a_1"]/span')
            color_6 = new_page1.get_color('//*[@id="6884e0_314f7a_1"]/span')
            number_6 = new_page1.get_float(text_6)
            if number_6 < 0:
                assert color_6 == 'rgb(242, 79, 91)'
            elif number_6 > 0:
                assert color_6 == 'rgb(38, 181, 138)'

            time.sleep(2)
            text_7 = new_page1.get_text('//*[@id="6884e0_314f7a_2"]/span')
            color_7 = new_page1.get_color('//*[@id="6884e0_314f7a_2"]/span')
            number_7 = new_page1.get_float(text_7)
            if number_7 < 0:
                assert color_7 == 'rgb(242, 79, 91)'
            elif number_7 > 0:
                assert color_7 == 'rgb(38, 181, 138)'

            time.sleep(2)
            text_8 = new_page1.get_text('//*[@id="6884e0_314f7a_3"]/span')
            color_8 = new_page1.get_color('//*[@id="6884e0_314f7a_3"]/span')
            number_8 = new_page1.get_float(text_8)
            if number_8 < 0:
                assert color_8 == 'rgb(242, 79, 91)'
            elif number_8 > 0:
                assert color_8 == 'rgb(38, 181, 138)'

            time.sleep(2)
            text_9 = new_page1.get_text('//*[@id="6884e0_314f7a_4"]/span')
            color_9 = new_page1.get_color('//*[@id="6884e0_314f7a_4"]/span')
            number_9 = new_page1.get_float(text_9)
            if number_9 < 0:
                assert color_9 == 'rgb(242, 79, 91)'
            elif number_9 > 0:
                assert color_9 == 'rgb(38, 181, 138)'

    def test_list_4(self):
        self.log = Msg('test_list_4')
        with self.step("步骤一：切换至'Commodities'列表数据"):
            new_page1.click_button('Commodities')
            # text_5 = None
            # text_6 = None
            # text_7 = None
            # text_8 = None
            # text_9 = None
            # color_5 = None
            # color_6 = None
            # color_7 = None
            # color_8 = None
            # color_9 = None
            # number_5 = None
            # number_6 = None
            # number_7 = None
            # number_8 = None
            # number_9 = None
            text_5 = new_page1.get_text('//*[@id="6884e0_314f7a_0"]/span')
            color_5 = new_page1.get_color('//*[@id="6884e0_314f7a_0"]/span')
            number_5 = new_page1.get_float(text_5)
        with self.step("步骤二：断言列表项颜色"):
            if number_5 < 0:
                assert color_5 == 'rgb(242, 79, 91)'
            elif number_5 > 0:
                assert color_5 == 'rgb(38, 181, 138)'

            time.sleep(2)
            text_6 = new_page1.get_text('//*[@id="6884e0_314f7a_1"]/span')
            color_6 = new_page1.get_color('//*[@id="6884e0_314f7a_1"]/span')
            number_6 = new_page1.get_float(text_6)
            if number_6 < 0:
                assert color_6 == 'rgb(242, 79, 91)'
            elif number_6 > 0:
                assert color_6 == 'rgb(38, 181, 138)'

            time.sleep(2)
            text_7 = new_page1.get_text('//*[@id="6884e0_314f7a_2"]/span')
            color_7 = new_page1.get_color('//*[@id="6884e0_314f7a_2"]/span')
            number_7 = new_page1.get_float(text_7)
            if number_7 < 0:
                assert color_7 == 'rgb(242, 79, 91)'
            elif number_7 > 0:
                assert color_7 == 'rgb(38, 181, 138)'

            time.sleep(2)
            text_8 = new_page1.get_text('//*[@id="6884e0_314f7a_3"]/span')
            color_8 = new_page1.get_color('//*[@id="6884e0_314f7a_3"]/span')
            number_8 = new_page1.get_float(text_8)
            if number_8 < 0:
                assert color_8 == 'rgb(242, 79, 91)'
            elif number_8 > 0:
                assert color_8 == 'rgb(38, 181, 138)'

            time.sleep(2)
            text_9 = new_page1.get_text('//*[@id="6884e0_314f7a_4"]/span')
            color_9 = new_page1.get_color('//*[@id="6884e0_314f7a_4"]/span')
            number_9 = new_page1.get_float(text_9)
            if number_9 < 0:
                assert color_9 == 'rgb(242, 79, 91)'
            elif number_9 > 0:
                assert color_9 == 'rgb(38, 181, 138)'

    def test_list_5(self):
        self.log = Msg('test_list_5')
        with self.step("步骤一：切换回'Short'列表数据"):
            new_page1.page.get_by_text("Short", exact=True).click()
            # text_5 = None
            # text_6 = None
            # text_7 = None
            # text_8 = None
            # text_9 = None
            # color_5 = None
            # color_6 = None
            # color_7 = None
            # color_8 = None
            # color_9 = None
            # number_5 = None
            # number_6 = None
            # number_7 = None
            # number_8 = None
            # number_9 = None
            text_5 = new_page1.get_text('//*[@id="6884e0_314f7a_0"]/span')
            color_5 = new_page1.get_color('//*[@id="6884e0_314f7a_0"]/span')
            number_5 = new_page1.get_float(text_5)
        with self.step("步骤二：断言列表项颜色"):
            if number_5 < 0:
                assert color_5 == 'rgb(242, 79, 91)'
            elif number_5 > 0:
                assert color_5 == 'rgb(38, 181, 138)'

            time.sleep(2)
            text_6 = new_page1.get_text('//*[@id="6884e0_314f7a_1"]/span')
            color_6 = new_page1.get_color('//*[@id="6884e0_314f7a_1"]/span')
            number_6 = new_page1.get_float(text_6)
            if number_6 < 0:
                assert color_6 == 'rgb(242, 79, 91)'
            elif number_6 > 0:
                assert color_6 == 'rgb(38, 181, 138)'

            time.sleep(2)
            text_7 = new_page1.get_text('//*[@id="6884e0_314f7a_2"]/span')
            color_7 = new_page1.get_color('//*[@id="6884e0_314f7a_2"]/span')
            number_7 = new_page1.get_float(text_7)
            if number_7 < 0:
                assert color_7 == 'rgb(242, 79, 91)'
            elif number_7 > 0:
                assert color_7 == 'rgb(38, 181, 138)'

            time.sleep(2)
            text_8 = new_page1.get_text('//*[@id="6884e0_314f7a_3"]/span')
            color_8 = new_page1.get_color('//*[@id="6884e0_314f7a_3"]/span')
            number_8 = new_page1.get_float(text_8)
            if number_8 < 0:
                assert color_8 == 'rgb(242, 79, 91)'
            elif number_8 > 0:
                assert color_8 == 'rgb(38, 181, 138)'

            time.sleep(2)
            text_9 = new_page1.get_text('//*[@id="6884e0_314f7a_4"]/span')
            color_9 = new_page1.get_color('//*[@id="6884e0_314f7a_4"]/span')
            number_9 = new_page1.get_float(text_9)
            if number_9 < 0:
                assert color_9 == 'rgb(242, 79, 91)'
            elif number_9 > 0:
                assert color_9 == 'rgb(38, 181, 138)'
