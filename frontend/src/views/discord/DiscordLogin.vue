<template>
  <v-container>
    <LoginForm user_type='discord'> </LoginForm>
  </v-container> 
</template>

<script>
  import LoginForm from '../../components/shared/LoginForm.vue'
  export default {
    name: 'DiscordLogin',
    components: {
      LoginForm
    }
  }
</script>