<template>
  <section id="campaign">
    
    <!-- Sequence -->
    <div v-if="hasSequences" class="sequence-blocks">
      <div class="text-center mb-5">
        <!-- Start -->
        <base-card id="sequence" class="shadow-sm">
          <template #body>
            Start
          </template>
        </base-card>
      </div>

      <sequence-block v-for="(sequence, i) in sequences" :key="sequence.sequence_id" :sequence="sequence" :class="{ 'mt-5': i >= 1 }" />
  
      <!-- Add -->
      <div class="col-12 d-flex justify-content-center mt-5">
        <base-button color="primary" rounded @click="handleNewSequence">
          Add
        </base-button>
      </div>
    </div>

    <div v-else class="choose-sequence-block">
      <base-card class="shadow-sm">
        <template #body>
          <h2 class="h4">Choose how to build your sequence</h2>
          <p class="fw-light">Start by choosing your sequence's first step</p>
        </template>
      </base-card>
    </div>
  </section>
</template>

<script>
import _ from 'lodash'

import { mapState } from 'pinia'
import { useCampaigns } from '../../store'
import { provide } from 'vue'

import BaseButton from '@/layouts/bootstrap/buttons/BaseButton.vue'
import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'
import SequenceBlock from '@/components/SequenceBlock.vue'

export default {
  components: {
    BaseCard,
    BaseButton,
    SequenceBlock
  },
  setup () {
    const store = useCampaigns()

    provide('previewEmail', false)
    
    return {
      store
    }
  },
  computed: {
    ...mapState(useCampaigns, { sequences: 'currentCampaignSequences' }),
    ...mapState(useCampaigns, ['hasSequences'])
  },
  beforeMount () {
    // if (!this.store.hasCampaigns) {
    //   this.store.getCampaigns()
    //   setTimeout(() => {
    //     this.store.getCurrentCampaign(this.$route.params.id)
    //   }, 300)
    // }
      this.store.reloadCampaigns(this.$route.params.id)
  },
  methods: {
    async handleNewSequence () {
      try {
        const lastItem = _.last(this.sequences)
        this.store.currentCampaign.sequences.push({
          id: lastItem.id + 1,
          sequence_id: 'seq_12345545',
          email_object: 'Some simple object',
          text: "Some text for me",
          html_text: "Some html text for you",
          days: 3
        })
      } catch (e) {
        console.log(e)
      }
    }
  }
}
</script>

<style scoped>
.separator::before {
  content: "";
  width: 10px;
  height: 100px;
  background-color: black;
}
</style>
