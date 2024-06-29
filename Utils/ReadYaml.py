# -*- coding:utf-8 -*-
import os
from os.path import dirname, abspath
import yaml
from ruamel import yaml


# 读取配置信息
def read_yml(environment, area):
    path = dirname(dirname(abspath(__file__)))
    path = os.path.join(path, 'Conf', f'{environment}_config.yml')
    with open(path, 'r', encoding="utf-8") as f:
        yaml_loader = yaml.YAML(typ='rt')
        msg = yaml_loader.load(f.read())
        msg = msg[area]
    return msg
