import base64
import time

from blueapps.utils.logger import logger


# todo 作业平台
def get_execute_script(client, bk_biz_id, script_id, ip_list, script_param, script_content):
    fast_execute_data = {
        "account": "root",
        "bk_biz_id": bk_biz_id,
        "ip_list": ip_list
    }
    if script_content:
        fast_execute_data['script_content'] = str(base64.b64encode(script_content.encode("utf-8")), "utf-8")
    if script_param:
        fast_execute_data['script_param'] = str(base64.b64encode(script_param.encode("utf-8")), "utf-8")
    if script_id:
        fast_execute_data['script_id'] = script_id
    logger.info('获取蓝鲸API中的fast_execute_script方法的作业实例')
    # 执行脚本
    info_script = client.job.fast_execute_script(fast_execute_data)
    #   作业实例ID
    job_instance_id = None
    if info_script.get("result"):
        #   获取作业实例ID
        job_instance_id = info_script.get("data").get("job_instance_id")
    return job_instance_id


def get_script_detail(client, script_id):
    """
    @param client:
    @param script_id:
    @return:
    """
    fast_execute_data = {
        "account": "root",
        "bk_biz_id": 6,
        "id": script_id
    }
    # 执行脚本
    logger.info('根据脚本id查询脚本详情')
    info_script = client.job.get_script_detail(fast_execute_data)
    return info_script


def get_instance_log(client, bk_biz_id, job_instance_id):
    instance_log_data = {
        "bk_biz_id": bk_biz_id,
        "job_instance_id": job_instance_id,
    }
    logger.info('根据作业实例 ID 查询作业执行日志')
    job_info = client.job.get_job_instance_log(instance_log_data)
    logger.info('返回作业执行日志结果=>' + str(job_info))
    return job_info


def get_instance_status(client, bk_biz_id, job_instance_id):
    instance_log_data = {
        "bk_biz_id": bk_biz_id,
        "job_instance_id": job_instance_id,
    }
    logger.info('根据作业实例 ID 查询作业执行状态')
    job_info = client.job.get_job_instance_status(instance_log_data)
    while not job_info['data']["is_finished"]:
        time.sleep(5)
        job_info = client.job.get_job_instance_status(instance_log_data)
        if job_info['data']["is_finished"]:
            break
    return job_info['data']["is_finished"]


def get_job_detail(client, bk_biz_id, bk_job_id):
    param = {
        "bk_biz_id": bk_biz_id,
        "bk_job_id": bk_job_id
    }
    logger.info('根据作业模板 ID 查询作业模板详情')
    job_info = client.job.get_job_detail(param)
    return job_info


def do_execute_job(client, job_detail_result, bk_biz_id, bk_job_id, ip_list):
    """
    执行作业
    @param client:
    @param job_detail_result: 获取的作业详情
    @param bk_biz_id:
    @param bk_job_id:
    @param ip_list:
    @return:
    """
    _params = {
        "bk_biz_id": bk_biz_id,
        "bk_job_id": bk_job_id
    }
    job_detail = job_detail_result.get('data')
    for step in job_detail.get('steps'):
        if step.get('ip_list'):
            step['ip_list'] = ip_list
    _params['steps'] = job_detail.get('steps')
    logger.info('执行作业')
    job_exec_result = client.job.execute_job(_params)
    return job_exec_result


# todo 标准运维

def bk_start_task(client, _params):
    """
    开始执行任务
    """
    error_result = {"result": False, "code": 0, "message": u"执行任务失败，请与管理员联系", "data": {}}
    result = client.sops.start_task(_params)
    logger.info('开始执行任务' + str(result))
    if result.get('result'):
        return result
    else:
        return error_result


def bk_create_task(client, _params):
    """
    通过流程模板创建任务
    """
    error_result = {"result": False, "code": 0, "message": u"通过流程模板创建任务失败，请与管理员联系", "data": {}}
    result = client.sops.create_task(_params)
    logger.info('通过流程模板创建任务，返回结果' + str(result))
    if result.get('result'):
        return result
    else:
        return error_result


def get_task_status(client, bk_biz_id, task_id):
    """
    :param client: 执行蓝鲸api
    :param task_id: 任务id
    :return:
    """
    task_data = {
        'bk_biz_id': bk_biz_id,
        "task_id": task_id
    }
    logger.info('查询任务或任务节点执行状态')
    err_flag = 0
    task_info = client.sops.get_task_status(task_data)
    while not task_info['result'] and err_flag < 3:
        time.sleep(5)
        task_info = client.sops.get_task_status(task_data)
        if task_info['result']:
            break
        err_flag += 1
    flag = 0
    while task_info['result'] and task_info['data']['state'] == 'RUNNING' and flag < 60:
        time.sleep(5)
        task_info = client.sops.get_task_status(task_data)
        if task_info['result'] and task_info['data']['state'] != 'RUNNING':
            break
        flag += 1
    logger.info('返回执行结果=>' + str(task_info))
    return task_info


# todo 蓝鲸监控
def select_event(client, param):
    """

    @param client:
    @param param:
    @return:
    """
    result = client.monitor_v3.search_event(param)
    return result


# todo 配置平台
def search_biz_hosts(client, bk_biz_id, set_name_value, bk_set_ids, bk_module_ids, host_property_filter):
    """
    根据业务 ID 查询业务下的主机，可附带其他的过滤信息，如集群 id,模块 id 等
    @param client:
    @param bk_biz_id: 业务ID
    @param set_name_value: 集群名称
    @param bk_set_ids: 集群ID列表
    @param bk_module_ids: 模块ID列表
    @param host_property_filter: 主机属性组合查询条件（这里的是临时的，根据自己查询需求进行组合）
    @return:
    """
    param = {
        "page": {
            "start": 0,
            "limit": 10,
            "sort": "bk_host_id"
        },
        "bk_biz_id": bk_biz_id,
        "set_cond": [  # 集群查询条件

        ],
        "bk_set_ids": [],  # 集群列表
        "bk_module_ids": [],  # 模块列表
        "fields": [],  # 返回的主机属性列表
        # 用于根据主机属性字段搜索主机。组合支持 AND 和 OR 两种方式，可以嵌套，最多嵌套 2 层。 过滤规则为四元组 field, operator, value
        "host_property_filter": {  # 主机属性组合查询条件

        },
    }
    if set_name_value:  # 集群名称
        param['set_cond'].append({
            "field": "bk_set_name",
            "operator": "$eq",
            "value": set_name_value
        })
    if bk_set_ids:  # 集群列表
        param['bk_set_ids'] = bk_set_ids
    if bk_module_ids:  # 模块列表
        param['bk_module_ids'] = bk_module_ids
    if host_property_filter:  # 主机属性组合查询条件
        param['host_property_filter'] = {
            "condition": "AND",  # and的关系
            "rules": [
                {
                    "field": "bk_host_innerip",  # 内网 IP
                    "operator": "begins_with",
                    "value": "192.168"
                },
                {
                    "condition": "OR",
                    "rules": [
                        {
                            "field": "bk_os_type",  # 操作系统类型 1:Linux;2:Windows;3:AIX
                            "operator": "not_in",
                            "value": [
                                "3"
                            ]
                        },
                        {
                            "field": "bk_cloud_id",  # 云区域
                            "operator": "equal",
                            "value": 0
                        }
                    ]
                }
            ]
        }
    result = client.cc.list_biz_hosts(param)
    return result


def do_search_business(client, bk_biz_id, bk_biz_name):
    """
    查询业务
    @param client:
    @param bk_biz_id: 业务ID
    @param bk_biz_name: 业务名称
    @return:
    """
    param = {
        # "bk_supplier_account": "0",
        "fields": [  # 查询的字段
            "bk_biz_id",
            "bk_biz_name"
        ],
        "condition": {  # 查询条件

        },
        "page": {  # 分页
            "start": 0,
            "limit": 10,
            "sort": "bk_biz_id"
        }
    }
    if bk_biz_name:  # 当查询条件bk_biz_name不为空时
        param["condition"]['bk_biz_name'] = bk_biz_name
    if bk_biz_id:  # 当查询条件bk_biz_id不为空时
        param["condition"]['bk_biz_id'] = bk_biz_id
    result = client.cc.search_business(param)
    return result


def do_search_set(client, bk_biz_id, bk_set_name):
    """
    查询集群
    @param client:
    @param bk_biz_id: 业务ID
    @param bk_set_name: 集群名称
    @return:
    """
    param = {
        # "bk_supplier_account": "0",
        "bk_biz_id": int(bk_biz_id),
        "fields": [  # 查询的字段
            "bk_set_id",
            "bk_set_name"
        ],
        "condition": {  # 查询条件

        },
        "page": {  # 分页
            "start": 0,
            "limit": 10,
            "sort": "bk_set_name"
        }
    }
    if bk_set_name:  # 当查询条件bk_set_name不为空时
        param["condition"]['bk_set_name'] = bk_set_name
    result = client.cc.search_set(param)
    return result


def do_search_module(client, bk_biz_id, bk_module_name):
    """
    查询模块
    @param client:
    @param bk_biz_id: 业务ID
    @param bk_module_name: 模块名称
    @return:
    """
    param = {
        # "bk_supplier_account": "0",
        "bk_biz_id": int(bk_biz_id),
        "fields": [  # 查询的字段
            "bk_module_name",
            "bk_set_id"
        ],
        "condition": {  # 查询条件

        },
        "page": {  # 分页
            "start": 0,
            "limit": 10,
            "sort": "bk_biz_id"
        }
    }
    if bk_module_name:  # 当查询条件bk_module_name不为空时
        param["condition"]['bk_module_name'] = bk_module_name
    result = client.cc.search_module(param)
    return result
