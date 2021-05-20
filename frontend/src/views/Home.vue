<template>
    <div>
        <bk-form :label-width="200" style="margin-bottom: 20px">
            <bk-form-item label="选择业务">
                <bk-select v-model="bkBizId" style="width: 250px;"
                           placeholder="请选择业务"
                           :clearable="false"
                           @change="bizIdChange"
                           ext-cls="select-custom"
                           ext-popover-cls="select-popover-custom">
                    <bk-option v-for="item in bizIdList"
                               :key="item.bk_biz_id"
                               :id="item.bk_biz_id"
                               :name="item.bk_biz_name">
                    </bk-option>
                </bk-select>
            </bk-form-item>
            <bk-form-item label="选择集群">
                <bk-select v-model="bkSetId" style="width: 250px;"
                           placeholder="请选择集群"
                           @change="setIdChange"
                           :clearable="false">
                    <bk-option v-for="item in bkSetIdList"
                               :key="item.bk_set_id"
                               :id="item.bk_set_id"
                               :name="item.bk_set_name">
                    </bk-option>
                </bk-select>
            </bk-form-item>
            <!--            <bk-form-item label="日期">-->
            <!--                <bk-date-picker-->
            <!--                    v-model="initDateTimeRange"-->
            <!--                    :placeholder="'选择日期时间范围'"-->
            <!--                    format="yyyy-MM-dd HH:mm:ss"-->
            <!--                    :type="'datetimerange'">-->
            <!--                </bk-date-picker>-->
            <!--            </bk-form-item>-->
            <!--            <bk-form-item>-->
            <!--                <bk-button :theme="'primary'" :title="'主要按钮'" class="mr10" @click="init">查询</bk-button>-->
            <!--            </bk-form-item>-->
            <bk-form-item>
                <bk-button :theme="'primary'" :title="'主要按钮'" class="mr10" @click="doExecuteJob">执行作业</bk-button>
            </bk-form-item>
        </bk-form>
        <div>
            <bk-table
                v-bkloading="{ isLoading: isLoading, zIndex: 10 }"
                :data="data"
                :size="size"
                :outer-border="false"
                :header-border="false"
                @selection-change="selectChange"
                :header-cell-style="{ background: '#fff' }">
                <bk-table-column type="selection" width="60"></bk-table-column>
                <bk-table-column type="index" label="序列" width="60"></bk-table-column>
                <bk-table-column label="内网IP" prop="bk_host_innerip"></bk-table-column>
                <bk-table-column label="系统名" prop="bk_os_name"></bk-table-column>
                <bk-table-column label="主机名" prop="bk_host_name"></bk-table-column>
                <bk-table-column label="云区域" prop="bk_cloud_id">
                </bk-table-column>
                <bk-table-column label="创建时间" prop="create_time">
                    <!--                    <template slot-scope="scope">-->
                    <!--                        dateFormat({{scope.row.create_time}})-->
                    <!--                    </template>-->
                </bk-table-column>
                <bk-table-column label="操作" width="150">
                    <template slot-scope="props">
                        <bk-button class="mr10" theme="primary" text :disabled="props.row.status === '创建中'" @click="reset(props.row)">重置</bk-button>
                        <bk-button class="mr10" theme="primary" text @click="remove">移除</bk-button>
                    </template>
                </bk-table-column>
            </bk-table>
            <bk-pagination
                style="margin-top: 20px"
                size="small"
                :current.sync="pagingConfigOne.current"
                :limit="pagingConfigOne.limit"
                :count="pagingConfigOne.count"
                :align="pagingConfigOne.align"
                :show-limit="pagingConfigOne.showLimit"
                @change="handlePageChange">
            </bk-pagination>
        </div>
        <bk-dialog
            v-model="exampleSetting.visible"
            :header-position="exampleSetting.headerPosition"
            :loading="exampleSetting.loading"
            @confirm="confirm"
            @cancel="cancel"
            title="执行作业">
            是否执行作业？
        </bk-dialog>
    </div>
</template>

<script>

import Vue from 'vue'
import { bkButton, bkTable, bkTableColumn, bkTooltips, bkPagination, bkDialog  } from 'bk-magic-vue'
Vue.use(bkTooltips)
export default {
  name: 'Home',
  components: {
    bkButton,
    bkTable,
    // bkInput,
    bkTableColumn,
    bkPagination,
    bkDialog
  },
  data() {
    return {
      initDateTime: new Date(),
      // bizIdList: [{
      //   bk_biz_id: null,
      //   bk_biz_name: '全部'
      // }],
      bizIdList: [],
      bkBizId: null,
      bkSetId: null,
      bkSetIdList: [],
      owner: null,
      pagingConfigOne: {    // 分页
        current: 1,
        limit: 10,
        count: 0,
        align: 'center',
        showLimit: false
      },
      isLoading: false,
      size: 'small',
      data: [],
      initDateTimeRange: [new Date(), new Date()],
      exampleSetting: { // 弹出框
        visible: false,
        loading: false,
        countdown: 3,
        headerPosition: 'left',
        timer: null
      },
      ipList: []
    }
  },
  mounted() {
    // this.$http.get('get_event').then((res) => {
    //   this.msg = res.data
    // })
  },
  created() {
    this.$http.get('api/test').then((res) => {
      console.log(res)
    })
    this.getBusiness()
    this.init()
  },
  methods: {
    confirm() { // 弹出框确定
      this.exampleSetting.loading = true
      const data = {
        bk_biz_id: this.bkBizId,
        ip_list: this.ipList
      }
      this.$http.post('do_execute_job/', data).then((res) => {
        if (res.data.result) {
          this.$bkMessage({
            theme: 'success',
            message: res.data.message
          })
        } else {
          this.$bkMessage({
            theme: 'error',
            message: res.data.message
          })
        }
      })
        .finally(() => {
          this.exampleSetting.visible = false
          this.exampleSetting.loading = false
        })
      // this.exampleSetting.timer = setInterval(() => {
      //   this.exampleSetting.countdown -= 1
      //   if (this.exampleSetting.countdown === 0) {
      //     this.exampleSetting.visible = false
      //     this.exampleSetting.loading = false
      //     clearInterval(this.exampleSetting.timer)
      //   }
      // }, 1000)
    },
    cancel() { // 弹出框取消
      console.warn('cancel')
    },
    handlePageChange(page) {
      this.pagingConfigOne.current = page
      this.init()
    },
    remove() {
      // 弹出框取消按钮背景色删除
      const style = document.getElementsByName('cancel')[0].getAttribute('class')
        .replace('bk-primary', '')
      document.getElementsByName('cancel')[0].setAttribute('class', style)
      this.exampleSetting.visible = true
    },
    reset(row) {
      row.status = '创建中'
    },
    selectChange(val) {
      this.ipList = []
      val.forEach((item) => {
        this.ipList.push({
          bk_cloud_id: 0,
          ip: item.bk_host_innerip
        })
      })
      console.log(val)
    },
    search() {
      console.log(this.initDateTimeRange)
    },
    getBusiness() {
      this.$http.get('get_business').then((res) => {
        if (res.data.result) {
          // const data = [{
          //   bk_biz_id: null,
          //   bk_biz_name: '全部'
          // }]
          // this.bizIdList = data.concat(res.data.data.info)
          this.bizIdList = res.data.data.info
        }
      })
    },
    getSet() {
      this.$http.get(`get_set?bk_biz_id=${this.bkBizId}`).then((res) => {
        if (res.data.result) {
          this.bkSetIdList = res.data.data.info
        }
      })
    },
    bizIdChange(newValue, oldValue) {
      console.log(newValue, oldValue)
      this.bkSetId = null
      this.ipList = []
      this.getSet()
      this.init()
    },
    setIdChange() {
      this.ipList = []
      this.init()
    },
    init() {
      this.data = []
      this.total = 0
      this.isLoading = true
      const data = {
        pageSize: this.pagingConfigOne.limit,
        currentPage: this.pagingConfigOne.current,
        bk_biz_id: this.bkBizId,
        bk_set_id: this.bkSetId
      }
      this.$http.get(`search_host?data=${JSON.stringify(data)}`).then((res) => {
        if (res.data.result) {
          this.data = res.data.data.info
          this.pagingConfigOne.count = res.data.data.count
        } else {
          this.data = []
          this.pagingConfigOne.count = 0
        }
      })
        .finally(() => {
          this.isLoading = false
        })
    },
    doExecuteJob() {
      // 弹出框取消按钮背景色删除
      const style = document.getElementsByName('cancel')[0].getAttribute('class')
        .replace('bk-primary', '')
      document.getElementsByName('cancel')[0].setAttribute('class', style)
      this.exampleSetting.visible = true
    },
    executeScript() {
      this.loading = true
      this.$http
        .request({
          url: 'execute_task',
          method: 'post',
          data: {
            bk_biz_id: 'this.bkBizId'
          }
        })
        .then((res) => {
          if (res.data.result) {
            this.$message({
              message: '执行成功',
              type: 'success'
            })
          }
          this.loading = false
        })
    }
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    h3 {
      margin: 40px 0 0;
    }
    ul {
      list-style-type: none;
      padding: 0;
    }
    li {
      display: inline-block;
      margin: 0 10px;
    }
    a {
      color: #42b983;
    }
     .bk-table-header .custom-header-cell {
        color: inherit;
        text-decoration: underline;
        text-decoration-style: dashed;
        text-underline-position: under;
    }
    li {
        display: block;
    }
</style>
