<template>
  <v-container>
    <LoginForm user_type='advertiser'> </LoginForm>
  </v-container> 
</template>

<script>
  import LoginForm from '../../components/shared/LoginForm.vue'
  export default {
    name: 'AdvertiserLogin',
    components: {
      LoginForm
    }
  }
</script>