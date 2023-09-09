<template>
  <section id="campaign">
    <div class="text-center mb-5">
      <base-card id="sequence" class="shadow-sm">
        <template #body>
          Start
        </template>
      </base-card>
    </div>

    <div v-for="(sequence, i) in sequences" :key="i" :class="{ 'mt-5': i >= 1 }" class="text-center">
      <template v-for="(item, y) in sequence.items" :key="y">
        <component :is="item.component" :class="{ 'mt-2': y >= 1 }" :sequence="sequence" :item="item" />
      </template>
    </div>

    <div class="col-12 d-flex justify-content-center mt-5">
      <base-button color="primary" rounded @click="handleNewSequence">
        Add
      </base-button>
    </div>
  </section>
</template>

<script>
import _ from 'lodash'
import BaseButton from '@/layouts/bootstrap/buttons/BaseButton.vue'
// import BaseCheckbox from '@/layouts/bootstrap/BaseCheckbox.vue'
import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'
import EmailSequence from '@/components/EmailSequence.vue'
import DateSequence from '@/components/DateSequence.vue'
import { useCampaigns } from '../../store'
import { mapState } from 'pinia'
export default {
  components: {
    BaseCard,
    BaseButton,
    EmailSequence,
    DateSequence,
    // BaseCheckbox
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
    ...mapState(useCampaigns, {sequences: 'currentCampaignSequences' })
  },
  beforeMount () {
    this.store.getViewedCampaign(this.$route.params.id)
  },
  methods: {
    async handleNewSequence () {
      try {
        const lastItem = _.last(this.sequences)
        this.store.currentCampaign.sequences.push({
          id: lastItem.id + 1,
          items: [
            {
              email_object: 'Some simple object',
              component: 'email-sequence'
            },
            {
              days: 5,
              component: 'date-sequence'
            }
          ]
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
