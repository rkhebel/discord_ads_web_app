<template>
  <v-container>
    <SignupForm user_type='advertiser'> </SignupForm>
  </v-container> 
</template>

<script>
  import SignupForm from '../../components/shared/SignupForm.vue'
  export default {
    name: 'AdvertiserSignup',
    components: {
      SignupForm
    }
  }
</script>