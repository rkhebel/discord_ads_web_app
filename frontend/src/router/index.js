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
    component: AdvertiserHome
  },
  {
    path: '/discord/',
    component: DiscordHome
  }
];

const router = new VueRouter({
  routes
});

router.beforeEach((to, from, next) => {
  const publicPages = ['/', '/advertiser/login', '/advertiser/signup', '/discord/login', '/discord/signup'];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = store.state.auth.status.loggedIn;

  if (authRequired && !loggedIn) {
    next('/');
  } else {
    next();
  }
});

export default router;
