import Vue from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import router from './router';
import store from './store';
import { ValidationProvider, extend } from 'vee-validate';
import { required } from 'vee-validate/dist/rules';

Vue.config.productionTip = false;

// this is for vee-validate
extend('required', {
  ...required,
  message: 'This field is required'
});
Vue.component('ValidationProvider', ValidationProvider);

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
