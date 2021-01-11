import AuthService from '../services/auth.service';

export const auth = {
  namespaced: true,
  state: { 
    loggedIn: false, 
    access_token: '',
    refresh_token: ''
  },
  actions: {
    login({ commit }, user) {
      return AuthService.login(user).then(
        response_data => {
          if (response_data.access_token && response_data.refresh_token) {
            commit('loginSuccess', response_data);
            return Promise.resolve(response_data);
          }
          commit('loginFailure');
          return Promise.resolve(response_data);
        }
      );
    },
    logout({ commit }) {
      return AuthService.logout().then( response_data => {
        commit('logout');
        return Promise.resolve(response_data);
      })
    },
    signup({ commit }, user) {
      return AuthService.signup(user).then(
        response_data => {
          if (!response_data.error) {
            commit('signupSuccess');
            return Promise.resolve(response_data);
          }
          commit('signupFailure');
          return Promise.reject(response_data);
        }
      );
    }
  },
  mutations: {
    loginSuccess(state, response_data) {
      state.loggedIn = true;
      state.access_token = response_data.access_token;
      state.refresh_token = response_data.refresh_token;
    },
    loginFailure(state) {
      state.loggedIn = false;
    },
    logout(state) {
      state.loggedIn = false;
      state.access_token = '';
      state.refresh_token = '';
    },
    signupSuccess(state) {
      state.loggedIn = false;
    },
    signupFailure(state) {
      state.loggedIn = false;
    }
  }
};