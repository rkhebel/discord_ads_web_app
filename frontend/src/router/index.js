import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/shared/Home.vue';
import AdvertiserLogin from '../views/advertiser/AdvertiserLogin.vue';
import AdvertiserSignup from '../views/advertiser/AdvertiserSignup.vue';
import DiscordLogin from '../views/discord/DiscordLogin.vue';
import DiscordSignup from '../views/discord/DiscordSignup';
import AdvertiserHome from '../views/advertiser/AdvertiserHome';
import DiscordHome from '../views/discord/DiscordHome';
import store from '../store';
import LoginPage from '../views/shared/LoginPage';
import SignupPage from '../views/shared/SignupPage';
import ForbiddenPage from '../views/shared/ForbiddenPage'
import InvalidPermissionsPage from '../views/shared/InvalidPermissionsPage'

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '*',
    redirect: '/'
  },
  {
    path: '/login',
    component: LoginPage
  },
  {
    path: '/signup',
    component: SignupPage
  },
  {
    path: '/advertiser/login',
    component: AdvertiserLogin
  },
  {
    path: '/advertiser/signup',
    component: AdvertiserSignup
  },
  {
    path: '/discord/login',
    component: DiscordLogin
  },
  {
    path: '/discord/signup',
    component: DiscordSignup
  },
  {
    path: '/advertiser/',
    component: AdvertiserHome,
    meta: {
      requireAuth: true,
      permissions: ['advertiser']
    }
  },
  {
    path: '/discord/',
    component: DiscordHome,
    meta: {
      requireAuth: true,
      permissions: ['discord']
    }
  },
  {
    path: '/forbidden',
    component: ForbiddenPage
  },
  {
    path: '/invalidpermissions',
    component: InvalidPermissionsPage
  }
];

const router = new VueRouter({
  routes
});

//check to see if we're logged in before accessing restricted pages
router.beforeEach((to, from, next) => {
  // check if auth is required
  if(to.matched.some(record => record.meta.requireAuth)) {
    // check if we're logged in
    if (store.state.auth.loggedIn) {
      // check if we have permissions
      if (to.meta.permissions.includes(store.state.auth.user_type)) {
        next();
      }
      else {
        // if no permissions, redirect to their home
        next('/invalidpermissions');
      }
    }
    else {
      // if not logged in , redirect to forbidden
      next('/forbidden');
    }
  } else {
    // if no auth required, just go
    next();
  }
});

export default router;
