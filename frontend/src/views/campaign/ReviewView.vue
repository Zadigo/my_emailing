<template>
  <section id="leads">
    <div class="row">
      <div class="col-6">
        <base-card class="shadow-sm">
          <template #body>
            <div v-if="leadsCount > 0" class="list-group">
              <div v-for="lead in leads" :key="lead.id" class="list-group-item p-3 d-flex justify-content-between align-items-center">
                <span>{{ lead.email }}</span>
                <base-button id="cta-review-lead" size="sm" color="secondary" rounded @click="handleReviewLead(lead)">
                  Review
                </base-button>
              </div>
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
        <base-card class="shadow-sm">
          <template #body>
            something
          </template>
        </base-card>
      </div>
    </div>
  </section>
</template>

<script>
import BaseButton from '@/layouts/bootstrap/buttons/BaseButton.vue'
import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'
import { useCampaigns } from '../../store'
import { mapState } from 'pinia';
export default {
  components: {
    BaseButton,
    BaseCard
  },
  setup () {
    const store = useCampaigns()
    return {
      store
    }
  },
  computed: {
    ...mapState(useCampaigns, { 
      leads: 'unreviewedLeads', 
      leadsCount: 'unreviewedLeadsCount'
    })
  },
  methods: {
    async handleReviewLead (lead) {
      try {
        lead.reviewed = true
      } catch (e) {
        console.log(e)
      }
    }
  }
}
</script>
