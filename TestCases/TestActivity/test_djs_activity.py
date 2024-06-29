import allure

from Pages.PageActivity.page_djs_activity import DjsPage
from Utils.Log import Msg

global new_page


class TestDjsActivity:

    def step(self, msg=''):
        self.log.info(msg)
        return allure.step(msg)

    def test_less_than_48_00(self, base_page):
        self.log = Msg('未满48小时入场弹窗')
        global new_page
        new_page = DjsPage(base_page, self.log)
        new_page.get_token()
        with self.step("步骤一：初始化数据"):
            new_page.initialization_data()
            new_page.waits()
        with self.step("步骤二：打开活动链接"):
            new_page.open_url_()
        with self.step("步骤三：查找并断言入场弹窗"):
            ruchangtc = new_page.wait_for_selector_01()
        assert ruchangtc is not None

    def test_less_than_48_01(self):
        self.log = Msg('未满48小时主页面倒计时展示')
        with self.step("步骤一：断言未报名主页面的'happy'组件"):
            new_page.click_element_01()
            happy = new_page.wait_for_selector_02()
        assert happy is not None

    def test_less_than_48_02(self):
        self.log = Msg('未满48小时HOW TO页面倒计时展示')
        with self.step("步骤一：断言未报名HOW TO页面的倒计时组件"):
            new_page.click_element_02()
            djs = new_page.wait_for_selector_03()
        assert djs[0] and djs[1] and djs[2] is not None

    def test_less_than_48_03(self):
        self.log = Msg('未满48小时HOW TO人物头像图标')
        with self.step("步骤一：断言人物头像"):
            avatar = new_page.wait_for_selector_04()
        assert avatar is not None

    def test_less_than_48_10(self):
        self.log = Msg('未满48小时报名后弹窗')
        with self.step("步骤一：点击报名+断言报名后的倒计时弹窗"):
            new_page.page.reload()
            new_page.click_element_03()
            djstc = new_page.wait_for_selector_05()
        assert djstc is not None

    def test_less_than_48_11(self):
        self.log = Msg('未满48小时报名后弹窗中的倒计时')
        with self.step("步骤一：断言报名后弹窗中的倒计时"):
            djs_time = new_page.get_text_01()
        assert 133080 <= djs_time <= 133200

    def test_less_than_48_12(self):
        self.log = Msg('未满48小时报名后弹窗中的倒计时')
        with self.step('步骤一：断言报名后主页中的倒计时'):
            new_page.click_element_04()
            djs_time = new_page.get_text_02()
        assert 133080 <= djs_time <= 133200

    def test_less_than_48_13(self):
        self.log = Msg('未满48小时报名后HOW TO人物头像图标')
        with self.step("步骤一：断言人物头像"):
            new_page.click_element_05()
            new_page.waits()
            avatar = new_page.wait_for_selector_06()
        assert avatar is not None

    def test_less_than_48_14(self):
        self.log = Msg('未满48小时报名后HOW TO中的倒计时')
        with self.step('步骤一：断言报名后HOW TO中的倒计时'):
            djs_time = new_page.get_text_03()
        assert 133080 <= djs_time <= 133200

    def test_less_than_48_15(self):
        self.log = Msg('未满48小时报名后HOW TO人数文案')
        with self.step("步骤一：断言人数文案"):
            quantity = new_page.get_text_04()
        assert quantity == '0/1'

    def test_less_than_48_16(self):
        self.log = Msg('未满48小时报名后Cash弹窗的人数文案')
        with self.step("步骤一：断言Cash弹窗的人数文案"):
            new_page.click_element_06()
            new_page.waits()
            new_page.click_element_07()
            text = new_page.get_text_05()
        assert text == '0/1'

    def test_less_than_48_17(self):
        self.log = Msg('未满48小时报名后Cash弹窗中的倒计时')
        with self.step('步骤一：断言报名后Cash弹窗中的倒计时'):
            djs_time = new_page.get_text_06()
        assert 133080 <= djs_time <= 133200

    def test_less_than_48_18(self):
        self.log = Msg('未满48小时报名后入场弹窗的人数文案')
        with self.step("步骤一：断言入场弹窗的人数文案"):
            new_page.page.reload()
            text = new_page.get_text_07()
        assert text == '0/1'

    def test_less_than_48_19(self):
        self.log = Msg('未满48小时报名后入场弹窗中的倒计时')
        with self.step('步骤一：断言报名后入场弹窗中的倒计时'):
            djs_time = new_page.get_text_08()
        assert 133080 <= djs_time <= 133200

    def test_less_than_48_110(self):
        self.log = Msg('未满48小时报名后抽奖按钮弹窗的人数文案')
        with self.step("步骤一：断言抽奖按钮弹窗的人数文案"):
            new_page.click_element_08()
            new_page.click_element_09()
            text = new_page.get_text_09()
        assert text == '0/1'

    def test_less_than_48_111(self):
        self.log = Msg('未满48小时报名后抽奖按钮弹窗中的倒计时')
        with self.step('步骤一：断言报名后抽奖按钮弹窗中的倒计时'):
            djs_time = new_page.get_text_10()
        assert 133080 <= djs_time <= 133200

    def test_less_than_48_20(self):
        self.log = Msg('未满48小时报名+邀请注册后的入场弹窗')
        with self.step('步骤一：断言报名+邀请注册后的入场弹窗'):
            new_page.simulation_steps_2()
            new_page.waits()
            new_page.page.reload()
            tc = new_page.wait_for_selector_07()
        assert tc is not None

    def test_less_than_48_21(self):
        self.log = Msg('未满48小时报名+邀请注册后的HOW TO页面')
        with self.step('步骤一：断言报名+邀请注册后的HOW TO页面'):
            new_page.click_element_10()
            new_page.click_element_11()
            tc = new_page.wait_for_selector_08()
        assert tc is not None

    def test_less_than_48_22(self):
        self.log = Msg('未满48小时报名+邀请注册后的Cash弹窗')
        with self.step('步骤一：断言报名+邀请注册后的Cash弹窗'):
            new_page.waits()
            new_page.click_element_12()
            new_page.waits()
            new_page.click_element_13()
            tc = new_page.wait_for_selector_09()
        assert tc is not None

    def test_less_than_48_31(self):
        self.log = Msg('未满48小时报名+邀请注册+入金后的How To')
        with self.step('步骤一：断言报名+邀请注册+入金后How To中的人物头像'):
            new_page.simulation_steps_3()
            new_page.waits()
            new_page.page.reload()
            new_page.click_element_14()
            tc = new_page.wait_for_selector_10()
        assert tc is not None

    def test_less_than_48_32(self):
        self.log = Msg('未满48小时报名+邀请注册+入金后的cash弹窗')
        with self.step('步骤一：断言报名+邀请注册+入金后cash弹窗'):
            new_page.waits()
            new_page.click_element_15()
            new_page.waits()
            new_page.click_element_16()
            tc = new_page.wait_for_selector_11()
        assert tc is not None

    def test_less_than_48_33(self):
        self.log = Msg('未满48小时获得奖励抽奖')
        with self.step('步骤一：断言获奖弹窗'):
            new_page.simulation_steps_4()
            new_page.click_element_17()
            new_page.click_element_18()
            tc = new_page.wait_for_selector_12
        assert tc is not None

    #   超过48小时的活动步骤

    def test_more_than_48_00(self, base_page):
        self.log = Msg('超过48小时入场弹窗')
        with self.step("步骤一：初始化数据+断言入场弹窗"):
            new_page.initialization_data_48()
            new_page.waits()
            new_page.page.reload()
            ruchangtc = new_page.wait_for_selector_13()
        assert ruchangtc is not None

    def test_more_than_48_01(self):
        self.log = Msg('超过48小时主页面倒计时展示')
        with self.step("步骤一：断言未报名主页面的'48：00:00'组件"):
            new_page.click_element_19()
            h_48 = new_page.wait_for_selector_14()
        assert h_48 is not None

    def test_more_than_48_02(self):
        self.log = Msg('超过48小时HOW TO页面倒计时展示')
        with self.step("步骤一：断言未报名HOW TO页面的倒计时组件"):
            new_page.click_element_20()
            result = new_page.get_text_11()
        assert result[0] == '48' and result[1] == '00' and result[2] == '00'

    def test_more_than_48_03(self):
        self.log = Msg('超过48小时HOW TO人物头像图标')
        with self.step("步骤一：断言人物头像"):
            avatar = new_page.wait_for_selector_15()
        assert avatar is not None

    def test_more_than_48_04(self):
        self.log = Msg('超过48小时HOW TO人数')
        with self.step("步骤一：断言邀请人数"):
            avatar = new_page.get_text_12()
        assert avatar == '0/1'

    def test_more_than_48_10(self):
        self.log = Msg('超过48小时报名后弹窗')
        with self.step("步骤一：点击报名+断言报名后的倒计时弹窗"):
            new_page.page.reload()
            new_page.click_element_21()
            djstc = new_page.wait_for_selector_16()
        assert djstc is not None

    def test_more_than_48_11(self):
        self.log = Msg('超过48小时报名后弹窗中的倒计时')
        with self.step("步骤一：断言报名后弹窗中的倒计时"):
            djs_time1 = new_page.get_text_13()
        assert 172740 <= djs_time1 <= 172800

    def test_more_than_48_12(self):
        self.log = Msg('超过48小时报名后弹窗中的倒计时')
        with self.step('步骤一：断言报名后主页中的倒计时'):
            new_page.click_element_22()
            djs_time2 = new_page.get_text_14()
        assert 172740 <= djs_time2 <= 172800

    def test_more_than_48_13(self):
        self.log = Msg('超过48小时报名后HOW TO人物头像图标')
        with self.step("步骤一：断言人物头像"):
            new_page.click_element_23()
            avatar = new_page.wait_for_selector_17()
        assert avatar is not None

    def test_more_than_48_14(self):
        self.log = Msg('未满48小时报名后HOW TO中的倒计时')
        with self.step('步骤一：断言报名后HOW TO中的倒计时'):
            djs_time3 = new_page.get_text_15()
        assert 172740 <= djs_time3 <= 172800

    def test_more_than_48_15(self):
        self.log = Msg('超过48小时报名后HOW TO人数文案')
        with self.step("步骤一：断言人数文案"):
            quantity = new_page.get_text_16()
        assert quantity == '0/1'

    def test_more_than_48_16(self):
        self.log = Msg('超过48小时报名后Cash弹窗的人数文案')
        with self.step("步骤一：断言Cash弹窗的人数文案"):
            new_page.waits()
            new_page.click_element_24()
            new_page.waits()
            new_page.click_element_25()
            text = new_page.get_text_17()
        assert text == '0/1'

    def test_more_than_48_17(self):
        self.log = Msg('超过48小时报名后Cash弹窗中的倒计时')
        with self.step('步骤一：断言报名后Cash弹窗中的倒计时'):
            djs_time4 = new_page.get_text_18()
        assert 172740 <= djs_time4 <= 172800

    def test_more_than_48_18(self):
        self.log = Msg('超过48小时报名后入场弹窗的人数文案')
        with self.step("步骤一：断言入场弹窗的人数文案"):
            new_page.page.reload()
            text = new_page.get_text_19()
        assert text == '0/1'

    def test_more_than_48_19(self):
        self.log = Msg('超过48小时报名后入场弹窗中的倒计时')
        with self.step('步骤一：断言报名后入场弹窗中的倒计时'):
            djs_time5 = new_page.get_text_20()
        assert 172740 <= djs_time5 <= 172800

    def test_more_than_48_110(self):
        self.log = Msg('超过48小时报名后抽奖按钮弹窗的人数文案')
        with self.step("步骤一：断言抽奖按钮弹窗的人数文案"):
            new_page.click_element_26()
            new_page.click_element_27()
            text = new_page.get_text_21()
        assert text == '0/1'

    def test_more_than_48_111(self):
        self.log = Msg('超过48小时报名后抽奖按钮弹窗中的倒计时')
        with self.step('步骤一：断言报名后抽奖按钮弹窗中的倒计时'):
            djs_time6 = new_page.get_text_22()
        assert 172740 <= djs_time6 <= 172800

    def test_more_than_48_20(self):
        self.log = Msg('超过48小时报名+邀请注册后的入场弹窗')
        with self.step('步骤一：断言报名+邀请注册后的入场弹窗'):
            new_page.simulation_steps_2()
            new_page.waits()
            new_page.page.reload()
            tc = new_page.wait_for_selector_18()
        assert tc is not None

    def test_more_than_48_21(self):
        self.log = Msg('超过48小时报名+邀请注册后的HOW TO页面')
        with self.step('步骤一：断言报名+邀请注册后的HOW TO页面'):
            new_page.click_element_28()
            new_page.click_element_29()
            tc = new_page.wait_for_selector_19()
        assert tc is not None

    def test_more_than_48_22(self):
        self.log = Msg('超过48小时报名+邀请注册后的Cash弹窗')
        with self.step('步骤一：断言报名+邀请注册后的Cash弹窗'):
            new_page.waits()
            new_page.click_element_30()
            new_page.waits()
            new_page.click_element_31()
            tc = new_page.wait_for_selector_20()
        assert tc is not None

    def test_more_than_48_31(self):
        self.log = Msg('超过48小时报名+邀请注册+入金后的How To')
        with self.step('步骤一：断言报名+邀请注册+入金后How To中的人物头像'):
            new_page.simulation_steps_3()
            new_page.waits()
            new_page.page.reload()
            new_page.click_element_32()
            tc = new_page.wait_for_selector_21()
        assert tc is not None

    def test_more_than_48_32(self):
        self.log = Msg('超过48小时报名+邀请注册+入金后的cash弹窗')
        with self.step('步骤一：断言报名+邀请注册+入金后cash弹窗'):
            new_page.waits()
            new_page.click_element_33()
            new_page.waits()
            new_page.click_element_34()
            new_page.waits()
            tc = new_page.wait_for_selector_22()
        assert tc is not None

    def test_more_than_48_33(self):
        self.log = Msg('超过48小时获得奖励抽奖')
        with self.step('步骤一：断言获奖弹窗'):
            new_page.simulation_steps_4()
            new_page.waits()
            new_page.click_element_35()
            new_page.click_element_36()
            tc = new_page.wait_for_selector_23()
            new_page.initialization_data()
        assert tc is not None
