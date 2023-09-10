<template>
  <div class="container">
    <div class="row">
      <div class="col-8 offset-md-2 py-3">
        <!-- Campaigns -->
        <base-card class="shadow-sm">
          <template #header>
            <div class="d-flex justify-content-end">
              <base-button id="cta-new-campaign" :shadow-none="true" color="primary" rounded @click="handleNewCampaign">
                <font-awesome-icon :icon="['fas', 'plus']" class="me-2" />Create new campaign
              </base-button>
            </div>
          </template>
          
          <template #body>
            <div v-if="hasCampaigns" class="list-group">
              <!-- Campaign -->
              <a v-for="(campaign, i) in store.campaigns" :key="campaign.id" class="list-group-item list-group-item-action p-3 d-flex justify-content-between align-items-center" href @click.prevent>
                <div class="d-flex justify-content-left gap-2">
                  <base-checkbox :id="`campaign-${i}`" v-model="campaign.active" label="" is-switch />
                  <router-link :to="{ name: 'campaign_view', params: { id: campaign.campaign_id } }" class="ms-2 m-0 link-underline-primary">
                    {{ campaign.name }}
                  </router-link>
                </div>

                <base-button id="more" color="white" size="sm" floating>
                  <font-awesome-icon :icon="['fas', 'ellipsis-vertical']" />
                </base-button>
              </a>
            </div>
            
            <div v-else class="text-center">
              <h3>You have no campaigns yet</h3>
              <base-button id="cta-import-leads" :shadow-none="true" class="mt-3" color="secondary" rounded @click="handleNewCampaign">
                Import new leads
              </base-button>
            </div>
          </template>
        </base-card>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'pinia'
import { useCampaigns } from '../store'

import BaseButton from '@/layouts/bootstrap/buttons/BaseButton.vue'
import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'
import BaseCheckbox from '@/layouts/bootstrap/BaseCheckbox.vue'

export default {
  components: {
    BaseButton,
    BaseCard,
    BaseCheckbox
  },
  setup () {
    const store = useCampaigns()
    return {
      store
    }
  },
  computed: {
    ...mapState(useCampaigns, ['hasCampaigns']),
    campaignActive: {
      get () {
        return true
      },
      set (value) {
        console.log(value)
        // Do something
      }
    }
  },
  created () {
    this.getCampaigns()
  },
  methods: {
    async getCampaigns () {
      // Gets all the campaigns for the current team
      try {
        const response = await this.$http.get('/campaigns')
        this.store.campaigns = response.data
      } catch (e) {
        console.error(e)
      }
    },
    async handleNewCampaign () {
      // Creates a new campaign
      try {
        const response = await this.$http.post('/campaigns/new')
        const campaign = response.data
        this.store.currentCampaign = campaign
        this.$router.push({ name: 'new_campaign_view', params: { id: campaign.campaign_id } })
      } catch (e) {
        console.error(e)
      }
    }
  }
}
</script>
