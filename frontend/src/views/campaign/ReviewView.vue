<template>
  <section id="leads">
    <div class="row">
      <div class="col-6">
        <base-card class="shadow-sm">
          <template #body>
            <div v-if="leadsCount > 0" class="list-group">
              <a v-for="lead in leads" :key="lead.id" href class="list-group-item list-group-item-action p-3 d-flex justify-content-between align-items-center" @click.prevent="handlePreviewEmail(lead)">
                <span>{{ lead.email }}</span>
                <base-button id="cta-review-lead" size="sm" color="secondary" rounded @click="handleReviewLead(lead)">
                  Review
                </base-button>
              </a>
            </div>

            <div v-else class="text-center">
              <h2 class="h4">All leads are reviewed</h2>
              <p class="">No leads are waiting to be reviewed</p>

              <base-button id="cta-add-leads mt-5" color="primary" rounded>
                Add leads to this campaign
              </base-button>
            </div>
          </template>
        </base-card>
      </div>
      
      <div class="col-6">
        <sequence-block v-for="(sequence, i) in sequences" :key="sequence.sequene_id" :sequence="sequence" :class="{ 'mt-5': i >= 1 }" show-explicit-result />
      </div>
    </div>
  </section>
</template>

<script>
import { useCampaigns } from '../../store'
import { mapState } from 'pinia'
import { provide, ref } from 'vue'

import BaseButton from '@/layouts/bootstrap/buttons/BaseButton.vue'
import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'
import SequenceBlock from '@/components/SequenceBlock.vue'

export default {
  components: {
    BaseButton,
    BaseCard,
    SequenceBlock
  },
  setup () {
    const store = useCampaigns()
    const previewEmail = ref(true)
    const previewForLead = ref({})

    provide('previewEmail', previewEmail)
    provide('previewForLead', previewForLead)

    return {
      previewEmail,
      previewForLead,
      store
    }
  },
  computed: {
    ...mapState(useCampaigns, { 
      leads: 'unreviewedLeads', 
      leadsCount: 'unreviewedLeadsCount',
      sequences: 'currentCampaignSequences'
    })
  },
  methods: {
    async handleReviewLead (lead) {
      try {
        lead.reviewed = true
      } catch (e) {
        console.log(e)
      }
    },
    handlePreviewEmail (lead) {
      this.previewEmail = !this.previewEmail
      if (this.previewEmail) {
        this.previewForLead = lead
      } else {
        this.previewForLead = {}
      }
    }
  }
}
</script>
