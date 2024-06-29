import json
import requests


def send_dingtalk_message(file_path):
    # allure报告结果json路径
    # file_path = r"D:\test_daily\report\html\widgets\summary.json"
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    case_json = data['statistic']
    case_all = case_json['total']  # 测试用例总数
    case_fail = case_json['failed']  # 失败用例数量
    case_pass = case_json['passed']  # 成功用例数量
    if case_all >= 0:
        # 计算出来当前失败率
        case_rate = round((case_pass / case_all) * 100, 2)
    else:
        print('未获取到执行结果')

    text = f"ko自动化测试报告" \
           f"\n用例通过率：{case_rate}%" \
           f"\n执行用例数：{case_all}个" \
           f"\n成功用例数：{case_pass}个" \
           f"\n失败用例数：{case_fail}个" \
           f"\n测试报告地址：http://localhost:63342/webull-operation-autotest/TestReport/AllureReport/index.html"

    data = {
        "msgtype": "text",
        "text": {
            "content": text
        },
        "at": {
            "atMobiles": [
                "+86-18239432539",
                "+86-13543284669",
                "+86-15019280592"
            ],
            "isAtAll": False
        }
    }
    headers = {'Content-Type': 'application/json'}
    url = 'https://oapi.dingtalk.com/robot/send?access_token=f75030fef4962865396e7f26f5a886ae3cc88d005c59c8514b9ced3a45b95512'

    requests.post(url=url, headers=headers, data=json.dumps(data))
