<template>
  <intro-wrapper :image="image" :opacity="opacity">
    <div class="d-flex justify-content-left gap-5 mx-5 h-100 align-items-center">
      <div class="col-3 text-light">
        <p class="text-muted fw-bold text-uppercase mb-2">Get started within 2 minutes</p>
        <h1 class="fs-3">Learn How To Bake In 5 Easy Steps</h1>
        <p class="mt-4">In order to discuss the general function of the logo, we must firstly identify and define the environment.</p>
      </div>

      <div class="col-4">
        <base-card class="p-4 bg-dark">
          <template #body>
            <form @submit.prevent>
              <base-input id="name" class="p-3" />
              <base-input id="surname" class="my-3 p-3" />
              <base-input id="email" class="p-3" />

              <button type="button" class="btn btn-primary btn-block mt-3 p-3">
                Download E-book now
              </button>

              <p class="text-muted mt-4">
                * We don't share your personal info with anyone.
                Check out our <router-link :to="{ name: 'home_view' }">Privacy Policy.</router-link>
              </p>
            </form>
          </template>
        </base-card>
      </div>
    </div>
  </intro-wrapper>
</template>

<script>
import IntroWrapper from './IntroWrapper.vue'

export default {
  name: 'FormHero',
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
