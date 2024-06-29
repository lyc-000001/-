from Utils.dingtalk import send_dingtalk_message
import os


def run_case():
    # 运行测试用例
    os.system('pytest ./TestCases')
    # 生成allure报告
    # os.system('allure generate ./TestReport/result/ -o ./TestReport/AllureReport/ --clean')


def send_report():
    file_path = r"./TestReport/AllureReport/widgets/summary.json"
    send_dingtalk_message(file_path=file_path)


if __name__ == '__main__':
    run_case()
    # send_report()
