import json

from Pages.Base import BasePage
from Utils.tools import get_base, tokens
from Conf.config import Config
import allure
import time


class ButtonPage(BasePage):
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
            time.sleep(2)
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

    @allure.step("获取token并且注入浏览器")
    def get_token(self):
        token = tokens(environment=Config.environment, area=Config.area, user=Config.pre_webull_user_23,
                       pwd=Config.pre_webull_pwd_23)
        self.page.context.add_cookies([{
            'name': 'web_lt_pre',
            'value': f'{token}',
            'url': 'https://www.pre.webullbroker.com'
        }])

    @allure.step('打开url')
    def openurl(self):
        self.open_url('https://www.pre.webullbroker.com/ko-builder/auto')

    @allure.step('点击按钮隐藏图片')
    def click(self):
        self.click_button("隐藏图片")

    def selectelement(self):
        jpg = self.select_element('//*[@id="513675_f802d5"]/img')
        return jpg

    @allure.step('获取页面时间')
    def select_time(self):
        page_time = self.get_text('//*[@id="049401_f802d5"]/span')
        return page_time

    @allure.step('点击按钮生成新页面')
    def get_page(self, button):
        with self.page.expect_popup() as page1_info:
            self.page.get_by_text(button).click()
        page1 = page1_info.value
        return page1

    @allure.step('将百分比字符串转化成数字')
    def get_float(self, text):
        percentage_str = text  # 你的百分比字符串
        percentage_str_without_percent = percentage_str.replace('%', '')  # 去掉百分比符号
        percentage_as_float = float(percentage_str_without_percent) / 100  # 转化为浮点数并除以 100 得到小数表示
        return percentage_as_float

    @allure.step('获取指定接口返回参数')
    def listening_response(self, captured_response,
                           url='https://usact.pre-sign.webullbroker.com/api/oas/koLable/labelValues'):
        def record_response(response):
            if url is not None:
                response_url = response.url
                if url in response_url:
                    # 获取响应的文本数据
                    body = response.text()
                    # 提取 newsUrl 字段
                    data = json.loads(body)
                    getActSystemTime = [item['getActSystemTime'] for item in data['data']]
                    for item in getActSystemTime:
                        captured_response.append(item)
            else:
                # 获取响应的文本数据
                body = response.text()
                # 提取 newsUrl 字段
                data = json.loads(body)
                getActSystemTime1 = [item['getActSystemTime'] for item in data['data']]
                for item in getActSystemTime1:
                    captured_response.append(item)

        self.page.on("response", record_response)
        return captured_response
