import Vue from 'vue'
import Router from 'vue-router'
import store from './store' // (1)ログイン情報を参照するため

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: () => import('./views/Mypage.vue'),
      meta: { requiresAuth: true } // マイページはログイン認証が必要
    },
    {
      path: '/signin',
      component: () => import('./views/Signin.vue')
    },
    {
      path: '/signup',
      component: () => import('./views/Signup.vue')
    },
    {
      path: '/confirm-registar',
      component: () => import('./views/ConfirmRegistration.vue')
    },
    {
      path: '/change-password',
      component: () => import('./views/ChangePassword.vue')
    },
    {
      path: '/register-creditcard',
      component: () => import('./views/RegisterCreditcard.vue')
    },
    {
      path: '/about-codefolio',
      component: () => import('./views/AboutCodeFolio.vue')
    },
    {
      path: '/qa',
      component: () => import('./views/QandA.vue')
    },
    // 利用規約
    {
      path: '/terms-conditions',
      component: () => import('./views/TermsConditions.vue')
    },
    // プライバシーポリシー
    {
      path: '/privacy-policy',
      component: () => import('./views/PrivacyPolicy.vue')
    }
  ]
});

// (3)
router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!store.getters.loggedIn) {
      next({
        path: '/signin'
      })
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router;
