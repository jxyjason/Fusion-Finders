import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Detect from "@/views/Detect";
import aDemo from "@/views/aDemo"
import SupervisoryRetrieval from "@/views/SupervisoryRetrieval";
import RemoteCare from "@/views/RemoteCare";
import AnimalDetect from "@/views/AnimalDetect";
import Submit3D from "@/views/ThreeDim/Submit3D";
import AccidentDetect from "@/views/AccidentDetect";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },

  {
    path: '/detect',
    name: 'Detect',
    component: Detect
  },
  {
    path: '/aDemo',
    name: 'aDemo',
    component: aDemo
  },
  {
    path: '/supervisoryRetrieval',
    name: 'SupervisoryRetrieval',
    component: SupervisoryRetrieval
  },
  {
    path: '/remoteCare',
    name: 'RemoteCare',
    component: RemoteCare
  },
  {
    path: '/animalDetect',
    name: 'AnimalDetect',
    component: AnimalDetect
  },
  {
    path: '/accidentDetect',
    name: 'AccidentDetect',
    component: AccidentDetect
  },
  {
    path: '/submit3D',
    name: 'Submit3D',
    component: Submit3D
  },


]

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

export default router
