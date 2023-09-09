<template>
  <intro-wrapper :image="image" :opacity="opacity">
    <div class="d-flex justify-content-start align-items-center h-100 text-light text-right">
      <div class="col-6 mx-5">
        <h1 class="mb-3 display-4 fw-bold">
          Education costs money. But then so does ignorance
        </h1>
        <p class="mb-3 fw-light fs-5">
          Before cell phones became so popular, watches were much more
          attractive to carry around because they are the most convenient way
          to keep track of the time.
        </p>
        <router-link :to="{ name: 'buttons_view' }" class="btn btn-primary btn-lg mt-3">
          Bootstrap templates
        </router-link>
      </div>
    </div>

  </intro-wrapper>
</template>

<script>
import IntroWrapper from './IntroWrapper.vue'

export default {
  name: 'LeftHero',
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
