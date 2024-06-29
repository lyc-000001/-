"""
@Author: Li Yu Cai
@Date: 2024/4/11 9:17
@FileName: page_edit.py
"""
import allure

from Pages.Base import BasePage
from Utils.tools import data_backup

QR_code1 = "body > div:nth-child(5) > div > div.ant-popover-content > div > div > div > div.build-url > div.ant-qrcode> canvas"
QR_code2 = 'body > div:nth-child(4) > div > div.ant-popover-content > div > div > div > div.build-url > div.ant-qrcode > canvas'


class EditPage(BasePage):

    def __init__(self, page):
        super().__init__(page)


    @allure.step('登录office')
    def office_login(self):
        self.page.goto('https://pre-office.webullbroker.com')
        self.page.locator('//*[@id="userName"]').fill('ko_auto_test@webull.com')
        self.page.locator('//*[@id="passwd"]').fill('Ac110403')
        self.page.locator('//*[@id="code"]').fill('888888')
        self.page.locator('//*[@id="react-app"]/div/div[2]/div[2]/div/form/div[2]/button').click()
        self.waits()

    @allure.step('备份数据')
    def data_backup_(self):
        data_backup('pre', 'us', "'P_19448','P_14773','P_13747','P_17027','P_14026','P_18348','P_13741'")

    @allure.step('构建倒计时活动应用')
    def release_djs(self):
        element = self.preview_release('https://pre-office.webullbroker.com/ko/editor/YXBwJjcxNSYwJjA=', QR_code1,
                                       QR_code2)

        return element

    @allure.step('构建内容资料库应用')
    def release_uj(self):
        element = self.preview_release('https://pre-office.webullbroker.com/ko/editor/YXBwJjI3NjEmMCYw', QR_code1,
                                       QR_code2)
        return element

    @allure.step('构建按钮操作应用')
    def release_button(self):
        element = self.preview_release('https://pre-office.webullbroker.com/ko/editor/YXBwJjEzJjAmMA==', QR_code1,
                                       QR_code2)
        return element

    @allure.step('构建官网链接跳转应用')
    def release_gw(self):
        element = self.preview_release('https://pre-office.webullbroker.com/ko/editor/YXBwJjEyODYmMCYw', QR_code1,
                                       QR_code2)
        return element

    @allure.step('构建邀请关系应用')
    def release_invite(self):
        element = self.preview_release('https://pre-office.webullbroker.com/ko/editor/YXBwJjc3NSYwJjA=', QR_code1,
                                       QR_code2)
        return element

    @allure.step('构建多语言&数据计算应用')
    def release_application_1(self):
        element = self.preview_release('https://pre-office.webullbroker.com/ko/editor/YXBwJjIzODgmMCYw', QR_code1,
                                       QR_code2)
        return element

    @allure.step('构建大转盘应用')
    def release_zp(self):
        element = self.preview_release('https://pre-office.webullbroker.com/ko/editor/YXBwJjM4MiYwJjA=', QR_code1,
                                       QR_code2)
        return element
