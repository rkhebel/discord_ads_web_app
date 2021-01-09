//This file provides a helper function that finds the jwt access token in local storage and 
//appends it to the request header so we can make api requests!

export default function authHeader() {
  let access_token = JSON.parse(localStorage.getItem('access_token'));

  if (access_token) {
    return { Authorization: 'Bearer ' + access_token };
  } else {
    return {};
  }
}