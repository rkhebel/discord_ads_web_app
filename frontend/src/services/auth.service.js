// This file contains methods that perform auth functions by connecting to the api.
// User data is stored in local storage

//using this axios because i added interceptors to automatically add headers on requests and intercept 401s
// on response in case we need to refresh access token
import axios from './axios.service'

const API_URL = process.env.VUE_APP_API_URL + 'auth/';

class AuthService {
  login(user) {
    let login_url = API_URL + 'login';
    return axios.post(login_url, {
      email: user.email,
      password: user.password,
      user_type: user.type
    }).then(response => {
      return response.data;
    }).catch(error => {
      console.log(error);
      return Promise.reject(error);
    });
  }

  logout() {
    let logout_url = API_URL + 'logout';
    return axios.post(logout_url, {
    }).then(response => {
      return response.data;
    }).catch(error => {
      console.log(error);
      return Promise.reject(error);
    })
  }

  signup(user) {
    let register_url = API_URL + 'signup';
    return axios.post(register_url, {
      first_name: user.first_name,
      last_name: user.last_name,
      email: user.email,
      password: user.password,
      user_type: user.type
    }).then(response => {
      return response.data;
    }).catch(error => {
      console.log(error);
      return Promise.reject(error);
    })
  }
}

export default new AuthService();
