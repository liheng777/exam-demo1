import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from './service'
import ElementUI from 'element-ui'
import moment from 'moment'
import 'element-ui/lib/theme-chalk/index.css'
// 全量引入 bk-magic-vue
import bkMagicVue from 'bk-magic-vue'
// 全量引入 bk-magic-vue 样式
import 'bk-magic-vue/dist/bk-magic-vue.min.css'
Vue.config.productionTip = false
Vue.config.productionTip = false
Vue.prototype.$http = axios
Vue.use(ElementUI)
Vue.use(
  bkMagicVue,
  {
    zIndex: 3000,
    'bk-button': {
      theme: 'primary'
    },
    'bk-input': {
      clearable: true
    }
  }
)

Vue.filter('date', (value, format = 'YYYY-MM-DD HH:mm:ss') => moment(value).format(format))
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
