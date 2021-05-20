<template>
    <div id="app" style="height: 100%">
        <remote-css
            href="https://magicbox.bk.tencent.com/static_api/v3/assets/bootstrap-3.3.4/css/bootstrap.min.css"
        />
        <remote-css
            href="https://magicbox.bk.tencent.com/static_api/v3/bk/css/bk.css"
        />
        <nav class="bk-horz-nav11">
            <div class="bk-nav-logo fl">
                <img
                    src="https://magicbox.bk.tencent.com/static_api/v3/bk/images/logo1.png"
                />蓝鲸模考
            </div>
            <div class="bk-nav-user fr">
                <span class="mr5">{{username}}</span>
                <img
                    src="https://magicbox.bk.tencent.com/static_api/v3/components_pro/horizontal_nav1/images/avatar.png"
                />
            </div>
            <ul class="bk-nav-links fl" style="padding-left: 16px">
                <li :class="{ active: isActive[0] }" @click="activeMenu(0)">
                    <router-link to="/"> 首页 </router-link>
                </li>
                <li :class="{ active: isActive[1] }" @click="activeMenu(1)">
                    <router-link to="/history/list"> 历史任务 </router-link>
                </li>
                <li :class="{ active: isActive[2] }" @click="activeMenu(2)">
                    <router-link to="/about1"> 执行记录1 </router-link>
                </li>
                <!--        <li class="bk-has-submenu">-->
                <!--          <a href="javascript:;">系统配置</a>-->
                <!--          <ul class="bk-submenu">-->
                <!--            <li>-->
                <!--              <a href="city_manage.html">配置城市</a>-->
                <!--            </li>-->
                <!--            <li>-->
                <!--              <a href="auth_manage.html">配置部门</a>-->
                <!--            </li>-->
                <!--          </ul>-->
                <!--        </li>-->
            </ul>
        </nav>
        <div class="page-content">
            <div class="page-content-wrapper">
                <div class="bk-panel bk-panel-title-btns">
                    <router-view />
                </div>
            </div>
        </div>
        <footer class="footer">
            <div class="footer-links">
                <ul>
                    <li>
                        <a href="###">QQ咨询</a>
                    </li>
                    <li>
                        <a href="###">蓝鲸论坛</a>
                    </li>
                    <li>
                        <a href="###">蓝鲸官网</a>
                    </li>
                    <li>
                        <a href="###">蓝鲸智云工作台</a>
                    </li>
                </ul>
            </div>
            <p class="footer-copyright">
                Copyright &copy; 2012-2017 Tencent BlueKing. All Rights Reserved.
                蓝鲸智云 版权所有
            </p>
        </footer>
    </div>
</template>

<script>
export default {
  components: {
    'remote-css': {
      render(createElement) {
        return createElement('link', {
          attrs: { rel: 'stylesheet', href: this.href }
        })
      },
      props: {
        href: { type: String, required: true }
      }
    }
    // 'remote-js': {
    //     render(createElement) {
    //         return createElement('script', {attrs: {type: 'text/javascript', src: this.src}})
    //     },
    //     props: {
    //         src: {type: String, required: true}
    //     }
    // }
  },
  data() {
    return {
      isActive: [true, false, false],
      username: 'admin'
    }
  },
  mounted() {
    this.$http.get('get_username').then((res) => {
      this.username = res.data.username
    })
  },
  methods: {
    activeMenu(index) {
      this.isActive.forEach((item, ind) => {
        if (index === ind) {
          this.$set(this.isActive, ind, true)
        } else {
          this.$set(this.isActive, ind, false)
        }
      })
    }
  }
}
</script>
<style lang="scss">
@import "assets/css/common.css";

.bk-panel
  .bk-panel-body
  > .bk-table.has-thead-bordered
  > tbody
  > tr:first-child
  > td,
.bk-panel
  .bk-panel-body
  > .bk-table.table-bordered
  > tbody
  > tr:first-child
  > td {
  border-top: none;
}
</style>
<style lang="scss" scoped>
.bk-horz-nav11 {
  height: 72px;
  line-height: 72px;
  padding: 0 15px 0 35px;
  background-color: #313b4c;
}
.bk-horz-nav .bk-nav-logo,
.bk-horz-nav11 .bk-nav-logo {
  color: #fff;
  font-size: 18px;
  float: left;
}
.bk-horz-nav .bk-nav-logo > img,
.bk-horz-nav11 .bk-nav-logo > img {
  vertical-align: middle;
  margin-right: 15px;
  height: 30px;
  margin-top: -5px;
}
.bk-horz-nav11 .bk-nav-user {
  float: right;
  padding-left: 20px;
  padding-right: 20px;
  color: #8292a7;
  cursor: pointer;
}
.mr5 {
  margin-right: 5px !important;
}
.bk-horz-nav .bk-nav-user > img,
.bk-horz-nav11 .bk-nav-user > img {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  vertical-align: middle;
}
.bk-horz-nav .bk-nav-links,
.bk-horz-nav11 .bk-nav-links {
  margin: 0;
  padding: 0;
  list-style: none;
  font-size: 0;
  float: right;
}
.bk-horz-nav .bk-nav-links > li.active,
.bk-horz-nav11 .bk-nav-links > li.active {
  background-color: #283242;
}
.bk-horz-nav .bk-nav-links > li > a,
.bk-horz-nav11 .bk-nav-links > li > a {
  display: block;
  padding: 0 22px;
  text-decoration: none;
  color: #8292a7;
  line-height: 72px;
}
.bk-horz-nav .bk-nav-links > li,
.bk-horz-nav11 .bk-nav-links > li {
  display: inline-block;
  font-size: 14px;
}
.bk-horz-nav .bk-nav-links > li > a[data-v-7ba5bd90],
.bk-horz-nav11 .bk-nav-links > li > a[data-v-7ba5bd90] {
  display: block;
  padding: 0 22px;
  text-decoration: none;
  color: #8292a7;
  line-height: 72px;
}
.page-content {
  min-height: calc(100% - 72px - 150px);
  width: 90%;
  min-width: 1200px;
  max-width: 1530px;
  margin: auto;
  margin-top: 30px;
}
.page-content-wrapper {
  min-width: 1200px;
  margin: auto;
}
</style>
