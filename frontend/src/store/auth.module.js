import AuthService from '../services/auth.service';

export const auth = {
  namespaced: true,
  state: { 
    loggedIn: false, 
    access_token: '',
    refresh_token: '',
    user_type: ''
  },
  actions: {
    login({ commit }, user) {
      return AuthService.login(user).then(
        response_data => {
          if (response_data.access_token && response_data.refresh_token && response_data.user_type) {
            commit('loginSuccess', response_data);
          }
          else {
            commit('loginFailure');
          }
          return Promise.resolve(response_data);
        }
      ).catch(error => {
        commit('loginFailure');
        return Promise.reject(error);
      });
    },
    logout({ commit }) {
      return AuthService.logout().then(response_data => {
        commit('logout');
        return Promise.resolve(response_data);
      }).catch(error => {
        commit('logout');
        return Promise.reject(error);
      })
    },
    signup({ commit }, user) {
      return AuthService.signup(user).then(
        response_data => {
          if (!response_data.error) {
            commit('signupSuccess');
          }
          else {
            commit('signupFailure');
          }
          return Promise.resolve(response_data);
        }
      ).catch(error => {
        commit('signupFailure');
        return Promise.reject(error);
      });
    }
  },
  mutations: {
    loginSuccess(state, response_data) {
      state.loggedIn = true;
      state.access_token = response_data.access_token;
      state.refresh_token = response_data.refresh_token;
      state.user_type = response_data.user_type;
    },
    loginFailure(state) {
      state.loggedIn = false;
    },
    logout(state) {
      state.loggedIn = false;
      state.access_token = '';
      state.refresh_token = '';
      state.user_type = '';
    },
    signupSuccess(state) {
      state.loggedIn = false;
    },
    signupFailure(state) {
      state.loggedIn = false;
    }
  }
};