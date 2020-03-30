// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
// 正常语法应该是./router/index.js,由于webpack，所以可以直接写
import router from './router'
// import store from './store'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.config.productionTip = false

// 在store中全局管理整个组件的状态信息，一个变量改变，所有使用该变量的组件都会相应更新
import Vuex from 'vuex'
Vue.use(Vuex);
Vue.use(ElementUI)

const store = new Vuex.Store({
  state: {
    userList: [],
    unNormallist: []
  },
  getters: {
    userList: state => {
      return state.userList
    },
    unNormallist: state => {
      return state.unNormallist
    }
  },
  mutations: {
    changeUserList(state, list) {
      console.log("change!!!")
      state.userList = list
      console.log(state.userList)
    },
    changeUnNormalUser(state, list) {
      console.log("change2!!!")
      state.unNormallist = list
      console.log(state.unNormallist)
    }
  }
})



/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
