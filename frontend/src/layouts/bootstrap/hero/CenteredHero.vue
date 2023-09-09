<template>
  <intro-wrapper :image="image" :opacity="opacity">
    <div class="d-flex justify-content-center align-items-center h-100 text-center">
      <div class="text-white">
        <h1 class="mb-3 display-3 fw-bold">Simple Vue Bootstrap templates</h1>
        <h4 class="mb-3 fw-light">A simple VueJS projects for template demonstrations</h4>
  
        <router-link :to="{ name: 'buttons_view' }" class="btn btn-primary btn-lg mt-4 btn-rounded">
          Bootstrap templates
        </router-link>
  
        <div class="d-flex justify-content-center align-items-center gap-5 text-center mt-5">
          <img :src="require('@/assets/brands/brand1.webp')" alt="Brand1">
          <img :src="require('@/assets/brands/brand2.webp')" alt="Brand2">
          <img :src="require('@/assets/brands/brand3.webp')" alt="Brand3">
        </div>
      </div>
    </div>
  </intro-wrapper>
</template>

<script>
import IntroWrapper from './IntroWrapper.vue'

export default {
  name: 'CenteredHero',
  components: {
    IntroWrapper
  },
  props: {
    image: {
      type: String,
      required: true
    },
    opacity: {
      type: Number,
      default: 0.3
    }
  }
}
</script>
