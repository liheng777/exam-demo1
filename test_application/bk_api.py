import base64
import time

from blueapps.utils.logger import logger
from config import APP_CODE, SECRET_KEY


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


# todo 标准运维
def get_task_status(client, task_id):
    """
    :param client: 执行蓝鲸api
    :param username: 用户名
    :param task_id: 任务id
    :return:
    """
    task_data = {
        'bk_biz_id': 6,
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
def search_business(client, param):
    result = client.cc.search_business(param)
    return result


def search_biz_hosts(client, param):
    """
    查询业务下的主机
    @param client:
    @param param:
    @return:
    """
    result = client.cc.list_biz_hosts(param)
    return result


def search_set(client, param):
    result = client.cc.search_set(param)
    return result
