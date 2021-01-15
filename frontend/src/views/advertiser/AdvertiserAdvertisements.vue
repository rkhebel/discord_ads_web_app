<template>
  <v-container>
    <h1 class="text-center display-2 font-weight-bold">
          Your ads
    </h1>

    <v-btn @click="test">Test button</v-btn>

    <v-btn to="/advertiser/advertisement/create">
      + Create Ad
    </v-btn>

    <v-data-table></v-data-table>
  </v-container>
</template>

<script>
import AdvertiserService from '../../services/advertiser.service'
//import DiscordService from '../../services/discord.service'
  export default {
    name: 'AdvertiserAdvertisements',
    data() {
      return {
      }
    },
    methods: {
      test() {
        AdvertiserService.getAdvertisements().then(response => {
          console.log(response); 
        }).catch(() => {
          // do nothing
        })
      }
    }
  }
</script>
