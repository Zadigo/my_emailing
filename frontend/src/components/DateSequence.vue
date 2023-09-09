<template>
  <base-card id="date-sequence" class="shadow-sm">
    <template #body>
      <div class="d-flex justify-content-between align-items-center">
        <div class="d-flex flex-column align-items-start">
          <span class="p-2">Wait for {{ numberOfDays }} days</span>
          <base-input id="days" v-model="numberOfDays" type="number" min="1" max="365" class="p-2" />
        </div>

        <base-button size="sm" rounded @click="handleDeleteSequence">
          Delete
        </base-button>
      </div>
    </template>
  </base-card>
</template>

<script>
import BaseButton from '@/layouts/bootstrap/buttons/BaseButton.vue';
import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'
import BaseInput from '@/layouts/bootstrap/BaseInput.vue'

export default {
  components: {
    BaseButton,
    BaseCard,
    BaseInput
  },
  props: {
    sequence: {
      type: Object,
      required: true
    }
  },
  data () {
    return {
      numberOfDays: 1
    }
  },
  created () {
    this.numberOfDays = this.sequence.days
  },
  methods: {
    async handleUpdateDays () {
      try {
        this.sequence.sequence_id
        // Pass
      } catch (e) {
        console.log(e)
      }
    },
    async handleDeleteSequence () {
      try {
        this.sequence.sequence_id
        // Pass
      } catch (e) {
        console.log(e)
      }
    }
  }
}
</script>
