import os

import yaml

from tools.logs_utils import logger


def set_data():
    root_path = os.path.dirname(os.path.abspath(__file__))
    print(root_path)
    dic = {"login":
        [
            ["admin", "LSYJ14001", "全国经销商"],
            ["admin", "LSYJ1400", "密码错误"],
            ["admi", "LSYJ14001", "用户账户不存在"]
        ]
    }
    # 拼接当前要输出日志的路径
    log_dir_path = os.sep.join([root_path, "..", f'data\\login.yaml'])
    print(log_dir_path)
    with open(log_dir_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(dic, f, allow_unicode="utf-8")
        # print(data_obj)


def get_data(dic_name):
    root_path = os.path.dirname(os.path.abspath(__file__))
    print(root_path)
    # 拼接当前要输出日志的路径
    log_dir_path = os.sep.join([root_path, "..", f'data\\{dic_name}.yaml'])
    print(log_dir_path)
    with open(log_dir_path, "r", encoding="utf-8") as f:
        data_obj = yaml.safe_load(f)
        logger.info(f"获取yaml的数据{data_obj}")
        return data_obj


if __name__ == '__main__':
    # dic = {"login": [[], []], }
    print(get_data("add_normal_user").get("add_normal_user"))
