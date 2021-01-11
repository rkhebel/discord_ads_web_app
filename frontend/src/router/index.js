import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import AdvertiserLogin from '../views/AdvertiserLogin.vue';
import AdvertiserSignup from '../views/AdvertiserSignup.vue';
import DiscordLogin from '../views/DiscordLogin.vue';
import DiscordSignup from '../views/DiscordSignup';
import AdvertiserHome from '../views/AdvertiserHome';
import DiscordHome from '../views/DiscordHome';
import store from '../store';
import LoginPage from '../views/LoginPage';
import SignupPage from '../views/SignupPage';
import ForbiddenPage from '../views/ForbiddenPage'

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
      requireAuth: true
    }
  },
  {
    path: '/discord/',
    component: DiscordHome,
    meta: {
      requireAuth: true
    }
  },
  {
    path: '/forbidden',
    component: ForbiddenPage
  }
];

const router = new VueRouter({
  routes
});

//check to see if we're logged in before accessing restricted pages
router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requireAuth)) {
    if (store.state.auth.loggedIn) {
      next()
      return
    }
    next('/forbidden')
  } else {
    next()
  }
});

export default router;
