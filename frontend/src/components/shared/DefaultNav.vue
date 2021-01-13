// nav bar that's shown when the user isn't logged it

<template>
  <v-app-bar app>
    <router-link to="/">
      <v-img
        class="mr-2"
        alt="Discord Ads Logo"
        src="../../assets/logo.png"
        contain
        max-height="40"
        max-width="40"
        to="/"
      />
    </router-link>
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
</template>

<script>
export default {
  name: 'DefaultNav',
}
</script>