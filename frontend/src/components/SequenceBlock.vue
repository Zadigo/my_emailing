<template>
  <div id="sequence-block">
    <base-card v-if="showExplicitResult" id="date" class="shadow-sm" @click="$emit('expand-preview', sequence)">
      <template #body>
        <p><span class="badge text-bg-light">Object:</span> {{ replacePlaceholders(sequence.email_object, previewedLead) }}</p>
        <p><span class="badge text-bg-light">Text:</span> {{ replacePlaceholders(sequence.email_text, previewedLead) }}</p>
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
import { useEmailUtilities } from '../composables/emailing'

import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'
import DateSequence from './DateSequence.vue'
import EmailSequence from './EmailSequence.vue'

export default {
  components: {
    BaseCard,
    DateSequence,
    EmailSequence
  },
  inject: ['previewEmail'],
  props: {
    sequence: {
      type: Object,
      required: true
    },
    showExplicitResult: {
      type: Boolean
    },
    previewedLead: {
      type: Object,
      required: false
    }
  },
  emits: {
    'expand-preview' () {
      return true
    }
  },
  setup () {
    const app = getCurrentInstance()
    const { replacePlaceholders } = useEmailUtilities()
    provide('showExplicitResult', app.props.showExplicitResult)
    
    return {
      replacePlaceholders
    }
  }
}
</script>
