# encoding=utf-8
import json
import random
import requests
from rediscluster import RedisCluster
from Utils.ReadYaml import read_yml
from Utils.Log import Msg
from Utils.db import Mysql
log_msg = Msg(name='log_msg')


# 生成email账号
def random_email_():
    email_type = ["@qq.com", "@163.com", "@126.com", "@189.com", "@bccto.cc"]
    email_type_ = random.choice(email_type)
    rang = random.randint(2, 5)
    number = "0123456789qwertyuioplkjhgfdsazxcvbnm"
    number_ = "".join(random.choice(number) for i in range(rang))
    email = number_ + email_type_
    return email


# 生成电话号码
def random_phone_(area):
    number = None
    str_ = "0123456789"
    if area == 'jp':
        num = '+81-'
        num_ = "".join(random.choice(str_) for i in range(8))
        number = num + "136" + num_
        # number = "136" + num_
    elif area == 'us':
        # +1-3334443010
        num = '+1-'
        num_ = "".join(random.choice(str_) for i in range(7))
        number = num + "333" + num_
        # number = "333" + num_
    elif area == 'sg':
        # +65-44440100
        num = '+65-'
        num_ = "".join(random.choice(str_) for i in range(5))
        number = num + "444" + num_
        # number = "444" + num_
    elif area == 'hk':
        # +852-33330209
        num = '+852-'
        num_ = "".join(random.choice(str_) for i in range(5))
        number = num + "333" + num_
        # number = "333" + num_
    elif area == 'au':
        # +61-1668563363
        num = '+61-'
        num_ = "".join(random.choice(str_) for i in range(7))
        number = num + "166" + num_
        # number = "166" + num_
    else:
        print('请输入正确地区')
    return number


# 获取数据库配置
def get_base(environment, area):
    msg = read_yml(environment, area)
    return msg


def get_redis_code_(username, account_type, event_type, msg, sql=None):
    """
    :param msg:
    :param username: 账号   string
    :param account_type: int   账号类型   1、手机   2、邮箱
    :param event_type: 事件类型 int    1、注册事件   2、手机、邮箱绑定   3、开户验证 4、邀请平台注册 5、邀请平台登录
    :param sql:
    :return:
    """
    startup_nodes = msg['redis']
    try:
        rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True, skip_full_coverage_check=True)
        log_msg.info('redis connection succeeded')
    except Exception as e:
        log_msg.info(f'redis连接错误:error {e}')

    if account_type == 1:
        account = 'PHONE'
    else:
        account = 'EMAIL'

    # 注册获取验证码
    if event_type == 1:
        sql = f'REG_{account}_{username}'
    # 邮箱\手机绑定
    elif event_type == 2:
        sql = f'BIND_{account}_{username}'
    # 开户验证码
    elif event_type == 3:
        sql = f'APP_SEND_CODE_{account}_{username}'
    elif event_type == 4:
        sql = f"mktb-user:email-code-v2:1:1:{username}"
    elif event_type == 5:
        sql = f"mktb-user:email-code-v2:2:1:{username}"
    else:
        sql = sql
    log_msg.info(f'执行语句：{sql}')
    verification_code = rc.get(sql)
    log_msg.info(f'验证码:{verification_code}')
    if verification_code:
        if event_type == 4 or event_type == 5:
            ret_ = json.loads(verification_code)
            return ret_['code']
        else:
            return verification_code
    else:
        return 'NULL'


def get_user_id(environment, account):
    url = "https://web-tools.preplat.webullbroker.com/api/tools/user/get_user_id"
    data = json.dumps(
        {"env": environment, "account": account}
    )
    headers = {'Content-Type': 'application/json', }
    ret = requests.post(url=url, headers=headers, data=data)
    user_id = (ret.json()['msg'])
    ret = user_id.isdigit()
    if ret is not True:
        return {"msg": "请确认是可登录账户", "code": 500}
    return user_id


# 获取token
def get_token(user, pwd, msg):
    url = f'{msg["login_url"]}/api/user/v1/login/account/v2'

    data = {
        "account": user,
        "accountType": 2,
        "channel": "app",
        "deviceId": "f249de435c8a42bb9c0607f6e3422f4a",
        "deviceName": "Redmi Note 8 Pro",
        "extInfo": {
            "codeAccountType": 0,
            "xPos": 0
        },
        "grade": 1,
        "pwd": pwd,
        "regionId": "6"
    }

    response = requests.post(url, headers=msg['login_headers'], json=data)
    result = response.json()

    if response.status_code == 200:
        accessToken = result['accessToken']
        return accessToken
    else:
        print('请求失败')
        return 'NULL'


def tokens(environment, area, user, pwd):
    msg = get_base(environment, area)
    token_ = get_token(user=user, pwd=pwd, msg=msg)
    return token_


def data_backup(environment, area, page_ids):
    msg = get_base(environment, area)
    mysql = Mysql(host=msg["mysql_host"], user=msg["mysql_user"], pwd=msg["mysql_pwd"], port=3306)
    mysql.sql_perform(
        'INSERT INTO wl_oas.wlo_ko_module_app_record_back(id,title, cover_url, status,params,target_url,create_time,file_path,approve_status,category_id,publish_time,down_time,content_tags,operation_id,operation_name,page_id,update_content,module_status,module_approve_status,deploy_env,location_env,update_operation_id,update_operation_name,ui_principal_list,app_type,app_level,app_note,approve_principal_list,update_principal_list,owner_type,timer,extend_param_content,platform_type) SELECT id,title, cover_url, status,params,target_url,create_time,file_path,approve_status,category_id,publish_time,down_time,content_tags,operation_id,operation_name,page_id,update_content,module_status,module_approve_status,deploy_env,location_env,update_operation_id,update_operation_name,ui_principal_list,app_type,app_level,app_note,approve_principal_list,update_principal_list,owner_type,timer,extend_param_content,platform_type FROM wl_oas.wlo_ko_module_app_record WHERE page_id in ({});'.format(
            page_ids))
    mysql.sql_perform(
        'INSERT into wl_oas.wlo_ko_module_content_record_back(id,resource_id,resource_type,content,update_content) select id,resource_id,resource_type,content,update_content from wl_oas.wlo_ko_module_content_record WHERE resource_id in (select id from wl_oas.wlo_ko_module_app_record where page_id in ({}));'.format(
            page_ids))


def record_response(response, url, captured_response):
    response_url = response.url
    if url in response_url:
        # 获取响应的文本数据
        body = response.text()
        # 提取 newsUrl 字段
        data = json.loads(body)
        data_list = data['data']
        for item in data_list:
            captured_response.append(item)


def record_request(request, url, captured_request):
    request_url = request.url
    if url in request_url:
        # 获取响应的文本数据
        body = request.post_data
        # 提取 newsUrl 字段
        data = json.loads(body)
        captured_request.append(data)
