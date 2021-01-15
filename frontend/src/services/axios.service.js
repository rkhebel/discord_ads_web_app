// this file contains interceptors for axios, that add the access token to outgoing requests
// and handle logic for refreshing the access token

import axios from 'axios';
import store from '../store';
import router from '../router'

const API_URL = process.env.VUE_APP_API_URL + 'auth/';

//on all requests, add the access token if we have it along with accept and content-type headers
axios.interceptors.request.use(
  config => {
    let access_token = store.state.auth.access_token;
    //if we're refreshing our token, make sure to use refresh token instead
    if (config.url.endsWith('/auth/refresh')) {
      access_token = store.state.auth.refresh_token;
    }
    if (access_token) {
      config.headers['Authorization'] = 'Bearer ' + access_token;
    }
    config.headers['Accept'] = 'application/json, text/plain, */*';
    config.headers['Content-Type'] = 'application/json';
    return config;
  },
  error => {
    Promise.reject(error);
  }
)

//response interceptor, here is where we check if we had an unauthorized request. if so, refresh token
axios.interceptors.response.use(
  response => {
    return response;
  }, function (error) {
    if (!error.response) {
      return Promise.reject(error);
    }
    let original_request = error.config;
    if (error.response.status === 401 && original_request.url.endsWith('/auth/refresh')) {
      console.log('refresh token not valid, routing to log in');
      router.push('/login')
      return Promise.reject(error);
    }
    if (error.response.status === 401 && !original_request._retry) {
      original_request._retry = true;
      return axios.get(API_URL + 'refresh').then(response => {
        if (response.status === 200) {
          console.log('refreshed token!');
          store.state.auth.access_token = response.data.access_token;
          axios.defaults.headers.common['Authorization'] = 'Bearer ' + store.state.auth.access_token;
          // retry the original reqeust with updated header
          return axios(original_request);
        }
      })
    }
    return Promise.reject(error);
  }
)

export default axios;