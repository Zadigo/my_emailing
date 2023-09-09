<template>
  <section class="dashboard">
    <div class="sidebar-overlay"></div>
    <!-- Header -->
    <header>
      <!-- Sidebar -->
      <nav id="sidebar" link="sidebar" class="collapse d-lg-block sidebar collapse bg-white">
        <div class="position-sticky">
          <keep-alive>
            <div class="list-group list-group-flush mx-3 mt-4">
              <router-link v-for="(link, i) in adminLinks" :key="i" :to="{ name: link.to }" class="list-group-item list-group-item-action py-2 ripple" aria-current="true">
                <font-awesome-icon :icon="`fa-solid fa-${link.icon}`" class="me-3" />
                <span>{{ link.title }}</span>
              </router-link>
            </div>
          </keep-alive>
        </div>
      </nav>

      <!-- Navbar -->
      <nav id="main-navbar" class="navbar navbar-expand-lg navbar-light bg-white fixed-top">
        <div class="container-fluid">
          <button class="navbar-toggler" type="button" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation">
            <i class="fas fa-bars"></i>
          </button>

          <router-link to="/" class="navbar-brand">
            <div class="fw-bold text-uppercase">Templates</div>
            <!-- <img src="https://mdbootstrap.com/img/logo/mdb-transaprent-noshadows.png" height="25" loading="lazy" alt="Image 4" /> -->
          </router-link>

          <ul class="navbar-nav ms-auto d-flex flex-row">
            <nav-item :to="{ name: 'home_view' }" link-name="Some link" />
          </ul>
        </div>
      </nav>
    </header>

    <!-- Main -->
    <main>
      <div :class="bodyClasses" class="container pt-4">
        <router-view></router-view>
      </div>
    </main>

    <transition name="pop">
      <button v-if="!arrivedState.top" id="back-to-top" class="btn btn-primary btn-floating" type="button" @click="scrollToTop">
        <font-awesome-icon icon="fa-solid fa-arrow-up" />
      </button>
    </transition>
  </section>
</template>

<script>
// import _ from 'lodash'

import { ref } from 'vue'
// import { useDarkMode } from '@/composables/darkmode'
import { scrollToTop } from '@/composables/utils'
import { useScroll } from '@vueuse/core'

import NavItem from '@/layouts/bootstrap/nav/NavItem.vue'

export default {
  name: 'DashboardLayout',
  components: {
    NavItem
  },
  props: {
    bodyClasses: {
      type: String,
      required: false
    }
  },
  setup () {
    const target = ref(null)
    const { y, arrivedState } = useScroll(target)
    // const { darkMode } = useDarkMode()
    // provide('darkMode', darkMode)
    return {
      // darkMode,
      target,
      scrollToTop,
      scrollY: y,
      arrivedState
    }
  },
  computed: {
    adminLinks () {      
      // const result = _.map(this.$router.getRoutes(), function (link) {
      //   if (link.meta.adminLink) {
      //     return { title: link.meta.title, to: link.name, icon: link.meta.icon }
      //   }
      //   return null
      // })
      // return _.filter(result, function (item) { 
      //   return item !== null
      // })
      return [
        {
          title: 'Campaigns',
          to: 'home_view',
          icon: 'table'
        }
      ]
    }
  },
  mounted () {
    document.body.classList.remove('bg-white')
    document.body.classList.add('bg-light')
    this.target = window.document
  }
}
</script>

<style scoped>
@import url('@/layouts/bootstrap/css/dashboard1.css');
</style>
