# encoding=utf-8

from Pages.Base import BasePage
import allure
from Utils import tools
import time
from Utils.tools import get_base, tokens
from Conf.config import Config


class GWPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @allure.step("去登录")
    def login_user(self, name, password):
        time.sleep(2)
        self.page.get_by_text("Email Login").click()
        self.page.locator("input[type=\"text\"]").fill(name)
        self.page.locator("input[type=\"password\"]").fill(password)
        self.page.get_by_role("button", name="Log In").click()
        time.sleep(2)
        bg = '//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div[5]/div[2]/div/div[1]/img[2]'
        hk = '//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div[5]/div[2]/div/div[1]/img[1]'
        button = '//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div[5]/div[2]/div/div[2]/div[2]'
        self.slider_validation(bg, hk, button)
        time.sleep(2)
        error = self.page.query_selector('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div[5]/div[2]/div')
        while error is not None:
            self.slider_validation(bg, hk, button)
            time.sleep(2)
            error = self.page.query_selector('//*[@id="app"]/div/div[2]/div[2]/div/div/div[5]/div[5]/div[2]/div')
        time.sleep(2)
        tk = self.page.query_selector('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div')
        bg2 = '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div/div[1]/img[2]'
        hk2 = '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div/div[1]/img[1]'
        button2 = '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[2]'
        if tk is None:
            print("没有二次图形验证码")
        else:
            self.slider_validation(bg2, hk2, button2)
        time.sleep(2)
        error1 = self.page.query_selector(
            '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div')
        while error1 is not None:
            self.slider_validation(bg2, hk2, button2)
            error1 = self.page.query_selector('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div')
        here = self.page.query_selector('//*[@id="app"]/div/div[2]/div[2]/div/div/div/div/div[2]/div/p/span')
        if here is None:
            print("没有安全问题")
        else:
            self.page.get_by_text("here").click()
            self.page.get_by_role("textbox").click()
            self.page.get_by_role("textbox").fill("1")
            time.sleep(2)
            self.page.get_by_role("button", name="Log In").click()
        self.waits()
        url1 = self.page.url
        self.page.close()
        return url1

    @allure.step("点击登录")
    def gw_dl(self, button, name, password):
        with self.page.expect_popup() as page1_info:
            self.page.get_by_text(button).click()
        page1 = page1_info.value
        time.sleep(2)
        url = page1.url
        page2 = GWPage(page1)
        url1 = page2.login_user(name, password)
        return url, url1

    @allure.step("获取token并且注入浏览器")
    def get_token(self):
        token = tokens(environment=Config.environment, area=Config.area, user=Config.pre_webull_user_23,
                       pwd=Config.pre_webull_pwd_23)
        self.page.context.add_cookies([{
            'name': 'web_lt_pre',
            'value': f'{token}',
            'url': 'https://www.pre.webullbroker.com'
        }])

    @allure.step("去官网注册")
    def gw_zc(self):
        with self.page.expect_popup() as page2_info:
            self.page.get_by_text("点击跳官网注册").click()
        page2 = page2_info.value
        phone = tools.random_phone_("us")
        time.sleep(2)
        url1 = page2.url
        page2.locator("span").filter(has_text="+1").get_by_role("textbox").click()
        page2.locator("span").filter(has_text="+1").get_by_role("textbox").fill(phone.split('-')[1])
        page2.get_by_label("").check()
        page2.get_by_text("Send code").click()
        # msg = tools.get_base("pre", "us")
        # self.waits()
        # tk = page2.query_selector(
        #     '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/div[2]/div')
        # p2 = BasePage(page2)
        # if tk is None:
        #     print("没有图形验证码")
        # else:
        #     bg = '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div[1]/img[2]'
        #     hk = '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div[1]/img[1]'
        #     button = '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div[2]/div[2]'
        #
        #     p2.slider_validation(bg, hk, button)
        #
        # time.sleep(2)
        # error1 = page2.query_selector(
        #     '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/div[2]/div')
        # while error1 is not None:
        #     bg = '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div[1]/img[2]'
        #     hk = '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div[1]/img[1]'
        #     button = '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div[2]/div[2]'
        #     p2.slider_validation(bg, hk, button)
        #     time.sleep(2)
        #     error1 = page2.query_selector(
        #         '//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/div[2]/div')
        #
        # self.waits()
        # code = tools.get_redis_code_(phone, 1, 1, msg)
        # if code is None:
        #     code = '888888'
        page2.locator("input[type=\"text\"]").fill('888888')
        page2.get_by_role("button", name="Next").click()
        time.sleep(2)
        page2.get_by_role("textbox").first.click()
        page2.get_by_role("textbox").first.fill("Aa123456")
        page2.get_by_role("textbox").nth(1).click()
        page2.get_by_role("textbox").nth(1).fill("Aa123456")
        page2.get_by_role("button", name="Sign Up").click()
        self.waits()
        url2 = page2.url
        page2.close()
        return url1, url2

    @allure.step('官网跳转')
    def gw_center(self, button):
        with self.page.expect_popup() as page1_info:
            self.page.get_by_text(button).click()
        page1 = page1_info.value
        time.sleep(2)
        page1.get_by_text("Email Login").click()
        page1.locator("input[type=\"text\"]").click()
        page1.locator("input[type=\"text\"]").fill("zengge_23@163.com")
        page1.locator("input[type=\"password\"]").click()
        page1.locator("input[type=\"password\"]").fill("auto1234")
        page1.get_by_role("button", name="Log In").click()
        bg = '//*[@id="app"]/div/div[2]/div/div/div[5]/div[5]/div[2]/div/div[1]/img[2]'
        hk = '//*[@id="app"]/div/div[2]/div/div/div[5]/div[5]/div[2]/div/div[1]/img[1]'
        button = '//*[@id="app"]/div/div[2]/div/div/div[5]/div[5]/div[2]/div/div[2]/div[2]'
        a = BasePage(page1)
        a.slider_validation(bg, hk, button)
        time.sleep(2)
        error = page1.query_selector('//*[@id="app"]/div/div[2]/div/div/div[5]/div[5]/div[2]/div/div[1]/img[2]')
        while error is not None:
            a.slider_validation(bg, hk, button)
            error = page1.query_selector('//*[@id="app"]/div/div[2]/div/div/div[5]/div[5]/div[2]/div/div[3]/p')
        time.sleep(2)
        tk = page1.query_selector('//*[@id="app"]/div/div[2]/div/div/div/div/div[3]/div[2]/div')

        if tk is None:
            print("没有二次图形验证码")
        else:
            bg2 = '//*[@id="app"]/div/div[2]/div/div/div/div/div[3]/div[2]/div/div[1]/img[2]'
            hk2 = '//*[@id="app"]/div/div[2]/div/div/div/div/div[3]/div[2]/div/div[1]/img[1]'
            button2 = '//*[@id="app"]/div/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[2]'
            a.slider_validation(bg2, hk2, button2)
        time.sleep(3)
        error1 = page1.query_selector('//*[@id="app"]/div/div[2]/div/div/div/div/div[3]/div[2]/div/div[1]/img[2]')
        while error1 is not None:
            bg2 = '//*[@id="app"]/div/div[2]/div/div/div/div/div[3]/div[2]/div/div[1]/img[2]'
            hk2 = '//*[@id="app"]/div/div[2]/div/div/div/div/div[3]/div[2]/div/div[1]/img[1]'
            button2 = '//*[@id="app"]/div/div[2]/div/div/div/div/div[3]/div[2]/div/div[2]/div[2]'
            a.slider_validation(bg2, hk2, button2)
            error1 = page1.query_selector('//*[@id="app"]/div/div[2]/div/div/div[5]/div[5]/div[2]/div/div[3]/p')

        here = page1.query_selector('//*[@id="app"]/div/div[2]/div/div/div/div/div[2]/div/p/span')

        if here is None:
            print("没有安全问题")
        else:
            page1.get_by_text("here").click()
            page1.get_by_role("textbox").click()
            page1.get_by_role("textbox").fill("1")
            page1.get_by_role("button", name="Log In").click()
        time.sleep(2)
        url = page1.url
        return url

    @allure.step('点击按钮生成新页面')
    def gw_get_page(self, button):
        with self.page.expect_popup() as page1_info:
            self.page.get_by_text(button).click()
        page1 = page1_info.value
        return page1
