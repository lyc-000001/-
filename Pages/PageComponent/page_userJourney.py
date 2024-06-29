"""
@Author: Li Yu Cai
@Date: 2024/3/11 19:06
@FileName: page_userJourney.py
"""
from Pages.Base import BasePage

import allure
from Utils.tools import tokens
from Conf.config import Config
import json


class UJPage(BasePage):
    def __init__(self, page, log):
        super().__init__(page)
        self.log = log

    @allure.step("打开埋点测试页面")
    def open_url_(self):
        self.open_url('https://www.pre.webullbroker.com/ko-builder/1711346366021-0646cf')
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

    @allure.step('获取指定接口返回参数')
    def listening_response(self, captured_response,
                           url='https://usact.pre.webullbroker.com/api/urcs/v1/content/source/getContentInfo'):

        def record_response(response):
            if url is not None:
                response_url = response.url
                if url in response_url:
                    # 获取响应的文本数据
                    body = response.text()
                    # 提取 newsUrl 字段
                    data = json.loads(body)
                    news_urls1 = [item['newsUrl'] for item in data['data']]
                    for item in news_urls1:
                        captured_response.append(item)
            else:
                # 获取响应的文本数据
                body = response.text()
                # 提取 newsUrl 字段
                data = json.loads(body)
                news_urls1 = [item['newsUrl'] for item in data['data']]
                for item in news_urls1:
                    captured_response.append(item)

        self.page.on("response", record_response)
        return captured_response

    @allure.step('点击后获取第一条链接')
    def get_url_1(self):
        with self.page.expect_popup() as page1_info:
            self.click_element('//*[@id="a3a893_92f194_0"]/span')
        page1 = page1_info.value
        return page1.url

    @allure.step('点击后获取第二条链接')
    def get_url_2(self):
        with self.page.expect_popup() as page1_info:
            self.click_element('//*[@id="a3a893_92f194_1"]/span')
        page1 = page1_info.value
        return page1.url

    @allure.step('点击后获取第三条链接')
    def get_url_3(self):
        with self.page.expect_popup() as page1_info:
            self.click_element('//*[@id="a3a893_92f194_2"]/span')
        page1 = page1_info.value
        return page1.url

    @allure.step('点击后获取第四条链接')
    def get_url_4(self):
        with self.page.expect_popup() as page1_info:
            self.click_element('//*[@id="a3a893_92f194_3"]/span')
        page1 = page1_info.value
        return page1.url

    @allure.step('点击后获取第五条链接')
    def get_url_5(self):
        with self.page.expect_popup() as page1_info:
            self.click_element('//*[@id="a3a893_92f194_4"]/span')
        page1 = page1_info.value
        return page1.url

    @allure.step('分割新闻链接')
    def split_and_compare(self, url1, url2):
        # # 使用正则表达式按照 '?' 和 '&' 分隔符拆分字符串
        # words1 = [].append(re.split(r'[?&]', str1))
        # words2 = [].append(re.split(r'[?&]', str2))
        #
        # # 将拆分后的列表转换为集合（去除重复）
        # set1 = words1[0]
        # set2 = words2[0]
        # 找到问号的位置
        question_mark_index1 = url1.find('?')
        question_mark_index2 = url2.find('?')
        # 提取问号前面的部分
        if question_mark_index1 != -1:
            base_url1 = url1[:question_mark_index1]
        else:
            base_url1 = url1

        if question_mark_index2 != -1:
            base_url2 = url2[:question_mark_index2]
        else:
            base_url2 = url2

        # 检查集合内容是否相同（无视顺序）
        if base_url1 == base_url2:
            return True
        else:
            return False
