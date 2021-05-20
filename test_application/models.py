# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2020 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

# from django.db import models

# Create your models here.
from datetime import datetime

from django.db import models


class History(models.Model):
    username = models.CharField(max_length=32, verbose_name=u'用户名')
    bk_biz_id = models.BigIntegerField(verbose_name=u'业务id', null=True)
    bk_biz_name = models.CharField(max_length=64, verbose_name=u'业务名称', null=True)
    bk_job_id = models.IntegerField(verbose_name=u'作业ID', null=True)
    ip_list = models.TextField(verbose_name=u'主机列表', null=True)
    result = models.IntegerField(verbose_name=u'作业执行结果', null=True)
    log = models.TextField(verbose_name=u'作业执行日志', null=True)
    status = models.IntegerField(verbose_name=u'作业执行状态', null=True)
    created = models.DateTimeField(verbose_name=u'创建时间', default=datetime.now)

    class Meta:
        db_table = 'history'
        verbose_name = u'执行历史'
        verbose_name_plural = verbose_name


class StmSendHistory(models.Model):
    supplier_name = models.CharField(verbose_name=u'电信运营商名', max_length=10, default=None)
    supplier_place = models.CharField(verbose_name=u'运营商所在地', max_length=50, default=None)
    supplier_channel = models.CharField(verbose_name=u'短信发送渠道', max_length=50, default=None)
    custmer_name = models.CharField(verbose_name=u'客户名', max_length=225, default=None)
    custmer_place = models.CharField(verbose_name=u'客户所在地', max_length=50, default=None)
    mobile = models.BigIntegerField(verbose_name=u'发送目标手机',  default=None)
    mobile_from = models.CharField(verbose_name=u'发送目标手机归属地', max_length=10, default=None)
    error_code = models.CharField(verbose_name=u'发送结果，''0''表示发送成功，其他表示失败', max_length=4, default=None)
    error_message = models.CharField(verbose_name=u'错误信息', max_length=100, default=None)
    created_date = models.IntegerField(verbose_name=u'发送日期', default=None)
    created_time = models.DateTimeField(verbose_name=u'发送日期', default=None)

    class Meta:
        db_table = 'ht_stm_send_history'
        verbose_name = u'发送历史表'
        verbose_name_plural = verbose_name