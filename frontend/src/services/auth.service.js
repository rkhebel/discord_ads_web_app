// This file contains methods that perform auth functions by connecting to the api.
// User data is stored in local storage

const API_URL = 'http://localhost:5000/auth/';

class AuthService {
  login(user) {
    let login_url = API_URL + 'login';
    return fetch(login_url, {
      method: 'POST',
      headers: {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        email: user.email,
        password: user.password,
        user_type: user.type
      })
    }).then(response => {
      return response.json();
    }).then(responseJSON => {
      if (responseJSON['access_token']) {
        localStorage.setItem('access_token', JSON.stringify(responseJSON['access_token']));
      }
      return responseJSON;
    }).catch(error => {
      console.log(error);
    });
  }

  logout() {
    localStorage.removeItem('access_token');
  }

  signup(user) {
    let register_url = API_URL + 'signup';
    return fetch(register_url, {
      method: 'POST',
      headers: {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        first_name: user.first_name,
        last_name: user.last_name,
        email: user.email,
        password: user.password,
        user_type: user.type
      })
    }).then(response => {
      return response.json();
    }).then(responseJSON => {
      return responseJSON;
    }).catch(error => {
      console.log(error);
    })
  }
}

export default new AuthService();
