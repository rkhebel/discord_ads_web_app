<template>
  <v-container>
    <v-card>
      <v-card-title>Login</v-card-title>
      <v-card-text>
        <v-form>
          <v-text-field 
            label="Email"
            v-model="user.email"
            required
          ></v-text-field>
          <v-text-field 
            label="Password"
            v-model="user.password"
            type="password"
            required
          ></v-text-field>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-btn
          @click="login"
        > Log In </v-btn>
      </v-card-actions>
    </v-card>
    <v-dialog v-model="dialog">
      <v-card>
        <v-card-text>
          {{dialog_text}}
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-container> 
</template>

<script>
import User from '../models/user';

  export default {
    name: 'LoginForm',
    props: ['user_type'],
    data() {
      return {
        user: new User('', '', this.user_type),
        dialog: false,
        dialog_text: ''
      }
    },
    computed: {
      loggedIn() {
        return this.$store.state.auth.status.loggedIn;
      }
    },
    created() {
      if (this.loggedIn) {
        this.$router.push('/'+this.user_type+'/');
      }
    },
    methods: {
      login() {
        if (this.user.email && this.user.password, this.user_type) {
          this.$store.dispatch('auth/login', this.user).then ( response => {
            if (!response['error']) {
              this.$router.push('/'+this.user_type+'/');
            }
            else {
              this.dialog = true;
              this.dialog_text = response['error'];
            }
          },
          error => {
            // something happens on error, probably display message
            console.log(error);
          });
        }
      }
    }
  }
</script>