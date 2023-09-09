<template>
  <div id="sequence-block">
    <base-card v-if="showExplicitResult" id="date" class="shadow-sm">
      <template #body>
        <p>Object: {{ sequence.email_object }}</p>
        <p>Text: {{ sequence.email_text }}</p>
      </template>
    </base-card>

    <!-- Email -->
    <email-sequence v-else :sequence="sequence" />

    <!-- Date -->
    <base-card v-if="showExplicitResult" id="date" class="mt-2 shadow-sm">
      <template #body>
        Wait for {{ sequence.number_of_days }} days
      </template>
    </base-card>

    <!-- Date -->
    <date-sequence v-else :sequence="sequence" class="mt-2" />
  </div>
</template>

<script>
import { getCurrentInstance, provide } from 'vue'

import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'
import DateSequence from './DateSequence.vue'
import EmailSequence from './EmailSequence.vue'

export default {
  components: {
    BaseCard,
    DateSequence,
    EmailSequence
  },
  inject: ['previewEmail', 'previewForLead'],
  props: {
    sequence: {
      type: Object,
      required: true
    },
    showExplicitResult: {
      type: Boolean
    }
  },
  setup () {
    const app = getCurrentInstance()
    provide('showExplicitResult', app.props.showExplicitResult)

    return {}
  },
  computed: {
    previewedEmailObject () {
      if (this.previewEmail) {
        const variableRegex = new RegExp(/\[\[\s?(\w+)\s?\]\]/g)
        const result = variableRegex.exec(this.sequence.email_object)
        const newString = this.sequence.email_object
        newString.replace(result[0], this.previewForLead[result[1]])
        return newString
      } else {
        return this.sequence.email_object
      }
    }
  },
}
</script>
