import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const store =  new Vuex.Store({
  state: {
    userId: '',
    accessToken: '',
    idToken: ''
  },
  getters: {
    loggedIn: (state) => {
      return Boolean(state.accessToken.trim())
    },
    userId: (state) => {
      return state.userId
    },
    accessToken: (state) => {
      return state.accessToken
    },
    idToken: (state) => {
      return state.idToken
    }
  },
  mutations: {
    setUserId(state, userId) {
      state.userId = userId
    },
    setAccessToken(state, accessToken) {
      state.accessToken = accessToken
    },
    setIdToken(state, idToken) {
      state.idToken = idToken
    }
  },
  actions: {},
  plugins: [createPersistedState()]
})

export default store;