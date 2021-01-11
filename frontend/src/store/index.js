import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from 'vuex-persistedstate';

import { auth } from './auth.module';

const authState = createPersistedState({
  paths: ['auth']
})

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth
  },
  plugins: [authState]
});