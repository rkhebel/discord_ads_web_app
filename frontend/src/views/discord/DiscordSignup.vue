<template>
  <v-container>
    <SignupForm user_type='discord'> </SignupForm>
  </v-container> 
</template>

<script>
  import SignupForm from '../../components/shared/SignupForm.vue'
  export default {
    name: 'DiscordSignup',
    components: {
      SignupForm
    }
  }
</script>