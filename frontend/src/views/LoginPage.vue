<template>
  <v-container>
    <v-row align="center" style="height: 150px;" justify="space-around">
      <v-btn to="/advertiser/login" >
        Advertiser Log In
      </v-btn>

      <v-btn to="discord/login" >
        Discord Log In
      </v-btn>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'LoginPage',
  components: {

  }
}
</script>