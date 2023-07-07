import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import PayjpCheckout from 'vue-payjp-checkout'
import vuetify from './plugins/vuetify'
import VueGtm from 'vue-gtm'

Vue.config.productionTip = false

Vue.use(PayjpCheckout)
Vue.use(VueGtm, {
  id: 'GTM-NMP5NKT',//開発用
  enabled: true, 
  debug: true,
  ignoredViews: ['']
})

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')