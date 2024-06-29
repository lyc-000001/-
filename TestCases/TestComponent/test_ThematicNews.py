"""
@Author: Li Yu Cai
@Date: 2024/5/28 下午2:02
@FileName: test_Thematic_News.py
"""
from Pages.PageComponent.page_Thematic_News import ThematicNewsPage
import allure
from Utils.Log import Msg


class TestThematicNews:
    @staticmethod
    def step(msg=''):
        log = Msg(name='自选新闻榜单测试')
        log.info(msg)
        return allure.step(msg)

    def test_thematic_news(self, base_page):
        captured_response = []
        captured_request = []
        new_page = ThematicNewsPage(base_page)
        self.step('获取接口请求参数')
        request = new_page.listening_request(captured_request)
        self.step('获取接口返回值')
        response = new_page.listening_response(captured_response)
        self.step('获取登录信息')
        new_page.get_token()
        self.step('打开自选新闻测试页面')
        new_page.open_url_()
        self.step('处理请求参数')
        request_data = new_page.extract_data_request(request)
        tab1_req_data_len = len(request_data)
        self.step('处理响应数据')
        response_data1, response_data2 = new_page.extract_data_response(response)
        response_data1_len = len(response_data1)
        tab1_rep_data_len = len(response_data2)
        self.step('新闻content_id的第一响标题并做断言')
        text = new_page.get_text_1()
        assert response_data1[0]['topicName'] == text
        self.step('新闻content_id的第二响标题并做断言')
        text = new_page.get_text_2()
        assert response_data1[1]['topicName'] == text
        self.step('新闻content_id的第三响标题并做断言')
        text = new_page.get_text_3()
        assert response_data1[2]['topicName'] == text
        self.step('新闻content_id的第四响标题并做断言')
        text = new_page.get_text_4()
        assert response_data1[3]['topicName'] == text

        if tab1_req_data_len == 0:
            self.step('判断第一页数据是否使用了接口返回的contentid')
            assert int(response_data1[0]['id']) == int(request_data[0]['contentId'])
            self.step('断言第一页第一项新闻的title')
            title = new_page.get_title_1()
            assert title is None
            self.step('断言第一页第二项新闻的title')
            title = new_page.get_title_2()
            assert title is None
            self.step('断言第一页第三项新闻的title')
            title = new_page.get_title_3()
            assert title is None
            self.step('断言第一页第四项新闻的title')
            title = new_page.get_title_4()
            assert title is None
            self.step('断言第一页第五项新闻的title')
            title = new_page.get_title_5()
            assert title is None
            self.step('断言第一页第一项新闻的图片')
            picture_url = new_page.get_news_picture_1()
            assert picture_url is None
            self.step('断言第一页第二项新闻的图片')
            picture_url = new_page.get_news_picture_2()
            assert picture_url is None
            self.step('断言第一页第三项新闻的图片')
            picture_url = new_page.get_news_picture_3()
            assert picture_url is None
            self.step('断言第一页第四项新闻的图片')
            picture_url = new_page.get_news_picture_4()
            assert picture_url is None
            self.step('断言第一页第五项新闻的图片')
            picture_url = new_page.get_news_picture_5()
            assert picture_url is None
            self.step('断言第一页第一项新闻的作者及时间')
            name_time = new_page.get_news_source_name_1()
            assert name_time[0] is None and name_time[1] is None
            self.step('断言第一页第二项新闻的作者及时间')
            name_time = new_page.get_news_source_name_2()
            assert name_time[0] is None and name_time[1] is None
            self.step('断言第一页第三项新闻的作者及时间')
            name_time = new_page.get_news_source_name_3()
            assert name_time[0] is None and name_time[1] is None
            self.step('断言第一页第四项新闻的作者及时间')
            name_time = new_page.get_news_source_name_4()
            assert name_time[0] is None and name_time[1] is None
            self.step('断言第一页第五项新闻的作者及时间')
            name_time = new_page.get_news_source_name_5()
            assert name_time[0] is None and name_time[1] is None
            self.step('断言第一页第一项新闻的作者图片')
            picture_url = new_page.get_news_name_picture_1()
            assert picture_url is None
            self.step('断言第一页第二项新闻的作者图片')
            picture_url = new_page.get_news_name_picture_2()
            assert picture_url is None
            self.step('断言第一页第三项新闻的作者图片')
            picture_url = new_page.get_news_name_picture_3()
            assert picture_url is None
            self.step('断言第一页第四项新闻的作者图片')
            picture_url = new_page.get_news_name_picture_4()
            assert picture_url is None
            self.step('断言第一页第五项新闻的作者图片')
            picture_url = new_page.get_news_name_picture_5()
            assert picture_url is None
        else:

            self.step('判断第一页数据是否使用了接口返回的contentid')
            assert int(response_data1[0]['id']) == int(request_data[0]['contentId'])
            new_page.click_element_()
            self.step('断言第一页第一项新闻的title')
            title = new_page.get_title_1()
            assert title == response_data2[0]['title']
            self.step('断言第一页第二项新闻的title')
            title = new_page.get_title_2()
            assert title == response_data2[1]['title']
            self.step('断言第一页第三项新闻的title')
            title = new_page.get_title_3()
            assert title == response_data2[2]['title']
            self.step('断言第一页第四项新闻的title')
            title = new_page.get_title_4()
            assert title == response_data2[3]['title']
            self.step('断言第一页第五项新闻的title')
            title = new_page.get_title_5()
            assert title == response_data2[4]['title']
            self.step('断言第一页第一项新闻的图片')
            picture_url = new_page.get_news_picture_1()
            assert picture_url == response_data2[0]['mainPic']
            self.step('断言第一页第二项新闻的图片')
            picture_url = new_page.get_news_picture_2()
            assert picture_url == response_data2[1]['mainPic']
            self.step('断言第一页第三项新闻的图片')
            picture_url = new_page.get_news_picture_3()
            assert picture_url == response_data2[2]['mainPic']
            self.step('断言第一页第四项新闻的图片')
            picture_url = new_page.get_news_picture_4()
            assert picture_url == response_data2[3]['mainPic']
            self.step('断言第一页第五项新闻的图片')
            picture_url = new_page.get_news_picture_5()
            assert picture_url == response_data2[4]['mainPic']
            self.step('断言第一页第一项新闻的作者及时间')
            name_time = new_page.get_news_source_name_1()
            assert name_time[0] == response_data2[0]['sourceName'] and name_time[1] == response_data2[0]['newsTime']
            self.step('断言第一页第二项新闻的作者及时间')
            name_time = new_page.get_news_source_name_2()
            assert name_time[0] == response_data2[1]['sourceName'] and name_time[1] == response_data2[1]['newsTime']
            self.step('断言第一页第三项新闻的作者及时间')
            name_time = new_page.get_news_source_name_3()
            assert name_time[0] == response_data2[2]['sourceName'] and name_time[1] == response_data2[2]['newsTime']
            self.step('断言第一页第四项新闻的作者及时间')
            name_time = new_page.get_news_source_name_4()
            assert name_time[0] == response_data2[3]['sourceName'] and name_time[1] == response_data2[3]['newsTime']
            self.step('断言第一页第五项新闻的作者及时间')
            name_time = new_page.get_news_source_name_5()
            assert name_time[0] == response_data2[4]['sourceName'] and name_time[1] == response_data2[4]['newsTime']
            self.step('断言第一页第一项新闻的作者图片')
            picture_url = new_page.get_news_name_picture_1()
            assert picture_url == response_data2[0]['accountImage']
            self.step('断言第一页第二项新闻的作者图片')
            picture_url = new_page.get_news_name_picture_2()
            assert picture_url == response_data2[1]['accountImage']
            self.step('断言第一页第三项新闻的作者图片')
            picture_url = new_page.get_news_name_picture_3()
            assert picture_url == response_data2[2]['accountImage']
            self.step('断言第一页第四项新闻的作者图片')
            picture_url = new_page.get_news_name_picture_4()
            assert picture_url == response_data2[3]['accountImage']
            self.step('断言第一页第五项新闻的作者图片')
            picture_url = new_page.get_news_name_picture_5()
            assert picture_url == response_data2[4]['accountImage']
            self.step('断言第一页第一项changeRatio和disSymbol字段')
            text1, text2, text3 = new_page.get_title_symbol_ratio(1)
            if len(text1) >= 2:
                assert text1[0] == response_data2[0]['relTickers'][0]['disSymbol'] and text1[1] == \
                       response_data2[0]['relTickers'][0]['changeRatio'] and text1[2] == \
                       response_data2[0]['relTickers'][0]['color']
            else:
                assert len(text1) == 0 and response_data2[0]['relTickers'][0]['disSymbol'] is None

            if len(text2) >= 2:
                assert text2[0] == response_data2[0]['relTickers'][1]['disSymbol'] and text2[1] == \
                       response_data2[0]['relTickers'][1]['changeRatio'] and text2[2] == \
                       response_data2[0]['relTickers'][1]['color']
            else:
                assert len(text2) == 0 and response_data2[0]['relTickers'][1]['disSymbol'] is None

            if len(text3) >= 2:
                assert text3[0] == response_data2[0]['relTickers'][2]['disSymbol'] and text3[1] == \
                       response_data2[0]['relTickers'][2]['changeRatio'] and text3[2] == \
                       response_data2[0]['relTickers'][2]['color']
            else:
                assert len(text3) == 0 and response_data2[0]['relTickers'][2]['disSymbol'] is None
            self.step('断言第一页第二项changeRatio和disSymbol字段')
            text1, text2, text3 = new_page.get_title_symbol_ratio(2)
            if len(text1) >= 2:
                assert text1[0] == response_data2[1]['relTickers'][0]['disSymbol'] and text1[1] == \
                       response_data2[1]['relTickers'][0]['changeRatio'] and text1[2] == \
                       response_data2[1]['relTickers'][0]['color']
            else:
                assert len(text1) == 0 and response_data2[1]['relTickers'][0]['disSymbol'] is None

            if len(text2) >= 2:
                assert text2[0] == response_data2[1]['relTickers'][1]['disSymbol'] and text2[1] == \
                       response_data2[1]['relTickers'][1]['changeRatio'] and text2[2] == \
                       response_data2[1]['relTickers'][1]['color']
            else:
                assert len(text2) == 0 and response_data2[1]['relTickers'][1]['disSymbol'] is None

            if len(text3) >= 2:
                assert text3[0] == response_data2[1]['relTickers'][2]['disSymbol'] and text3[1] == \
                       response_data2[1]['relTickers'][2]['changeRatio'] and text3[2] == \
                       response_data2[1]['relTickers'][2]['color']
            else:
                assert len(text3) == 0 and response_data2[1]['relTickers'][2]['disSymbol'] is None
            self.step('断言第一页第三项changeRatio和disSymbol字段')
            text1, text2, text3 = new_page.get_title_symbol_ratio(3)
            if len(text1) >= 2:
                assert text1[0] == response_data2[2]['relTickers'][0]['disSymbol'] and text1[1] == \
                       response_data2[2]['relTickers'][0]['changeRatio'] and text1[2] == \
                       response_data2[2]['relTickers'][0]['color']
            else:
                assert len(text1) == 0 and response_data2[2]['relTickers'][0]['disSymbol'] is None

            if len(text2) >= 2:
                assert text2[0] == response_data2[2]['relTickers'][1]['disSymbol'] and text2[1] == \
                       response_data2[2]['relTickers'][1]['changeRatio'] and text2[2] == \
                       response_data2[2]['relTickers'][1]['color']
            else:
                assert len(text2) == 0 and response_data2[2]['relTickers'][1]['disSymbol'] is None

            if len(text3) >= 2:
                assert text3[0] == response_data2[2]['relTickers'][2]['disSymbol'] and text3[1] == \
                       response_data2[2]['relTickers'][2]['changeRatio'] and text3[2] == \
                       response_data2[2]['relTickers'][2]['color']
            else:
                assert len(text3) == 0 and response_data2[2]['relTickers'][2]['disSymbol'] is None
            self.step('断言第一页第四项changeRatio和disSymbol字段')
            text1, text2, text3 = new_page.get_title_symbol_ratio(4)
            if len(text1) >= 2:
                assert text1[0] == response_data2[3]['relTickers'][0]['disSymbol'] and text1[1] == \
                       response_data2[3]['relTickers'][0]['changeRatio'] and text1[2] == \
                       response_data2[3]['relTickers'][0]['color']
            else:
                assert len(text1) == 0 and response_data2[3]['relTickers']  [0]['disSymbol'] is None

            if len(text2) >= 2:
                assert text2[0] == response_data2[3]['relTickers'][1]['disSymbol'] and text2[1] == \
                       response_data2[3]['relTickers'][1]['changeRatio'] and text2[2] == \
                       response_data2[3]['relTickers'][1]['color']
            else:
                assert len(text2) == 0 and response_data2[3]['relTickers'][1]['disSymbol'] is None

            if len(text3) >= 2:
                assert text3[0] == response_data2[3]['relTickers'][2]['disSymbol'] and text3[1] == \
                       response_data2[3]['relTickers'][2]['changeRatio'] and text3[2] == \
                       response_data2[3]['relTickers'][2]['color']
            else:
                assert len(text3) == 0 and response_data2[3]['relTickers'][2]['disSymbol'] is None
            self.step('断言第一页第五项changeRatio和disSymbol字段')
            text1, text2, text3 = new_page.get_title_symbol_ratio(5)
            if len(text1) >= 2:
                assert text1[0] == response_data2[4]['relTickers'][0]['disSymbol'] and text1[1] == \
                       response_data2[4]['relTickers'][0]['changeRatio'] and text1[2] == \
                       response_data2[4]['relTickers'][0]['color']
            else:
                assert len(text1) == 0 and response_data2[4]['relTickers'][0]['disSymbol'] is None

            if len(text2) >= 2:
                assert text2[0] == response_data2[4]['relTickers'][1]['disSymbol'] and text2[1] == \
                       response_data2[4]['relTickers'][1]['changeRatio'] and text2[2] == \
                       response_data2[4]['relTickers'][1]['color']
            else:
                assert len(text2) == 0 and response_data2[4]['relTickers'][1]['disSymbol'] is None

            if len(text3) >= 2:
                assert text3[0] == response_data2[4]['relTickers'][2]['disSymbol'] and text3[1] == \
                       response_data2[4]['relTickers'][2]['changeRatio'] and text3[2] == \
                       response_data2[4]['relTickers'][2]['color']
            else:
                assert len(text3) == 0 and response_data2[4]['relTickers'][2]['disSymbol'] is None

        if response_data1_len >= 2:
            self.step('切换列表至第2个tab')
            new_page.click_element_tab(2)
            new_page.waits()
            self.step('处理请求参数')
            request_data = new_page.extract_data_request(request)
            self.step('处理响应数据')
            response_data1, response_data2 = new_page.extract_data_response(response)
            if len(response_data2) == tab1_req_data_len:
                self.step('判断第二页数据是否使用了接口返回的contentid')
                assert int(response_data1[1]['id']) == int(request_data[tab1_req_data_len]['contentId'])
                self.step('断言第二页第一项新闻的title')
                title = new_page.get_title_1()
                assert title is None
                self.step('断言第二页第二项新闻的title')
                title = new_page.get_title_2()
                assert title is None
                self.step('断言第二页第三项新闻的title')
                title = new_page.get_title_3()
                assert title is None
                self.step('断言第二页第四项新闻的title')
                title = new_page.get_title_4()
                assert title is None
                self.step('断言第二页第五项新闻的title')
                title = new_page.get_title_5()
                assert title is None
                self.step('断言第二页第一项新闻的图片')
                picture_url = new_page.get_news_picture_1()
                assert picture_url is None
                self.step('断言第二页第二项新闻的图片')
                picture_url = new_page.get_news_picture_2()
                assert picture_url is None
                self.step('断言第二页第三项新闻的图片')
                picture_url = new_page.get_news_picture_3()
                assert picture_url is None
                self.step('断言第二页第四项新闻的图片')
                picture_url = new_page.get_news_picture_4()
                assert picture_url is None
                self.step('断言第二页第五项新闻的图片')
                picture_url = new_page.get_news_picture_5()
                assert picture_url is None
                self.step('断言第二页第一项新闻的作者及时间')
                name_time = new_page.get_news_source_name_1()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第二页第二项新闻的作者及时间')
                name_time = new_page.get_news_source_name_2()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第二页第三项新闻的作者及时间')
                name_time = new_page.get_news_source_name_3()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第二页第四项新闻的作者及时间')
                name_time = new_page.get_news_source_name_4()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第二页第五项新闻的作者及时间')
                name_time = new_page.get_news_source_name_5()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第二页第一项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_1()
                assert picture_url is None
                self.step('断言第二页第二项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_2()
                assert picture_url is None
                self.step('断言第二页第三项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_3()
                assert picture_url is None
                self.step('断言第二页第四项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_4()
                assert picture_url is None
                self.step('断言第二页第五项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_5()
                assert picture_url is None
            else:

                self.step('判断第二页数据是否使用了接口返回的contentid')
                assert int(response_data1[1]['id']) == int(request_data[tab1_req_data_len]['contentId'])
                self.step('断言第二页第一项新闻的title')
                title = new_page.get_title_1()
                assert title == response_data2[tab1_rep_data_len]['title']
                self.step('断言第二页第二项新闻的title')
                title = new_page.get_title_2()
                assert title == response_data2[tab1_rep_data_len + 1]['title']
                self.step('断言第二页第三项新闻的title')
                title = new_page.get_title_3()
                assert title == response_data2[tab1_rep_data_len + 2]['title']
                self.step('断言第二页第四项新闻的title')
                title = new_page.get_title_4()
                assert title == response_data2[tab1_rep_data_len + 3]['title']
                self.step('断言第二页第五项新闻的title')
                title = new_page.get_title_5()
                assert title == response_data2[tab1_rep_data_len + 4]['title']
                self.step('断言第二页第一项新闻的图片')
                picture_url = new_page.get_news_picture_1()
                assert picture_url == response_data2[tab1_rep_data_len]['mainPic']
                self.step('断言第二页第二项新闻的图片')
                picture_url = new_page.get_news_picture_2()
                assert picture_url == response_data2[tab1_rep_data_len + 1]['mainPic']
                self.step('断言第二页第三项新闻的图片')
                picture_url = new_page.get_news_picture_3()
                assert picture_url == response_data2[tab1_rep_data_len + 2]['mainPic']
                self.step('断言第二页第四项新闻的图片')
                picture_url = new_page.get_news_picture_4()
                assert picture_url == response_data2[tab1_rep_data_len + 3]['mainPic']
                self.step('断言第二页第五项新闻的图片')
                picture_url = new_page.get_news_picture_5()
                assert picture_url == response_data2[tab1_rep_data_len + 4]['mainPic']
                self.step('断言第二页第一项新闻的作者及时间')
                name_time = new_page.get_news_source_name_1()
                assert name_time[0] == response_data2[tab1_rep_data_len]['sourceName'] and name_time[1] == \
                       response_data2[tab1_rep_data_len][
                           'newsTime']
                self.step('断言第二页第二项新闻的作者及时间')
                name_time = new_page.get_news_source_name_2()
                assert name_time[0] == response_data2[tab1_rep_data_len + 1]['sourceName'] and name_time[1] == \
                       response_data2[tab1_rep_data_len + 1]['newsTime']
                self.step('断言第二页第三项新闻的作者及时间')
                name_time = new_page.get_news_source_name_3()
                assert name_time[0] == response_data2[tab1_rep_data_len + 2]['sourceName'] and name_time[1] == \
                       response_data2[tab1_rep_data_len + 2]['newsTime']
                self.step('断言第二页第四项新闻的作者及时间')
                name_time = new_page.get_news_source_name_4()
                assert name_time[0] == response_data2[tab1_rep_data_len + 3]['sourceName'] and name_time[1] == \
                       response_data2[tab1_rep_data_len + 3]['newsTime']
                self.step('断言第二页第五项新闻的作者及时间')
                name_time = new_page.get_news_source_name_5()
                assert name_time[0] == response_data2[tab1_rep_data_len + 4]['sourceName'] and name_time[1] == \
                       response_data2[tab1_rep_data_len + 4]['newsTime']
                self.step('断言第二页第一项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_1()
                assert picture_url == response_data2[tab1_rep_data_len + 0]['accountImage']
                self.step('断言第二页第二项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_2()
                assert picture_url == response_data2[tab1_rep_data_len + 1]['accountImage']
                self.step('断言第二页第三项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_3()
                assert picture_url == response_data2[tab1_rep_data_len + 2]['accountImage']
                self.step('断言第二页第四项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_4()
                assert picture_url == response_data2[tab1_rep_data_len + 3]['accountImage']
                self.step('断言第二页第五项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_5()
                assert picture_url == response_data2[tab1_rep_data_len + 4]['accountImage']
                self.step('断言第二页第一项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(1)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab1_rep_data_len + 0]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab1_rep_data_len + 0]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab1_rep_data_len + 0]['relTickers'][0]['color']

                else:
                    assert len(text1) == 0 and response_data2[tab1_rep_data_len + 0]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab1_rep_data_len + 0]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab1_rep_data_len + 0]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab1_rep_data_len + 0]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab1_rep_data_len + 0]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    assert text3[0] == response_data2[tab1_rep_data_len + 0]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab1_rep_data_len + 0]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab1_rep_data_len + 0]['relTickers'][2]['color']
                else:

                    assert len(text3) == 0 and response_data2[tab1_rep_data_len + 0]['relTickers'][2][
                        'disSymbol'] is None

                self.step('断言第二页第二项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(2)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab1_rep_data_len + 1]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab1_rep_data_len + 1]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab1_rep_data_len + 1]['relTickers'][0]['color']
                else:
                    assert len(text1) == 0 and response_data2[tab1_rep_data_len + 1]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab1_rep_data_len + 1]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab1_rep_data_len + 1]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab1_rep_data_len + 1]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab1_rep_data_len + 1]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    assert text3[0] == response_data2[tab1_rep_data_len + 1]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab1_rep_data_len + 1]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab1_rep_data_len + 1]['relTickers'][2]['color']
                else:
                    assert len(text3) == 0 and response_data2[tab1_rep_data_len + 1]['relTickers'][2][
                        'disSymbol'] is None
                self.step('断言第二页第三项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(3)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab1_rep_data_len + 2]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab1_rep_data_len + 2]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab1_rep_data_len + 2]['relTickers'][0]['color']
                else:
                    assert len(text1) == 0 and response_data2[tab1_rep_data_len + 2]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab1_rep_data_len + 2]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab1_rep_data_len + 2]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab1_rep_data_len + 2]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab1_rep_data_len + 2]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    assert text3[0] == response_data2[tab1_rep_data_len + 2]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab1_rep_data_len + 2]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab1_rep_data_len + 2]['relTickers'][2]['color']
                else:
                    assert len(text3) == 0 and response_data2[tab1_rep_data_len + 2]['relTickers'][2][
                        'disSymbol'] is None

                self.step('断言第二页第四项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(4)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab1_rep_data_len + 3]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab1_rep_data_len + 3]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab1_rep_data_len + 3]['relTickers'][0]['color']
                else:
                    assert len(text1) == 0 and response_data2[tab1_rep_data_len + 3]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab1_rep_data_len + 3]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab1_rep_data_len + 3]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab1_rep_data_len + 3]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab1_rep_data_len + 3]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    assert text3[0] == response_data2[tab1_rep_data_len + 3]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab1_rep_data_len + 3]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab1_rep_data_len + 3]['relTickers'][2]['color']
                else:
                    print(response_data2[tab1_rep_data_len + 3]['relTickers'][2], text3)
                    assert len(text3) == 0 and response_data2[tab1_rep_data_len + 3]['relTickers'][2][
                        'disSymbol'] is None

                self.step('断言第二页第五项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(5)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab1_rep_data_len + 4]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab1_rep_data_len + 4]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab1_rep_data_len + 4]['relTickers'][0]['color']
                else:
                    assert len(text1) == 0 and response_data2[tab1_rep_data_len + 4]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab1_rep_data_len + 4]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab1_rep_data_len + 4]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab1_rep_data_len + 4]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab1_rep_data_len + 4]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    print(text3, response_data2[tab1_rep_data_len + 4]['relTickers'][2])
                    assert text3[0] == response_data2[tab1_rep_data_len + 4]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab1_rep_data_len + 4]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab1_rep_data_len + 4]['relTickers'][2]['color']
                else:

                    assert len(text3) == 0 and response_data2[tab1_rep_data_len + 4]['relTickers'][2][
                        'disSymbol'] is None

        tab2_req_data_len = len(request_data)
        tab2_rep_data_len = len(response_data2)

        if response_data1_len >= 3:
            self.step('切换列表至第三个tab')
            new_page.click_element_tab(3)
            new_page.waits()
            self.step('处理请求参数')
            request_data = new_page.extract_data_request(request)
            self.step('处理响应数据')
            response_data1, response_data2 = new_page.extract_data_response(response)
            if len(response_data2) == tab2_rep_data_len:
                self.step('判断第三页数据是否使用了接口返回的contentid')
                assert int(response_data1[2]['id']) == int(request_data[tab2_req_data_len]['contentId'])
                self.step('断言第三页第一项新闻的title')
                title = new_page.get_title_1()
                assert title is None
                self.step('断言第三页第二项新闻的title')
                title = new_page.get_title_2()
                assert title is None
                self.step('断言第三页第三项新闻的title')
                title = new_page.get_title_3()
                assert title is None
                self.step('断言第三页第四项新闻的title')
                title = new_page.get_title_4()
                assert title is None
                self.step('断言第三页第五项新闻的title')
                title = new_page.get_title_5()
                assert title is None
                self.step('断言第三页第一项新闻的图片')
                picture_url = new_page.get_news_picture_1()
                assert picture_url is None
                self.step('断言第三页第二项新闻的图片')
                picture_url = new_page.get_news_picture_2()
                assert picture_url is None
                self.step('断言第三页第三项新闻的图片')
                picture_url = new_page.get_news_picture_3()
                assert picture_url is None
                self.step('断言第三页第四项新闻的图片')
                picture_url = new_page.get_news_picture_4()
                assert picture_url is None
                self.step('断言第三页第五项新闻的图片')
                picture_url = new_page.get_news_picture_5()
                assert picture_url is None
                self.step('断言第页三第一项新闻的作者及时间')
                name_time = new_page.get_news_source_name_1()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第三页第二项新闻的作者及时间')
                name_time = new_page.get_news_source_name_2()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第三页第三项新闻的作者及时间')
                name_time = new_page.get_news_source_name_3()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第三页第四项新闻的作者及时间')
                name_time = new_page.get_news_source_name_4()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第三页第五项新闻的作者及时间')
                name_time = new_page.get_news_source_name_5()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第三页第一项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_1()
                assert picture_url is None
                self.step('断言第三页第二项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_2()
                assert picture_url is None
                self.step('断言第页三第三项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_3()
                assert picture_url is None
                self.step('断言第三页第四项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_4()
                assert picture_url is None
                self.step('断言第三页第五项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_5()
                assert picture_url is None
            else:
                self.step('判断第三页数据是否使用了接口返回的contentid')
                assert int(response_data1[2]['id']) == int(request_data[tab2_req_data_len]['contentId'])
                self.step('断言第三页第一项新闻的title')
                title = new_page.get_title_1()
                assert title == response_data2[tab2_rep_data_len]['title']
                self.step('断言第三页第二项新闻的title')
                title = new_page.get_title_2()
                assert title == response_data2[tab2_rep_data_len + 1]['title']
                self.step('断言第三页第三项新闻的title')
                title = new_page.get_title_3()
                assert title == response_data2[tab2_rep_data_len + 2]['title']
                self.step('断言第三页第四项新闻的title')
                title = new_page.get_title_4()
                assert title == response_data2[tab2_rep_data_len + 3]['title']
                self.step('断言第三页第五项新闻的title')
                title = new_page.get_title_5()
                assert title == response_data2[tab2_rep_data_len + 4]['title']
                self.step('断言第三页第一项新闻的图片')
                picture_url = new_page.get_news_picture_1()
                assert picture_url == response_data2[tab2_rep_data_len]['mainPic']
                self.step('断言第三页第二项新闻的图片')
                picture_url = new_page.get_news_picture_2()
                assert picture_url == response_data2[tab2_rep_data_len + 1]['mainPic']
                self.step('断言第三页第三项新闻的图片')
                picture_url = new_page.get_news_picture_3()
                assert picture_url == response_data2[tab2_rep_data_len + 2]['mainPic']
                self.step('断言第三页第四项新闻的图片')
                picture_url = new_page.get_news_picture_4()
                assert picture_url == response_data2[tab2_rep_data_len + 3]['mainPic']
                self.step('断言第三页第五项新闻的图片')
                picture_url = new_page.get_news_picture_5()
                assert picture_url == response_data2[tab2_rep_data_len + 4]['mainPic']
                self.step('断言第三页第一项新闻的作者及时间')
                name_time = new_page.get_news_source_name_1()
                assert name_time[0] == response_data2[tab2_rep_data_len]['sourceName'] and name_time[1] == \
                       response_data2[tab2_rep_data_len][
                           'newsTime']
                self.step('断言第三页第二项新闻的作者及时间')
                name_time = new_page.get_news_source_name_2()
                assert name_time[0] == response_data2[tab2_rep_data_len + 1]['sourceName'] and name_time[1] == \
                       response_data2[tab2_rep_data_len + 1]['newsTime']
                self.step('断言第三页第三项新闻的作者及时间')
                name_time = new_page.get_news_source_name_3()
                assert name_time[0] == response_data2[tab2_rep_data_len + 2]['sourceName'] and name_time[1] == \
                       response_data2[tab2_rep_data_len + 2]['newsTime']
                self.step('断言第三页第四项新闻的作者及时间')
                name_time = new_page.get_news_source_name_4()
                assert name_time[0] == response_data2[tab2_rep_data_len + 3]['sourceName'] and name_time[1] == \
                       response_data2[tab2_rep_data_len + 3]['newsTime']
                self.step('断言第三页第五项新闻的作者及时间')
                name_time = new_page.get_news_source_name_5()
                assert name_time[0] == response_data2[tab2_rep_data_len + 4]['sourceName'] and name_time[1] == \
                       response_data2[tab2_rep_data_len + 4]['newsTime']
                self.step('断言第三页第一项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_1()
                assert picture_url == response_data2[tab2_rep_data_len + 0]['accountImage']
                self.step('断言第三页第二项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_2()
                assert picture_url == response_data2[tab2_rep_data_len + 1]['accountImage']
                self.step('断言第三页第三项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_3()
                assert picture_url == response_data2[tab2_rep_data_len + 2]['accountImage']
                self.step('断言第三页第四项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_4()
                assert picture_url == response_data2[tab2_rep_data_len + 3]['accountImage']
                self.step('断言第三页第五项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_5()
                assert picture_url == response_data2[tab2_rep_data_len + 4]['accountImage']
                self.step('断言第三页第一项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(1)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab2_rep_data_len + 0]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab2_rep_data_len + 0]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab2_rep_data_len + 0]['relTickers'][0]['color']

                else:
                    assert len(text1) == 0 and response_data2[tab2_rep_data_len + 0]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab2_rep_data_len + 0]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab2_rep_data_len + 0]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab2_rep_data_len + 0]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab2_rep_data_len + 0]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    assert text3[0] == response_data2[tab2_rep_data_len + 0]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab2_rep_data_len + 0]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab2_rep_data_len + 0]['relTickers'][2]['color']
                else:

                    assert len(text3) == 0 and response_data2[tab2_rep_data_len + 0]['relTickers'][2][
                        'disSymbol'] is None

                self.step('断言第三页第二项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(2)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab2_rep_data_len + 1]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab2_rep_data_len + 1]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab2_rep_data_len + 1]['relTickers'][0]['color']
                else:
                    assert len(text1) == 0 and response_data2[tab2_rep_data_len + 1]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab2_rep_data_len + 1]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab2_rep_data_len + 1]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab2_rep_data_len + 1]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab2_rep_data_len + 1]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    assert text3[0] == response_data2[tab2_rep_data_len + 1]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab2_rep_data_len + 1]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab2_rep_data_len + 1]['relTickers'][2]['color']
                else:
                    assert len(text3) == 0 and response_data2[tab2_rep_data_len + 1]['relTickers'][2][
                        'disSymbol'] is None
                self.step('断言第三页第三项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(3)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab2_rep_data_len + 2]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab2_rep_data_len + 2]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab2_rep_data_len + 2]['relTickers'][0]['color']
                else:
                    assert len(text1) == 0 and response_data2[tab2_rep_data_len + 2]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab2_rep_data_len + 2]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab2_rep_data_len + 2]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab2_rep_data_len + 2]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab2_rep_data_len + 2]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    assert text3[0] == response_data2[tab2_rep_data_len + 2]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab2_rep_data_len + 2]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab2_rep_data_len + 2]['relTickers'][2]['color']
                else:
                    assert len(text3) == 0 and response_data2[tab2_rep_data_len + 2]['relTickers'][2][
                        'disSymbol'] is None

                self.step('断言第三页第四项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(4)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab2_rep_data_len + 3]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab2_rep_data_len + 3]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab2_rep_data_len + 3]['relTickers'][0]['color']
                else:
                    assert len(text1) == 0 and response_data2[tab2_rep_data_len + 3]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab2_rep_data_len + 3]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab2_rep_data_len + 3]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab2_rep_data_len + 3]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab2_rep_data_len + 3]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    assert text3[0] == response_data2[tab2_rep_data_len + 3]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab2_rep_data_len + 3]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab2_rep_data_len + 3]['relTickers'][2]['color']
                else:
                    print(response_data2[tab2_rep_data_len + 3]['relTickers'][2], text3)
                    assert len(text3) == 0 and response_data2[tab2_rep_data_len + 3]['relTickers'][2][
                        'disSymbol'] is None

                self.step('断言第三页第五项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(5)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab2_rep_data_len + 4]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab2_rep_data_len + 4]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab2_rep_data_len + 4]['relTickers'][0]['color']
                else:
                    assert len(text1) == 0 and response_data2[tab2_rep_data_len + 4]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab2_rep_data_len + 4]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab2_rep_data_len + 4]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab2_rep_data_len + 4]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab2_rep_data_len + 4]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    print(text3, response_data2[tab2_rep_data_len + 4]['relTickers'][2])
                    assert text3[0] == response_data2[tab2_rep_data_len + 4]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab2_rep_data_len + 4]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab2_rep_data_len + 4]['relTickers'][2]['color']
                else:

                    assert len(text3) == 0 and response_data2[tab2_rep_data_len + 4]['relTickers'][2][
                        'disSymbol'] is None

        tab3_req_data_len = len(request_data)
        tab3_rep_data_len = len(response_data2)

        if response_data1_len >= 4:
            self.step('切换列表至第四个tab')
            new_page.click_element_tab(4)
            new_page.waits()
            self.step('处理请求参数')
            request_data = new_page.extract_data_request(request)
            self.step('处理响应数据')
            response_data1, response_data2 = new_page.extract_data_response(response)
            if len(response_data2) == tab3_rep_data_len:
                self.step('判断第四页数据是否使用了接口返回的contentid')
                assert int(response_data1[3]['id']) == int(request_data[tab3_req_data_len]['contentId'])
                self.step('断言第二页第一项新闻的title')
                title = new_page.get_title_1()
                assert title is None
                self.step('断言第四页第二项新闻的title')
                title = new_page.get_title_2()
                assert title is None
                self.step('断言第四页第三项新闻的title')
                title = new_page.get_title_3()
                assert title is None
                self.step('断言第四页第四项新闻的title')
                title = new_page.get_title_4()
                assert title is None
                self.step('断言第四页第五项新闻的title')
                title = new_page.get_title_5()
                assert title is None
                self.step('断言第四页第一项新闻的图片')
                picture_url = new_page.get_news_picture_1()
                assert picture_url is None
                self.step('断言第四页第二项新闻的图片')
                picture_url = new_page.get_news_picture_2()
                assert picture_url is None
                self.step('断言第四页第三项新闻的图片')
                picture_url = new_page.get_news_picture_3()
                assert picture_url is None
                self.step('断言第四页第四项新闻的图片')
                picture_url = new_page.get_news_picture_4()
                assert picture_url is None
                self.step('断言第四页第五项新闻的图片')
                picture_url = new_page.get_news_picture_5()
                assert picture_url is None
                self.step('断言第四页第一项新闻的作者及时间')
                name_time = new_page.get_news_source_name_1()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第四页第二项新闻的作者及时间')
                name_time = new_page.get_news_source_name_2()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第四页第三项新闻的作者及时间')
                name_time = new_page.get_news_source_name_3()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第四页第四项新闻的作者及时间')
                name_time = new_page.get_news_source_name_4()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第四页第五项新闻的作者及时间')
                name_time = new_page.get_news_source_name_5()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第四页第一项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_1()
                assert picture_url is None
                self.step('断言第四页第二项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_2()
                assert picture_url is None
                self.step('断言第四页第三项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_3()
                assert picture_url is None
                self.step('断言第四页第四项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_4()
                assert picture_url is None
                self.step('断言第四页第五项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_5()
                assert picture_url is None
            else:

                self.step('判断第四页数据是否使用了接口返回的contentid')
                assert int(response_data1[3]['id']) == int(request_data[tab3_req_data_len]['contentId'])
                self.step('断言第四页第一项新闻的title')
                title = new_page.get_title_1()
                assert title == response_data2[tab3_rep_data_len]['title']
                self.step('断言第四页第二项新闻的title')
                title = new_page.get_title_2()
                assert title == response_data2[tab3_rep_data_len + 1]['title']
                self.step('断言第四页第三项新闻的title')
                title = new_page.get_title_3()
                assert title == response_data2[tab3_rep_data_len + 2]['title']
                self.step('断言第四页第四项新闻的title')
                title = new_page.get_title_4()
                assert title == response_data2[tab3_rep_data_len + 3]['title']
                self.step('断言第四页第五项新闻的title')
                title = new_page.get_title_5()
                assert title == response_data2[tab3_rep_data_len + 4]['title']
                self.step('断言第四页第一项新闻的图片')
                picture_url = new_page.get_news_picture_1()
                assert picture_url == response_data2[tab3_rep_data_len]['mainPic']
                self.step('断言第四页第二项新闻的图片')
                picture_url = new_page.get_news_picture_2()
                assert picture_url == response_data2[tab3_rep_data_len + 1]['mainPic']
                self.step('断言第四页第三项新闻的图片')
                picture_url = new_page.get_news_picture_3()
                assert picture_url == response_data2[tab3_rep_data_len + 2]['mainPic']
                self.step('断言第四页第四项新闻的图片')
                picture_url = new_page.get_news_picture_4()
                assert picture_url == response_data2[tab3_rep_data_len + 3]['mainPic']
                self.step('断言第四页第五项新闻的图片')
                picture_url = new_page.get_news_picture_5()
                assert picture_url == response_data2[tab3_rep_data_len + 4]['mainPic']
                self.step('断言第四页第一项新闻的作者及时间')
                name_time = new_page.get_news_source_name_1()
                assert name_time[0] == response_data2[tab3_rep_data_len]['sourceName'] and name_time[1] == \
                       response_data2[tab3_rep_data_len][
                           'newsTime']
                self.step('断言第四页第二项新闻的作者及时间')
                name_time = new_page.get_news_source_name_2()
                assert name_time[0] == response_data2[tab3_rep_data_len + 1]['sourceName'] and name_time[1] == \
                       response_data2[tab3_rep_data_len + 1]['newsTime']
                self.step('断言第四页第三项新闻的作者及时间')
                name_time = new_page.get_news_source_name_3()
                assert name_time[0] == response_data2[tab3_rep_data_len + 2]['sourceName'] and name_time[1] == \
                       response_data2[tab3_rep_data_len + 2]['newsTime']
                self.step('断言第四页第四项新闻的作者及时间')
                name_time = new_page.get_news_source_name_4()
                assert name_time[0] == response_data2[tab3_rep_data_len + 3]['sourceName'] and name_time[1] == \
                       response_data2[tab3_rep_data_len + 3]['newsTime']
                self.step('断言第四页第五项新闻的作者及时间')
                name_time = new_page.get_news_source_name_5()
                assert name_time[0] == response_data2[tab3_rep_data_len + 4]['sourceName'] and name_time[1] == \
                       response_data2[tab3_rep_data_len + 4]['newsTime']
                self.step('断言第四页第一项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_1()
                assert picture_url == response_data2[tab3_rep_data_len + 0]['accountImage']
                self.step('断言第四页第二项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_2()
                assert picture_url == response_data2[tab3_rep_data_len + 1]['accountImage']
                self.step('断言第四页第三项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_3()
                assert picture_url == response_data2[tab3_rep_data_len + 2]['accountImage']
                self.step('断言第四页第四项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_4()
                assert picture_url == response_data2[tab3_rep_data_len + 3]['accountImage']
                self.step('断言第四页第五项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_5()
                assert picture_url == response_data2[tab3_rep_data_len + 4]['accountImage']
                self.step('断言第四页第一项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(1)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab3_rep_data_len + 0]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab3_rep_data_len + 0]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab3_rep_data_len + 0]['relTickers'][0]['color']

                else:
                    assert len(text1) == 0 and response_data2[tab3_rep_data_len + 0]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab3_rep_data_len + 0]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab3_rep_data_len + 0]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab3_rep_data_len + 0]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab3_rep_data_len + 0]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    assert text3[0] == response_data2[tab3_rep_data_len + 0]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab3_rep_data_len + 0]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab3_rep_data_len + 0]['relTickers'][2]['color']
                else:

                    assert len(text3) == 0 and response_data2[tab3_rep_data_len + 0]['relTickers'][2][
                        'disSymbol'] is None

                self.step('断言第四页第二项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(2)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab3_rep_data_len + 1]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab3_rep_data_len + 1]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab3_rep_data_len + 1]['relTickers'][0]['color']
                else:
                    assert len(text1) == 0 and response_data2[tab3_rep_data_len + 1]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab3_rep_data_len + 1]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab3_rep_data_len + 1]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab3_rep_data_len + 1]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab3_rep_data_len + 1]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    assert text3[0] == response_data2[tab3_rep_data_len + 1]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab3_rep_data_len + 1]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab3_rep_data_len + 1]['relTickers'][2]['color']
                else:
                    assert len(text3) == 0 and response_data2[tab3_rep_data_len + 1]['relTickers'][2][
                        'disSymbol'] is None
                self.step('断言第四页第三项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(3)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab3_rep_data_len + 2]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab3_rep_data_len + 2]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab3_rep_data_len + 2]['relTickers'][0]['color']
                else:
                    assert len(text1) == 0 and response_data2[tab3_rep_data_len + 2]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab3_rep_data_len + 2]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab3_rep_data_len + 2]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab3_rep_data_len + 2]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab3_rep_data_len + 2]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    assert text3[0] == response_data2[tab3_rep_data_len + 2]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab3_rep_data_len + 2]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab3_rep_data_len + 2]['relTickers'][2]['color']
                else:
                    assert len(text3) == 0 and response_data2[tab3_rep_data_len + 2]['relTickers'][2][
                        'disSymbol'] is None

                self.step('断言第四页第四项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(4)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab3_rep_data_len + 3]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab3_rep_data_len + 3]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab3_rep_data_len + 3]['relTickers'][0]['color']
                else:
                    assert len(text1) == 0 and response_data2[tab3_rep_data_len + 3]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab3_rep_data_len + 3]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab3_rep_data_len + 3]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab3_rep_data_len + 3]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab3_rep_data_len + 3]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    assert text3[0] == response_data2[tab3_rep_data_len + 3]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab3_rep_data_len + 3]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab3_rep_data_len + 3]['relTickers'][2]['color']
                else:
                    print(response_data2[tab3_rep_data_len + 3]['relTickers'][2], text3)
                    assert len(text3) == 0 and response_data2[tab3_rep_data_len + 3]['relTickers'][2][
                        'disSymbol'] is None

                self.step('断言第四页第五项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(5)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab3_rep_data_len + 4]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab3_rep_data_len + 4]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab3_rep_data_len + 4]['relTickers'][0]['color']
                else:
                    assert len(text1) == 0 and response_data2[tab3_rep_data_len + 4]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab3_rep_data_len + 4]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab3_rep_data_len + 4]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab3_rep_data_len + 4]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab3_rep_data_len + 4]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    print(text3, response_data2[tab3_rep_data_len + 4]['relTickers'][2])
                    assert text3[0] == response_data2[tab3_rep_data_len + 4]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab3_rep_data_len + 4]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab3_rep_data_len + 4]['relTickers'][2]['color']
                else:

                    assert len(text3) == 0 and response_data2[tab3_rep_data_len + 4]['relTickers'][2][
                        'disSymbol'] is None

        tab4_req_data_len = len(request_data)
        tab4_rep_data_len = len(response_data2)

        if response_data1_len >= 5:
            self.step('切换列表至第五个tab')
            new_page.click_element_tab(5)
            new_page.waits()
            self.step('处理请求参数')
            request_data = new_page.extract_data_request(request)
            self.step('处理响应数据')
            response_data1, response_data2 = new_page.extract_data_response(response)
            if len(response_data2) == tab4_rep_data_len:
                self.step('判断第五页数据是否使用了接口返回的contentid')
                assert int(response_data1[4]['id']) == int(request_data[tab4_req_data_len]['contentId'])
                self.step('断言第五页第一项新闻的title')
                title = new_page.get_title_1()
                assert title is None
                self.step('断言第五页第二项新闻的title')
                title = new_page.get_title_2()
                assert title is None
                self.step('断言第五页第三项新闻的title')
                title = new_page.get_title_3()
                assert title is None
                self.step('断言第五页第四项新闻的title')
                title = new_page.get_title_4()
                assert title is None
                self.step('断言第五页第五项新闻的title')
                title = new_page.get_title_5()
                assert title is None
                self.step('断言第五页第一项新闻的图片')
                picture_url = new_page.get_news_picture_1()
                assert picture_url is None
                self.step('断言第五页第二项新闻的图片')
                picture_url = new_page.get_news_picture_2()
                assert picture_url is None
                self.step('五页第五项新闻的图片')
                picture_url = new_page.get_news_picture_3()
                assert picture_url is None
                self.step('断言第五页第四项新闻的图片')
                picture_url = new_page.get_news_picture_4()
                assert picture_url is None
                self.step('断言第五页第五项新闻的图片')
                picture_url = new_page.get_news_picture_5()
                assert picture_url is None
                self.step('断言第五页第一项新闻的作者及时间')
                name_time = new_page.get_news_source_name_1()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第五页第二项新闻的作者及时间')
                name_time = new_page.get_news_source_name_2()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第五页第三项新闻的作者及时间')
                name_time = new_page.get_news_source_name_3()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第五页第四项新闻的作者及时间')
                name_time = new_page.get_news_source_name_4()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第五页第五项新闻的作者及时间')
                name_time = new_page.get_news_source_name_5()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第五页第一项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_1()
                assert picture_url is None
                self.step('断言第五页第二项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_2()
                assert picture_url is None
                self.step('断言第五页第三项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_3()
                assert picture_url is None
                self.step('断言第五页第四项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_4()
                assert picture_url is None
                self.step('断言第五页第五项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_5()
                assert picture_url is None
            else:
                self.step('判断第五页数据是否使用了接口返回的contentid')
                assert int(response_data1[4]['id']) == int(request_data[tab4_req_data_len]['contentId'])
                self.step('断言第五页第一项新闻的title')
                title = new_page.get_title_1()
                assert title == response_data2[tab4_rep_data_len]['title']
                self.step('断言第五页第二项新闻的title')
                title = new_page.get_title_2()
                assert title == response_data2[tab4_rep_data_len + 1]['title']
                self.step('断言第五页第三项新闻的title')
                title = new_page.get_title_3()
                assert title == response_data2[tab4_rep_data_len + 2]['title']
                self.step('断言第五页第四项新闻的title')
                title = new_page.get_title_4()
                assert title == response_data2[tab4_rep_data_len + 3]['title']
                self.step('断言第五页第五项新闻的title')
                title = new_page.get_title_5()
                assert title == response_data2[tab4_rep_data_len + 4]['title']
                self.step('断言第五页第一项新闻的图片')
                picture_url = new_page.get_news_picture_1()
                assert picture_url == response_data2[tab4_rep_data_len]['mainPic']
                self.step('断言第五页第二项新闻的图片')
                picture_url = new_page.get_news_picture_2()
                assert picture_url == response_data2[tab4_rep_data_len + 1]['mainPic']
                self.step('断言第五页第三项新闻的图片')
                picture_url = new_page.get_news_picture_3()
                assert picture_url == response_data2[tab4_rep_data_len + 2]['mainPic']
                self.step('断言第五页第四项新闻的图片')
                picture_url = new_page.get_news_picture_4()
                assert picture_url == response_data2[tab4_rep_data_len + 3]['mainPic']
                self.step('断言第五页第五项新闻的图片')
                picture_url = new_page.get_news_picture_5()
                assert picture_url == response_data2[tab4_rep_data_len + 4]['mainPic']
                self.step('断言第五页第一项新闻的作者及时间')
                name_time = new_page.get_news_source_name_1()
                assert name_time[0] == response_data2[tab4_rep_data_len]['sourceName'] and name_time[1] == \
                       response_data2[tab4_rep_data_len][
                           'newsTime']
                self.step('断言第五页第二项新闻的作者及时间')
                name_time = new_page.get_news_source_name_2()
                assert name_time[0] == response_data2[tab4_rep_data_len + 1]['sourceName'] and name_time[1] == \
                       response_data2[tab4_rep_data_len + 1]['newsTime']
                self.step('断言第五页第三项新闻的作者及时间')
                name_time = new_page.get_news_source_name_3()
                assert name_time[0] == response_data2[tab4_rep_data_len + 2]['sourceName'] and name_time[1] == \
                       response_data2[tab4_rep_data_len + 2]['newsTime']
                self.step('断言第五页第四项新闻的作者及时间')
                name_time = new_page.get_news_source_name_4()
                assert name_time[0] == response_data2[tab4_rep_data_len + 3]['sourceName'] and name_time[1] == \
                       response_data2[tab4_rep_data_len + 3]['newsTime']
                self.step('断言第五页第五项新闻的作者及时间')
                name_time = new_page.get_news_source_name_5()
                assert name_time[0] == response_data2[tab4_rep_data_len + 4]['sourceName'] and name_time[1] == \
                       response_data2[tab4_rep_data_len + 4]['newsTime']
                self.step('断言第五页第一项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_1()
                assert picture_url == response_data2[tab4_rep_data_len + 0]['accountImage']
                self.step('断言第五页第二项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_2()
                assert picture_url == response_data2[tab4_rep_data_len + 1]['accountImage']
                self.step('断言第五页第三项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_3()
                assert picture_url == response_data2[tab4_rep_data_len + 2]['accountImage']
                self.step('断言第五页第四项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_4()
                assert picture_url == response_data2[tab4_rep_data_len + 3]['accountImage']
                self.step('断言第五页第五项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_5()
                assert picture_url == response_data2[tab4_rep_data_len + 4]['accountImage']
                self.step('断言第五页第一项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(1)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab4_rep_data_len + 0]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab4_rep_data_len + 0]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab4_rep_data_len + 0]['relTickers'][0]['color']

                else:
                    assert len(text1) == 0 and response_data2[tab4_rep_data_len + 0]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab4_rep_data_len + 0]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab4_rep_data_len + 0]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab4_rep_data_len + 0]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab4_rep_data_len + 0]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    assert text3[0] == response_data2[tab4_rep_data_len + 0]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab4_rep_data_len + 0]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab4_rep_data_len + 0]['relTickers'][2]['color']
                else:

                    assert len(text3) == 0 and response_data2[tab4_rep_data_len + 0]['relTickers'][2][
                        'disSymbol'] is None

                self.step('断言第五页第二项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(2)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab4_rep_data_len + 1]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab4_rep_data_len + 1]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab4_rep_data_len + 1]['relTickers'][0]['color']
                else:
                    assert len(text1) == 0 and response_data2[tab4_rep_data_len + 1]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab4_rep_data_len + 1]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab4_rep_data_len + 1]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab4_rep_data_len + 1]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab4_rep_data_len + 1]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    assert text3[0] == response_data2[tab4_rep_data_len + 1]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab4_rep_data_len + 1]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab4_rep_data_len + 1]['relTickers'][2]['color']
                else:
                    assert len(text3) == 0 and response_data2[tab4_rep_data_len + 1]['relTickers'][2][
                        'disSymbol'] is None
                self.step('断言第五页第三项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(3)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab4_rep_data_len + 2]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab4_rep_data_len + 2]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab4_rep_data_len + 2]['relTickers'][0]['color']
                else:
                    assert len(text1) == 0 and response_data2[tab4_rep_data_len + 2]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab4_rep_data_len + 2]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab4_rep_data_len + 2]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab4_rep_data_len + 2]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab4_rep_data_len + 2]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    assert text3[0] == response_data2[tab4_rep_data_len + 2]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab4_rep_data_len + 2]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab4_rep_data_len + 2]['relTickers'][2]['color']
                else:
                    assert len(text3) == 0 and response_data2[tab4_rep_data_len + 2]['relTickers'][2][
                        'disSymbol'] is None

                self.step('断言第五页第四项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(4)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab4_rep_data_len + 3]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab4_rep_data_len + 3]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab4_rep_data_len + 3]['relTickers'][0]['color']
                else:
                    assert len(text1) == 0 and response_data2[tab4_rep_data_len + 3]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab4_rep_data_len + 3]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab4_rep_data_len + 3]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab4_rep_data_len + 3]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab4_rep_data_len + 3]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    assert text3[0] == response_data2[tab4_rep_data_len + 3]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab4_rep_data_len + 3]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab4_rep_data_len + 3]['relTickers'][2]['color']
                else:
                    print(response_data2[tab4_rep_data_len + 3]['relTickers'][2], text3)
                    assert len(text3) == 0 and response_data2[tab4_rep_data_len + 3]['relTickers'][2][
                        'disSymbol'] is None

                self.step('断言第五页第五项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(5)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab4_rep_data_len + 4]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab4_rep_data_len + 4]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab4_rep_data_len + 4]['relTickers'][0]['color']
                else:
                    assert len(text1) == 0 and response_data2[tab4_rep_data_len + 4]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab4_rep_data_len + 4]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab4_rep_data_len + 4]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab4_rep_data_len + 4]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab4_rep_data_len + 4]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    print(text3, response_data2[tab4_rep_data_len + 4]['relTickers'][2])
                    assert text3[0] == response_data2[tab4_rep_data_len + 4]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab4_rep_data_len + 4]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab4_rep_data_len + 4]['relTickers'][2]['color']
                else:

                    assert len(text3) == 0 and response_data2[tab4_rep_data_len + 4]['relTickers'][2][
                        'disSymbol'] is None

        tab5_req_data_len = len(request_data)
        tab5_rep_data_len = len(response_data2)

        if response_data1_len >= 6:
            self.step('切换列表至第六个tab')
            new_page.click_element_tab(6)
            new_page.waits()
            self.step('处理请求参数')
            request_data = new_page.extract_data_request(request)
            self.step('处理响应数据')
            response_data1, response_data2 = new_page.extract_data_response(response)
            if len(response_data2) == tab5_rep_data_len:
                self.step('判断第六页数据是否使用了接口返回的contentid')
                assert int(response_data1[5]['id']) == int(request_data[tab5_req_data_len]['contentId'])
                self.step('断言第六页第一项新闻的title')
                title = new_page.get_title_1()
                assert title is None
                self.step('断言第六页第二项新闻的title')
                title = new_page.get_title_2()
                assert title is None
                self.step('断言第六页第三项新闻的title')
                title = new_page.get_title_3()
                assert title is None
                self.step('断言第六页第四项新闻的title')
                title = new_page.get_title_4()
                assert title is None
                self.step('断言第六页第五项新闻的title')
                title = new_page.get_title_5()
                assert title is None
                self.step('断言第六页第一项新闻的图片')
                picture_url = new_page.get_news_picture_1()
                assert picture_url is None
                self.step('断言第六页第二项新闻的图片')
                picture_url = new_page.get_news_picture_2()
                assert picture_url is None
                self.step('断言第六页第三项新闻的图片')
                picture_url = new_page.get_news_picture_3()
                assert picture_url is None
                self.step('断言第六页第四项新闻的图片')
                picture_url = new_page.get_news_picture_4()
                assert picture_url is None
                self.step('断言第六页第五项新闻的图片')
                picture_url = new_page.get_news_picture_5()
                assert picture_url is None
                self.step('断言第六页第一项新闻的作者及时间')
                name_time = new_page.get_news_source_name_1()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第六页第二项新闻的作者及时间')
                name_time = new_page.get_news_source_name_2()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第六页第三项新闻的作者及时间')
                name_time = new_page.get_news_source_name_3()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第六页第四项新闻的作者及时间')
                name_time = new_page.get_news_source_name_4()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第六页第五项新闻的作者及时间')
                name_time = new_page.get_news_source_name_5()
                assert name_time[0] is None and name_time[1] is None
                self.step('断言第六页第一项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_1()
                assert picture_url is None
                self.step('断言第六页第二项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_2()
                assert picture_url is None
                self.step('断言第六页第三项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_3()
                assert picture_url is None
                self.step('断言第六页第四项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_4()
                assert picture_url is None
                self.step('断言第六页第五项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_5()
                assert picture_url is None
            else:
                self.step('判断第六页数据是否使用了接口返回的contentid')
                assert int(response_data1[5]['id']) == int(request_data[tab5_req_data_len]['contentId'])
                self.step('断言第六页第一项新闻的title')
                title = new_page.get_title_1()
                assert title == response_data2[tab5_rep_data_len]['title']
                self.step('断言第六页第二项新闻的title')
                title = new_page.get_title_2()
                assert title == response_data2[tab5_rep_data_len + 1]['title']
                self.step('断言第六页第三项新闻的title')
                title = new_page.get_title_3()
                assert title == response_data2[tab5_rep_data_len + 2]['title']
                self.step('断言第六页第四项新闻的title')
                title = new_page.get_title_4()
                assert title == response_data2[tab5_rep_data_len + 3]['title']
                self.step('断言第六页第五项新闻的title')
                title = new_page.get_title_5()
                assert title == response_data2[tab5_rep_data_len + 4]['title']
                self.step('断言第六页第一项新闻的图片')
                picture_url = new_page.get_news_picture_1()
                assert picture_url == response_data2[tab5_rep_data_len]['mainPic']
                self.step('断言第六页第二项新闻的图片')
                picture_url = new_page.get_news_picture_2()
                assert picture_url == response_data2[tab5_rep_data_len + 1]['mainPic']
                self.step('断言第六页第三项新闻的图片')
                picture_url = new_page.get_news_picture_3()
                assert picture_url == response_data2[tab5_rep_data_len + 2]['mainPic']
                self.step('断言第六页第四项新闻的图片')
                picture_url = new_page.get_news_picture_4()
                assert picture_url == response_data2[tab5_rep_data_len + 3]['mainPic']
                self.step('断言第六页第五项新闻的图片')
                picture_url = new_page.get_news_picture_5()
                assert picture_url == response_data2[tab5_rep_data_len + 4]['mainPic']
                self.step('断言第六页第一项新闻的作者及时间')
                name_time = new_page.get_news_source_name_1()
                assert name_time[0] == response_data2[tab5_rep_data_len]['sourceName'] and name_time[1] == \
                       response_data2[tab5_rep_data_len][
                           'newsTime']
                self.step('断言第六页第二项新闻的作者及时间')
                name_time = new_page.get_news_source_name_2()
                assert name_time[0] == response_data2[tab5_rep_data_len + 1]['sourceName'] and name_time[1] == \
                       response_data2[tab5_rep_data_len + 1]['newsTime']
                self.step('断言第六页第三项新闻的作者及时间')
                name_time = new_page.get_news_source_name_3()
                assert name_time[0] == response_data2[tab5_rep_data_len + 2]['sourceName'] and name_time[1] == \
                       response_data2[tab5_rep_data_len + 2]['newsTime']
                self.step('断言第六页第四项新闻的作者及时间')
                name_time = new_page.get_news_source_name_4()
                assert name_time[0] == response_data2[tab5_rep_data_len + 3]['sourceName'] and name_time[1] == \
                       response_data2[tab5_rep_data_len + 3]['newsTime']
                self.step('断言第六页第五项新闻的作者及时间')
                name_time = new_page.get_news_source_name_5()
                assert name_time[0] == response_data2[tab5_rep_data_len + 4]['sourceName'] and name_time[1] == \
                       response_data2[tab5_rep_data_len + 4]['newsTime']
                self.step('断言第六页第一项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_1()
                assert picture_url == response_data2[tab5_rep_data_len + 0]['accountImage']
                self.step('断言第六页第二项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_2()
                assert picture_url == response_data2[tab5_rep_data_len + 1]['accountImage']
                self.step('断言第六页第三项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_3()
                assert picture_url == response_data2[tab5_rep_data_len + 2]['accountImage']
                self.step('断言第六页第四项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_4()
                assert picture_url == response_data2[tab5_rep_data_len + 3]['accountImage']
                self.step('断言第六页第五项新闻的作者图片')
                picture_url = new_page.get_news_name_picture_5()
                assert picture_url == response_data2[tab5_rep_data_len + 4]['accountImage']
                self.step('断言第六页第一项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(1)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab5_rep_data_len + 0]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab5_rep_data_len + 0]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab5_rep_data_len + 0]['relTickers'][0]['color']

                else:
                    assert len(text1) == 0 and response_data2[tab5_rep_data_len + 0]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab5_rep_data_len + 0]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab5_rep_data_len + 0]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab5_rep_data_len + 0]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab5_rep_data_len + 0]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    assert text3[0] == response_data2[tab5_rep_data_len + 0]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab5_rep_data_len + 0]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab5_rep_data_len + 0]['relTickers'][2]['color']
                else:

                    assert len(text3) == 0 and response_data2[tab5_rep_data_len + 0]['relTickers'][2][
                        'disSymbol'] is None

                self.step('断言第六页第二项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(2)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab5_rep_data_len + 1]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab5_rep_data_len + 1]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab5_rep_data_len + 1]['relTickers'][0]['color']
                else:
                    assert len(text1) == 0 and response_data2[tab5_rep_data_len + 1]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab5_rep_data_len + 1]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab5_rep_data_len + 1]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab5_rep_data_len + 1]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab5_rep_data_len + 1]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    assert text3[0] == response_data2[tab5_rep_data_len + 1]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab5_rep_data_len + 1]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab5_rep_data_len + 1]['relTickers'][2]['color']
                else:
                    assert len(text3) == 0 and response_data2[tab5_rep_data_len + 1]['relTickers'][2][
                        'disSymbol'] is None
                self.step('断言第六页第三项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(3)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab5_rep_data_len + 2]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab5_rep_data_len + 2]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab5_rep_data_len + 2]['relTickers'][0]['color']
                else:
                    assert len(text1) == 0 and response_data2[tab5_rep_data_len + 2]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab5_rep_data_len + 2]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab5_rep_data_len + 2]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab5_rep_data_len + 2]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab5_rep_data_len + 2]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    assert text3[0] == response_data2[tab5_rep_data_len + 2]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab5_rep_data_len + 2]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab5_rep_data_len + 2]['relTickers'][2]['color']
                else:
                    assert len(text3) == 0 and response_data2[tab5_rep_data_len + 2]['relTickers'][2][
                        'disSymbol'] is None

                self.step('断言第六页第四项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(4)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab5_rep_data_len + 3]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab5_rep_data_len + 3]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab5_rep_data_len + 3]['relTickers'][0]['color']
                else:
                    assert len(text1) == 0 and response_data2[tab5_rep_data_len + 3]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab5_rep_data_len + 3]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab5_rep_data_len + 3]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab5_rep_data_len + 3]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab5_rep_data_len + 3]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    assert text3[0] == response_data2[tab5_rep_data_len + 3]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab5_rep_data_len + 3]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab5_rep_data_len + 3]['relTickers'][2]['color']
                else:
                    print(response_data2[tab5_rep_data_len + 3]['relTickers'][2], text3)
                    assert len(text3) == 0 and response_data2[tab5_rep_data_len + 3]['relTickers'][2][
                        'disSymbol'] is None

                self.step('断言第六页第五项changeRatio和disSymbol字段')
                text1, text2, text3 = new_page.get_title_symbol_ratio(5)
                if len(text1) >= 2:
                    assert text1[0] == response_data2[tab5_rep_data_len + 4]['relTickers'][0]['disSymbol'] and text1[
                        1] == \
                           response_data2[tab5_rep_data_len + 4]['relTickers'][0]['changeRatio'] and text1[2] == \
                           response_data2[tab5_rep_data_len + 4]['relTickers'][0]['color']
                else:
                    assert len(text1) == 0 and response_data2[tab5_rep_data_len + 4]['relTickers'][0][
                        'disSymbol'] is None

                if len(text2) >= 2:
                    assert text2[0] == response_data2[tab5_rep_data_len + 4]['relTickers'][1]['disSymbol'] and text2[
                        1] == \
                           response_data2[tab5_rep_data_len + 4]['relTickers'][1]['changeRatio'] and text2[2] == \
                           response_data2[tab5_rep_data_len + 4]['relTickers'][1]['color']
                else:
                    assert len(text2) == 0 and response_data2[tab5_rep_data_len + 4]['relTickers'][1][
                        'disSymbol'] is None

                if len(text3) >= 2:
                    print(text3, response_data2[tab5_rep_data_len + 4]['relTickers'][2])
                    assert text3[0] == response_data2[tab5_rep_data_len + 4]['relTickers'][2]['disSymbol'] and text3[
                        1] == \
                           response_data2[tab5_rep_data_len + 4]['relTickers'][2]['changeRatio'] and text3[2] == \
                           response_data2[tab5_rep_data_len + 4]['relTickers'][2]['color']
                else:

                    assert len(text3) == 0 and response_data2[tab5_rep_data_len + 4]['relTickers'][2][
                        'disSymbol'] is None
