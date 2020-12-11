<template>
  <v-app>
    <v-app-bar
      app
    >
      <div class="d-flex align-center mr-4">
        <v-img
          alt="Discord Ads Logo"
          contain
          src="./assets/logo.png"
          transition="scale-transition"
          width="40"
        />
      </div>

      <div class="float-right">
      <v-toolbar-title>Discord Ads</v-toolbar-title>
      </div>

    </v-app-bar>
    <v-main>
      <Home/>
    </v-main>
  </v-app>
</template>

<script>
import Home from './components/Home.vue';

export default {
  name: 'App',

  components: {
    Home,
  },

  data() {
  }
};
</script>
