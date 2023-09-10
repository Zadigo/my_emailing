<template>
  <section id="leads">
    <div class="row">
      <div class="col-6">
        <base-card class="shadow-sm">
          <template #body>
            <!-- Leads -->
            <div v-if="leadsCount > 0" class="list-group">
              <a v-for="(lead, i) in leads" :key="lead.id" href :class="{ active: i === currentSelection }" class="list-group-item list-group-item-action p-3 d-flex justify-content-between align-items-center" @click.prevent="handlePreviewEmail(lead, i)">
                <span>{{ lead.email }}</span>
                <base-button id="cta-review-lead" size="sm" color="secondary" rounded @click="handleReviewLead(lead)">
                  <font-awesome-icon :icon="['fas', 'magnifying-glass']" />
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

          <template #footer>
            <div class="d-flex justify-content-end">
              <base-button id="cta-review-all-lead" size="lg" color="primary" rounded @click="handleReviewAllLeads">
                <font-awesome-icon :icon="['fas', 'magnifying-glass']" class="me-2" />Review all
              </base-button>
            </div>
          </template>
        </base-card>
      </div>
      
      <div class="col-6">
        <sequence-block v-for="(sequence, i) in sequences" :key="sequence.sequence_id" :sequence="sequence" :class="{ 'mt-5': i >= 1 }" show-explicit-result :previewed-lead="previewedLead" @expand-preview="handleExpandPreview" />
      </div>
    </div>

    <base-modal id="expanded-email" :show="showExpandedModal" centered @close="showExpandedModal = false">
      <div class="container">
        <div class="row text-left">
          <div class="col-12">
            <p class="rounded-3 bg-light fw-light p-3">{{ previewedLead.email }}</p>
            <div class="rounded-3 bg-light fw-bold p-3">Object: {{ replacePlaceholders(store.currentSequence.email_object, previewedLead) }}</div>
            <div class="rounded-3 bg-light p-3 mt-5">{{ replacePlaceholders(store.currentSequence.email_text, previewedLead) }}</div>
          </div>
        </div>
      </div>
    </base-modal>
  </section>
</template>

<script>
import _ from 'lodash'

import { useCampaigns } from '../../store'
import { mapState } from 'pinia'
import { provide, ref } from 'vue'
import { useEmailUtilities } from '@/composables/emailing'

import BaseButton from '@/layouts/bootstrap/buttons/BaseButton.vue'
import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'
import BaseModal from '@/layouts/bootstrap/BaseModal.vue'
import SequenceBlock from '@/components/SequenceBlock.vue'

export default {
  components: {
    BaseButton,
    BaseCard,
    BaseModal,
    SequenceBlock
  },
  setup () {
    const store = useCampaigns()
    const previewEmail = ref(true)
    const currentSelection = ref(0)
    const { replacePlaceholders } = useEmailUtilities()

    provide('previewEmail', previewEmail)

    return {
      replacePlaceholders,
      currentSelection,
      previewEmail,
      store
    }
  },
  data () {
    return {
      showExpandedModal: false
    }
  },
  computed: {
    ...mapState(useCampaigns, { 
      leads: 'unreviewedLeads', 
      leadsCount: 'unreviewedLeadsCount',
      sequences: 'currentCampaignSequences'
    }),
    previewedLead () {
      return this.leads[this.currentSelection]
    }
  },
  methods: {
    async handleReviewLead (lead) {
      try {
        lead.reviewed = true
      } catch (e) {
        console.log(e)
      }
    },
    async handleReviewAllLeads () {
      try {
        const leadIds = _.map(this.leads, x => x.id)
        console.log(leadIds)
      } catch (e) {
        console.log(e)
      }
    },
    handleExpandPreview (sequence) {
      this.store.currentSequence = sequence
      this.showExpandedModal = true
    },
    handlePreviewEmail (lead, index) {
      this.currentSelection = index
      this.previewEmail = !this.previewEmail
    }
  }
}
</script>
