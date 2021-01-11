<template>
  <v-app>
    <v-app-bar app v-if="!loggedIn">
      <router-link to="/">
        <v-img
          class="d-flex align-center mr-4"
          alt="Discord Ads Logo"
          contain
          src="./assets/logo.png"
          transition="scale-transition"
          width="40"
        />
      </router-link>
      <v-btn class="mr-4" to="/">
        <span class="mr-2">Home</span>
        <v-icon>mdi-home</v-icon>
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn class="mr-4" to="/login">
        <span class="mr-2">Log In</span>
        <v-icon>mdi-login</v-icon>
      </v-btn>

      <v-btn to="/signup">
        <span class="mr-2">Sign Up</span>
        <v-icon>mdi-clipboard-account</v-icon>
      </v-btn>
    </v-app-bar>
    <v-app-bar app v-if="loggedIn">
      <router-link to="/">
        <v-img
          class="d-flex align-center mr-4"
          alt="Discord Ads Logo"
          contain
          src="./assets/logo.png"
          transition="scale-transition"
          width="40"
        />
      </router-link>
      <v-btn class="mr-4" to="/">
        <span class="mr-2">Home</span>
        <v-icon>mdi-home</v-icon>
      </v-btn>
      <v-spacer></v-spacer>
      <v-btn class="mr-4" @click="logout">
        <span class="mr-2">Logout</span>
        <v-icon>mdi-logout</v-icon>
      </v-btn>
    </v-app-bar>
    <v-main>
          <router-view/>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  computed: {
    loggedIn() {
      return this.$store.state.auth.loggedIn;
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('auth/logout').then(response => {
        if (!response['error']) {
          this.$router.push('/')
        }
      })
    }
  }
}
</script>

<style>
a {
  text-decoration: none;
}
</style>