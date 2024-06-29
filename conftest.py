# encoding=utf-8
import os

import allure
import pytest
from Conf.config import Config
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="class")
def base_page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False,
                                             channel=Config.browser,
                                             args=['--start-maximized'])
        context = browser.new_context(record_video_dir=Config.test_videos_dir, no_viewport=True)
        # 录制日志
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        context.grant_permissions(['clipboard-write', 'clipboard-read'])
        page = context.new_page()

        yield page

        context.tracing.stop(path="./TestReport/trace.zip")
        # 关闭浏览器
        page.close()
        context.close()


# 截图钩子
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    获取每个用例状态的钩子函数
    :param item: 测试用例
    :param call: 测试步骤
    :return:
    """
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()  # 从钩子方法的调用结果中获取测试报告
    # rep.when表示测试步骤，仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        with allure.step('---添加失败截图---'):
            # path = Config.test_screenshot_dir + os.path.sep + item.funcargs["datas"].get("用例编号") + "失败截图.png"
            path = Config.test_screenshot_dir + os.path.sep + "失败截图.png"
            try:
                file = item.funcargs["base_page"].screenshot(path=path)
                allure.attach(file, "失败截图", allure.attachment_type.PNG)
            except Exception as e:
                print("截图失败")
        with allure.step('---失败用例视频---'):
            try:
                page = item.funcargs["base_page"]
                video_file = page.video.path()
                item.user_properties.append(("failure_video", video_file))
                allure.attach.file(video_file, name="FailureVideo", attachment_type=allure.attachment_type.WEBM)
            except Exception as e:
                print("视频生成失败")
            # 放入视频
            # allure.attach.file(filepath, name=f"{request.node.name}-{human_readable_status}-{index + 1}",
            #                    attachment_type=allure.attachment_type.WEBM)
