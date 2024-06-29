# -*- coding:utf-8 -*-

import os


class Config:
    # 项目地址
    # pre_url = "https://www.pre.webullbroker.com/"
    # uat_url = "https://office.uat.webullbroker.com/"

    # 项目根目录
    root_dir = os.path.split(os.path.split(__file__)[0])[0]
    test_cases_dir = root_dir + os.path.sep + "TestCases"
    test_files_dir = root_dir + os.path.sep + "TestFiles"
    test_img_dir = root_dir + os.path.sep + "TestReport" + os.path.sep + "Picture"
    test_report_dir = root_dir + os.path.sep + "TestReport" + os.path.sep + "AllureReport"
    test_result_dir = root_dir + os.path.sep + "TestReport" + os.path.sep + "AllureResult"
    test_screenshot_dir = root_dir + os.path.sep + "TestReport" + os.path.sep + "Screenshot"
    test_videos_dir = root_dir + os.path.sep + "TestReport" + os.path.sep + "Videos"
    logs = root_dir + os.path.sep + "Logs"

    # 权限认证目录
    # auth_dir = root_dir + os.path.sep + "Auth"

    # 浏览器
    browser = "chrome"

    # 运行地区、环境
    environment = "pre"
    area = "us"

    # 账号密码
    pre_webull_user_23 = "zengge_23@163.com"
    pre_webull_pwd_23 = "2f54e9657020c9c2f7ba0d56999f678d"  # auto1234
    pre_webull_user_21 = "zengge_21@163.com"
    pre_webull_pwd_21 = "03e0bef7ba34db76635abbac1102fd22"  # Aa123456
