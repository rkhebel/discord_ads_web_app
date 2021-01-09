import authHeader from './auth-header';

const API_URL = 'http://localhost:5000/discord/';

class DiscordService {

  getProfile() {
    fetch(API_URL + 'profile', {
      method: 'GET',
      headers: {
        authHeader
      }
    }).then(response => {
      response.json();
    }).then(result => {
        return result;
    });
  }

}

export default new DiscordService();