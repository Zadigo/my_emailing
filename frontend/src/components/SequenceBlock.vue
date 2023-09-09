<template>
  <div id="sequence-block">
    <!-- Email -->
    <email-sequence :sequence="sequence" />

    <!-- Date -->
    <date-sequence :sequence="sequence" class="mt-2" />
  </div>
</template>

<script>
import DateSequence from './DateSequence.vue'
import EmailSequence from './EmailSequence.vue'
export default {
  components: {
    DateSequence,
    EmailSequence
  },
  props: {
    sequence: {
      type: Object,
      required: true
    }
  },
  setup () {
    return {
      
    }
  }
}
</script>
