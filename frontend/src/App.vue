<template>
  <v-app>
    <DefaultNav v-if="!loggedIn"></DefaultNav>
    <AuthenticatedNav v-if="loggedIn" :user_type="userType"></AuthenticatedNav>
    <v-main>
          <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import DefaultNav from './components/shared/DefaultNav'
import AuthenticatedNav from './components/shared/AuthenticatedNav'

export default {
  name: 'App',
  components: {
    DefaultNav,
    AuthenticatedNav
  },
  data() {
    return  {
    }
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.loggedIn;
    },
    userType() {
      return this.$store.state.auth.user_type;
    },
  },
}
</script>

<style>
a {
  text-decoration: none;
}
</style>