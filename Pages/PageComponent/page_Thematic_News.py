"""
@Author: Li Yu Cai
@Date: 2024/5/28 下午2:03
@FileName: page_Thematic_News.py
"""
from Pages.Base import BasePage
import allure
from Utils.tools import tokens
from Conf.config import Config
from Utils.tools import record_response, record_request
import pendulum
import re


class ThematicNewsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @allure.step("changeRatio数据格式化")
    def format_to_percentage(self, value):
        try:
            # 尝试将输入数据转换为浮点数
            number = float(value)
            # 获取数字的符号
            if number > 0:
                sign = "+"
            elif number < 0:
                sign = "-"
            else:
                sign = ""
            # 格式化为百分比，并保留两位小数
            formatted_number = "{}{:.2%}".format(sign, abs(number))
            return formatted_number
        except (ValueError, TypeError):
            # 捕获转换错误并返回默认格式 "0.00%"
            return "0.00%"

    @allure.step("判断changeRatio的颜色")
    def set_color(self, changeRatio):
        if changeRatio is None or float(changeRatio) == 0:
            return 'rgb(0, 0, 0)'
        elif float(changeRatio) > 0:
            return 'rgb(38, 181, 138)'
        else:
            return 'rgb(242, 79, 91)'

    @allure.step("给relTickers数组建立数据结构")
    def get_rel_tickers(self, tickers):

        structured_tickers = []
        if isinstance(tickers, list):
            for i in range(3):
                if len(tickers) <= i:
                    structured_tickers.append({'changeRatio': None,
                                               'disSymbol': None,
                                               'color': None})
                else:
                    structured_tickers.append({
                        'changeRatio': self.format_to_percentage(tickers[i].get('changeRatio')),
                        'disSymbol': tickers[i].get('disSymbol'),
                        'color': self.set_color(tickers[i].get('changeRatio'))

                    })
        return structured_tickers

    @allure.step("打开自选新闻测试页面")
    def open_url_(self):
        self.open_url('https://www.pre.webullbroker.com/ko-builder/1716452880665-babc33')
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
    def listening_response(self, captured_response):
        self.page.on("response", lambda response: (record_response(response, captured_response=captured_response,
                                                                   url='https://usact.pre.webullbroker.com/api/urcs/v1/content/source/getContentInfo')))
        return captured_response

    @allure.step('获取指定接口请求参数')
    def listening_request(self, captured_request):
        # 开启请求拦截
        self.page.route("**/*", lambda route, request: route.continue_())
        # 监听请求事件
        self.page.on("request", lambda request: (
            record_request(request, url='https://usact.pre.webullbroker.com/api/urcs/v1/content/source/getContentInfo',
                           captured_request=captured_request)))
        return captured_request

    @allure.step('解析请求参数')
    def extract_data_request(self, request):
        content_id = []
        for item in request:
            if item['apiCode'] == 'queryNewsContent':
                content_id.append(item)
        return content_id

    @allure.step('解析响应参数')
    def extract_data_response(self, data):
        relative_time = lambda datatime: pendulum.parse(datatime).in_timezone('America/New_York').format(
            'YYYY/MM/DD HH:mm')
        data1 = []
        data2 = []

        for item in data:
            if 'topicName' in item:
                data1.append({
                    'id': item.get('id', ''),
                    'topicName': item.get('topicName', '')
                })
            elif 'title' in item:
                data2.append({
                    'id': item.get('id', None),
                    'title': item.get('title', None),
                    'newsUrl': item.get('newsUrl', None),
                    'mainPic': item.get('mainPic', None),
                    'siteType': item.get('siteType', None),
                    'newsTime': relative_time(item.get('newsTime')),
                    'sourceName': item.get('sourceName', None),
                    'likes': item.get('likes', None),
                    'views': item.get('views', None),
                    'accountImage': item.get('accountImage', None),
                    'relTickers': self.get_rel_tickers(item.get('relTickers', [])),
                    'accountId': item.get('accountId', None),
                    'translated': item.get('translated', None)
                })

        return data1, data2

    @allure.step('获取列表第一项文本')
    def get_text_1(self):
        text = self.get_text(r'#\39 5dc76_a4252b_0 > span')
        return text

    @allure.step('获取列表第二项文本')
    def get_text_2(self):
        text = self.get_text(r'#\33 e6cc9_a4252b_1 > span')
        return text

    @allure.step('获取列表第三项文本')
    def get_text_3(self):
        text = self.get_text(r'#\33 e6cc9_a4252b_2 > span')
        return text

    @allure.step('获取列表第四项文本')
    def get_text_4(self):
        text = self.get_text(r'#\33 e6cc9_a4252b_3 > span')
        return text

    @allure.step('点击列表展示更多')
    def click_element_(self):
        self.click_element(r'#\36 978ba_a4252b > span')

    @allure.step('获取第一项新闻的title')
    def get_title_1(self):
        text = self.get_text(r'#\36 dce86_a4252b_0 > span')
        return text

    @allure.step('获取第二项新闻的title')
    def get_title_2(self):
        text = self.get_text(r'#\36 dce86_a4252b_1 > span')
        return text

    @allure.step('获取第三项新闻的title')
    def get_title_3(self):
        text = self.get_text(r'#\36 dce86_a4252b_2 > span')
        return text

    @allure.step('获取第四项新闻的title')
    def get_title_4(self):
        text = self.get_text(r'#\36 dce86_a4252b_3 > span')
        return text

    @allure.step('获取第五项新闻的title')
    def get_title_5(self):
        text = self.get_text(r'#\36 dce86_a4252b_4 > span')
        return text

    @allure.step('获取第一项新闻的图片')
    def get_news_picture_1(self):
        picture_url = self.get_picture(r'#\30 4d5fa_a4252b_0 > img')
        return picture_url

    @allure.step('获取第二项新闻的图片')
    def get_news_picture_2(self):
        picture_url = self.get_picture(r'#\30 4d5fa_a4252b_1 > img')
        return picture_url

    @allure.step('获取第三项新闻的图片')
    def get_news_picture_3(self):
        picture_url = self.get_picture(r'#\30 4d5fa_a4252b_2 > img')
        return picture_url

    @allure.step('获取第四项新闻的图片')
    def get_news_picture_4(self):
        picture_url = self.get_picture(r'#\30 4d5fa_a4252b_3 > img')
        return picture_url

    @allure.step('获取第五项新闻的图片')
    def get_news_picture_5(self):
        picture_url = self.get_picture(r'#\30 4d5fa_a4252b_4 > img')
        return picture_url

    @allure.step('获取第一项新闻的作者及时间')
    def get_news_source_name_1(self):
        text = self.get_text(r'#\34 974af_a4252b_0 > span')
        name_time = re.split(r' · ', text)
        return name_time

    @allure.step('获取第二项新闻的作者及时间')
    def get_news_source_name_2(self):
        text = self.get_text(r'#\34 974af_a4252b_1 > span')
        name_time = re.split(r' · ', text)
        return name_time

    @allure.step('获取第三项新闻的作者及时间')
    def get_news_source_name_3(self):
        text = self.get_text(r'#\34 974af_a4252b_2 > span')
        name_time = re.split(r' · ', text)
        return name_time

    @allure.step('获取第四项新闻的作者及时间')
    def get_news_source_name_4(self):
        text = self.get_text(r'#\34 974af_a4252b_3 > span')
        name_time = re.split(r' · ', text)
        return name_time

    @allure.step('获取第五项新闻的作者及时间')
    def get_news_source_name_5(self):
        text = self.get_text(r'#\34 974af_a4252b_4 > span')
        name_time = re.split(r' · ', text)
        return name_time

    @allure.step('获取第一项新闻的作者图片')
    def get_news_name_picture_1(self):
        picture_url = self.get_picture(r'#\33 0a836_a4252b_0 > img')
        return picture_url

    @allure.step('获取第二项新闻的作者图片')
    def get_news_name_picture_2(self):
        picture_url = self.get_picture(r'#\33 0a836_a4252b_1 > img')
        return picture_url

    @allure.step('获取第三项新闻的作者图片')
    def get_news_name_picture_3(self):
        picture_url = self.get_picture(r'#\33 0a836_a4252b_2 > img')
        return picture_url

    @allure.step('获取第四项新闻的作者图片')
    def get_news_name_picture_4(self):
        picture_url = self.get_picture(r'#\33 0a836_a4252b_3 > img')
        return picture_url

    @allure.step('获取第五项新闻的作者图片')
    def get_news_name_picture_5(self):
        picture_url = self.get_picture(r'#\33 0a836_a4252b_4 > img')
        return picture_url

    @allure.step('切换列表项')
    def click_element_tab(self, tab):
        if tab == 2:
            self.click_element(r'#\33 7ca40_a4252b_1')
        if tab == 3:
            self.click_element(r'#\33 7ca40_a4252b_2')
        if tab == 4:
            self.click_element(r'#\33 7ca40_a4252b_3')
        if tab == 5:
            self.click_element(r'#\33 7ca40_a4252b_4')
        if tab == 6:
            self.click_element(r'#\33 7ca40_a4252b_5')

    @allure.step('获取第一项新闻的changeRatio和disSymbol')
    def get_title_symbol_ratio(self, line):
        if line == 1:

            element1 = self.page.query_selector(r'#\33 657ff_a4252b_0 > span')

            if element1 is None:
                text1 = []
            else:
                text1 = self.get_text(r'#\33 657ff_a4252b_0 > span')
                text1 = re.split(r' ', text1)
                text1.append(self.get_color(r'#\33 657ff_a4252b_0 > span'))

            element2 = self.page.query_selector(r'#\38 43ac7_a4252b_0 > span')  # \38 43ac7_a4252b_0 > span

            if element2 is None:
                text2 = []
            else:
                text2 = self.get_text(r'#\38 43ac7_a4252b_0 > span')
                text2 = re.split(r' ', text2)
                text2.append(self.get_color(r'#\38 43ac7_a4252b_0 > span'))

            element3 = self.page.query_selector(r'#\31 fd77e_a4252b_0 > span')

            if element3 is None:
                text3 = []
            else:
                text3 = self.get_text(r'#\31 fd77e_a4252b_0 > span')
                text3 = re.split(r' ', text3)
                text3.append(self.get_color(r'#\31 fd77e_a4252b_0 > span'))
            return text1, text2, text3

        elif line == 2:

            element1 = self.page.query_selector(r'#\33 657ff_a4252b_1 > span')

            if element1 is None:
                text1 = []
            else:
                text1 = self.get_text(r'#\33 657ff_a4252b_1 > span')
                text1 = re.split(r' ', text1)
                text1.append(self.get_color(r'#\33 657ff_a4252b_1 > span'))

            element2 = self.page.query_selector(r'#\38 43ac7_a4252b_1 > span')
            if element2 is None:
                text2 = []
            else:
                text2 = self.get_text(r'#\38 43ac7_a4252b_1 > span')
                text2 = re.split(r' ', text2)
                text2.append(self.get_color(r'#\38 43ac7_a4252b_1 > span'))

            element3 = self.page.query_selector(r'#\31 fd77e_a4252b_1 > span')  # \31 fd77e_a4252b_1 > span

            if element3 is None:
                text3 = []
                print('element3', element3)
            else:
                text3 = self.get_text(r'#\31 fd77e_a4252b_1 > span')
                text3 = re.split(r' ', text3)
                text3.append(self.get_color(r'#\31 fd77e_a4252b_1 > span'))
            return text1, text2, text3

        elif line == 3:

            element1 = self.page.query_selector(r'#\33 657ff_a4252b_2 > span')

            if element1 is None:
                text1 = []
            else:
                text1 = self.get_text(r'#\33 657ff_a4252b_2 > span')
                text1 = re.split(r' ', text1)
                text1.append(self.get_color(r'#\33 657ff_a4252b_2 > span'))

            element2 = self.page.query_selector(r'#\38 43ac7_a4252b_2 > span')

            if element2 is None:
                text2 = []
            else:
                text2 = self.get_text(r'#\38 43ac7_a4252b_2 > span')
                text2 = re.split(r' ', text2)
                text2.append(self.get_color(r'#\38 43ac7_a4252b_2 > span'))

            element3 = self.page.query_selector(r'#\31 fd77e_a4252b_2 > span')

            if element3 is None:
                text3 = []
            else:
                text3 = self.get_text(r'#\31 fd77e_a4252b_2 > span')
                text3 = re.split(r' ', text3)
                text3.append(self.get_color(r'#\31 fd77e_a4252b_2 > span'))
            return text1, text2, text3

        elif line == 4:

            element1 = self.page.query_selector(r'#\33 657ff_a4252b_3 > span')

            if element1 is None:
                text1 = []
            else:
                text1 = self.get_text(r'#\33 657ff_a4252b_3 > span')
                text1 = re.split(r' ', text1)
                text1.append(self.get_color(r'#\33 657ff_a4252b_3 > span'))

            element2 = self.page.query_selector(r'#\38 43ac7_a4252b_3 > span')

            if element2 is None:
                text2 = []
            else:
                text2 = self.get_text(r'#\38 43ac7_a4252b_3 > span')
                text2 = re.split(r' ', text2)
                text2.append(self.get_color(r'#\38 43ac7_a4252b_3 > span'))

            element3 = self.page.query_selector(r'#\31 fd77e_a4252b_3 > span')

            if element3 is None:
                text3 = []
            else:
                text3 = self.get_text(r'#\31 fd77e_a4252b_3 > span')  # \31 fd77e_a4252b_3 > span
                text3 = re.split(r' ', text3)
                text3.append(self.get_color(r'#\31 fd77e_a4252b_3 > span'))
            return text1, text2, text3

        elif line == 5:

            element1 = self.page.query_selector(r'#\33 657ff_a4252b_4 > span')
            if element1 is None:
                text1 = []
            else:
                text1 = self.get_text(r'#\33 657ff_a4252b_4 > span')
                text1 = re.split(r' ', text1)
                text1.append(self.get_color(r'#\33 657ff_a4252b_4 > span'))

            element2 = self.page.query_selector(r'#\38 43ac7_a4252b_4 > span')
            if element2 is None:
                text2 = []
            else:
                text2 = self.get_text(r'#\38 43ac7_a4252b_4 > span')
                text2 = re.split(r' ', text2)
                text2.append(self.get_color(r'#\38 43ac7_a4252b_4 > span'))

            element3 = self.page.query_selector(r'#\31 fd77e_a4252b_4 > span')
            if element3 is None:
                text3 = []
            else:
                text3 = self.get_text(r'#\31 fd77e_a4252b_4 > span')
                text3 = re.split(r' ', text3)
                text3.append(self.get_color(r'#\31 fd77e_a4252b_4 > span'))
            return text1, text2, text3
