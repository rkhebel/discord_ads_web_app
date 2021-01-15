import axios from './axios.service'

const API_URL = process.env.VUE_APP_API_URL + 'discord/';

class DiscordService {

  getProfile() {
    let url = API_URL + 'profile'
    return axios.get(url).then(response => {
      return response.data;
    }).catch(error => {
      console.log(error);
      return Promise.reject(error);
    });
  }


}

export default new DiscordService();