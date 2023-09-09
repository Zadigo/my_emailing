<template>
  <section id="campaign">
    <div class="text-center mb-5">
      <!-- Start -->
      <base-card id="sequence" class="shadow-sm">
        <template #body>
          Start
        </template>
      </base-card>
    </div>

    <!-- Sequence -->
    <sequence-block v-for="(sequence, i) in sequences" :key="sequence.sequence_id" :sequence="sequence" :class="{ 'mt-5': i >= 1 }" />

    <!-- Add -->
    <div class="col-12 d-flex justify-content-center mt-5">
      <base-button color="primary" rounded @click="handleNewSequence">
        Add
      </base-button>
    </div>
  </section>
</template>

<script>
import _ from 'lodash'

import { mapState } from 'pinia'
import { useCampaigns } from '../../store'

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
    return {
      store
    }
  },
  data () {
    return {
      
    }
  },
  computed: {
    ...mapState(useCampaigns, { sequences: 'currentCampaignSequences' })
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
