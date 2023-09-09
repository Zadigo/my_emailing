<template>
  <intro-wrapper :image="image" :opacity="opacity">
    <div class="d-flex justify-content-center align-items-center text-center h-100 text-light">
      <div class="col-6">
        <h1>The Mortgage Process Simplified</h1>
        <p>Our online tools connect you with the financing you need.</p>

        <div class="d-flex justify-content-center align-items-center text-center text-light mt-5">
          <div class="p-5 border-end bg-dark" style="background-color:rgba(258,258,258,1);opacity:.75;width:600px;border-top-left-radius: .5em;border-bottom-left-radius: .5em;">
            <p class="m-0">3 Year Fixed</p>
            <p class="fw-bold fs-2">2.44%</p>
            <router-link :to="{ name: 'home_view' }" class="link-light"><u>Get this rate</u></router-link>
          </div>

          <div class="p-5 border-end bg-dark" style="background-color:rgba(258,258,258,1);opacity:.75;width:600px;">
            <p class="m-0">5 Year Fixed</p>
            <p class="fw-bold fs-2">2.44%</p>
            <router-link :to="{ name: 'home_view' }" class="link-light"><u>Get this rate</u></router-link>
          </div>

          <div class="p-5 bg-dark" style="background-color:rgba(258,258,258,1);opacity:.75;width:600px;border-top-right-radius: .5em;border-bottom-right-radius: .5em;">
            <p class="m-0">10 Year Fixed</p>
            <p class="fw-bold fs-2">2.44%</p>
            <router-link :to="{ name: 'home_view' }" class="link-light"><u>Get this rate</u></router-link>
          </div>
        </div>
      </div>
    </div>
  </intro-wrapper>
</template>

<script>
import IntroWrapper from './IntroWrapper.vue'

export default {
  name: 'MultipleHero',
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
