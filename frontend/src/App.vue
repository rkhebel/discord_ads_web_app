<template>
  <v-app>
    <v-app-bar app>
      <div class="d-flex align-center mr-4">
        <router-link to="/">
          <v-img
            alt="Discord Ads Logo"
            contain
            src="./assets/logo.png"
            transition="scale-transition"
            width="40"
          />
        </router-link>
      </div>
      <div class="float-right">
        <v-toolbar-title>Discord Ads</v-toolbar-title>
      </div>
    </v-app-bar>
    <v-main>
          <router-view/>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  components: {

  }
}
</script>