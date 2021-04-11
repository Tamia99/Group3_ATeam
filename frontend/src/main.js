import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import locale from 'element-ui/lib/locale/lang/en'
import Vuex from 'vuex'
import store from './vuex/store'
import '../theme/index.css'

Vue.config.productionTip = false
Vue.use(ElementUI, { locale })
Vue.use(Vuex)
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
