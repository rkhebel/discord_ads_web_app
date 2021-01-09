<template>
  <v-container>
    <SignupForm user_type='advertiser'> </SignupForm>
  </v-container> 
</template>

<script>
  import SignupForm from '../components/SignupForm.vue'
  export default {
    name: 'AdvertiserSignup',
    components: {
      SignupForm
    }
  }
</script>