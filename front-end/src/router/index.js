import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Register from '@/components/register'
import intro from '@/components/intro/IntroTitle'
import ADI from '@/components/intro/ADI'
import ts from '@/components/intro/ts'
import hdc from '@/components/intro/hdc'
import edc from '@/components/intro/edc'
import cc from '@/components/intro/cc'
import sp from '@/components/intro/sp'


Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    /*{
      path: '/join',
      name: 'Join',
      component: Register
    },*/
    {
      path: '/intro',
      component: intro,
    },
    {
      path: '/intro/ADI',
      component: ADI
    },
    {
      path: '/intro/ts',
      component: ts
    },
    {
      path: '/intro/hdc',
      component: hdc
    },
    {
      path: '/intro/edc',
      component: edc
    },
    {
      path: '/intro/cc',
      component: cc
    },
    {
      path: '/intro/sp',
      component: sp
    }
  ]
})
