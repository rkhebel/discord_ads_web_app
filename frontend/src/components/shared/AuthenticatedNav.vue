// nav bar that's shown when the user is logged in

<template>
  <div>
    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = true">
      </v-app-bar-nav-icon>
      <router-link :to="userHome">
        <v-img
          class="mr-2"
          alt="Discord Ads Logo"
          src="../../assets/logo.png"
          contain
          max-height="40"
          max-width="40"
        />
      </router-link>
      <v-toolbar-title>{{user_type}}</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn class="mr-4" @click="logout">
        <span class="mr-2">Logout</span>
        <v-icon>mdi-logout</v-icon>
      </v-btn>
    </v-app-bar>
    <v-navigation-drawer 
    v-model="drawer" 
    temporary 
    absolute
    >
      <AdvertiserNavigationList v-if="isAdvertiser"></AdvertiserNavigationList>
      <DiscordNavigationList v-if="isDiscord"></DiscordNavigationList>
    </v-navigation-drawer>
  </div>
</template>

<script>
import AdvertiserNavigationList from '../advertiser/AdvertiserNavigationList'
import DiscordNavigationList from '../discord/DiscordNavigationList'

export default {
  name: 'AuthenticatedNav',
  props: ['user_type'],
  components: {
    AdvertiserNavigationList,
    DiscordNavigationList
  },
  data() {
    return {
      drawer: false
    }
  },
  computed: {
    isAdvertiser() {
      return this.$store.state.auth.user_type == 'advertiser';
    },
    isDiscord() {
      return this.$store.state.auth.user_type == 'discord';
    },
    userHome() {
      return '/' + this.$store.state.auth.user_type;
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('auth/logout').then(response => {
        if (!response['error']) {
          this.$router.push('/')
        }
      }).catch(() => {
        // do nothing for now
      })
    }
  }
}
</script>