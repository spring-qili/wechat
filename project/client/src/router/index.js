import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Userlist from '@/components/Userlist'
import UnNormal from '@/components/UnNormal'

Vue.use(Router)
// 一个路由对应一个component（组件）
export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/user',
      name: 'Userlist',
      component: Userlist
    },
    {
      path: '/unnormal',
      name: 'UnNormal',
      component: UnNormal
    },
  ]
})