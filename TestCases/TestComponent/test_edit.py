"""
@Author: Li Yu Cai
@Date: 2024/4/11 9:17
@FileName: test_edit.py
"""
from Pages.PageComponent.page_edit import EditPage
import allure
import pytest
from Utils.Log import Msg

global new_page


@pytest.mark.run(order=1)
class TestEdit:
    @staticmethod
    def step(msg=''):
        log = Msg(name='备份数据和构建应用')
        log.info(msg)
        return allure.step(msg)

    @pytest.mark.run(order=1)
    def test_backup_data(self, base_page):
        global new_page
        new_page = EditPage(base_page)
        self.step('备份数据')
        new_page.data_backup_()

    def test_release_djs(self):
        self.step('登录office')
        new_page.office_login()
        self.step('构建倒计时应用')
        element = new_page.release_djs()
        print(element)
        assert element is not None

    def test_release_uj(self):
        self.step('构建内容资料库应用')
        element = new_page.release_uj()
        print(element)
        assert element is not None

    def test_release_gw(self):
        self.step('构建官网链接跳转应用')
        element = new_page.release_gw()
        print(element)
        assert element is not None

    def test_release_button(self):
        self.step('构建按钮操作应用')
        element = new_page.release_button()
        print(element)
        assert element is not None

    def test_release_application_all(self):
        self.step('构建多语言&数据计算应用')
        element = new_page.release_application_1()
        print(element)
        assert element is not None

    def test_release_invite(self):
        self.step('构建邀请关系应用')
        element = new_page.release_invite()
        print(element)
        assert element is not None

    def test_release_zp(self):
        self.step('构建转盘应用')
        element = new_page.release_zp()
        print(element)
        assert element is not None
