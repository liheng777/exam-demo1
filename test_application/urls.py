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

from django.conf.urls import url

from . import views

urlpatterns = (
    url(r"^$", views.home),
    url(r"^dev-guide/$", views.dev_guide),
    url(r"^contact/$", views.contact),
    url(r"^get_username/$", views.get_username),
    url(r"^api/test/$", views.test),
    url(r"^get_business/$", views.get_business),
    url(r"^search_host/$", views.search_host),
    url(r"^get_set/$", views.get_set),
    url(r"^do_execute_job/$", views.do_execute_job),
    url(r"^search_history_list/$", views.search_history_list),

    url(r"^get_supplier_name_charts/$", views.get_supplier_name_charts),
    url(r"^get_supplier_channel_charts/$", views.get_supplier_channel_charts),
    url(r"^get_customer_name_charts/$", views.get_customer_name_charts),

    url(r'^download_data', views.download_data),  # 导出Excel
    url(r'^export_all_excel/$', views.export_all_excel),
)
