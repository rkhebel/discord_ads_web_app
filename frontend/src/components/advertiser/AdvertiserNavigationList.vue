<template>
  <v-list-item-group>
    <v-list 
    nav
    dense
    >
      <v-list-item to="/advertiser">
        <v-list-item-icon>
          <v-icon>mdi-chart-line</v-icon>
        </v-list-item-icon>
        <v-list-item-title>Dashboard</v-list-item-title>
      </v-list-item>
    </v-list>
  </v-list-item-group>
</template>

<script>
export default {
  name: "AdvertiserNavigationList",
}
</script>