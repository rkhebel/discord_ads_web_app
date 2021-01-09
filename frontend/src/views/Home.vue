<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          src="../assets/logo.png"
          class="my-3"
          contain
          height="200"
        />
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">
          Welcome to Discord Ads!
        </h1>
      </v-col>
    </v-row>
    <v-row class="text-center">
      <v-col>
        <v-btn class="mr-4" @click.stop="login_dialog = true">
          <span class="mr-2">Log In</span>
          <v-icon>mdi-login</v-icon>
        </v-btn>

        <v-btn @click.stop="signup_dialog = true">
          <span class="mr-2">Sign Up</span>
          <v-icon>mdi-clipboard-account</v-icon>
        </v-btn>

      </v-col>
    </v-row>

    <v-dialog
      v-model="signup_dialog"
      width="50%"
    >
      <v-card>
        <v-card-actions>  
          <v-btn
            @click="signup_dialog = false"
            to="/advertiser/signup"
          >
            Advertiser Sign Up
          </v-btn>

          <v-spacer />

          <v-btn
            @click="signup_dialog = false"
            to="/discord/signup"
          >
            Discord Sign Up
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog
      v-model="login_dialog"
      width="50%"
    >
      <v-card>
        <v-card-actions>  
          <v-btn
            @click="login_dialog = false"
            to="/advertiser/login"
          >
            Advertiser Login
          </v-btn>

          <v-spacer />

          <v-btn
            @click="login_dialog = false"
            to="discord/login"
          >
            Discord Login
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
  export default {
    name: 'Home',
    data() {
      return {
        signup_dialog: false,
        login_dialog: false
      }
    }
  }
</script>
