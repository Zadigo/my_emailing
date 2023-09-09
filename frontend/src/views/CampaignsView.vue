<template>
  <div class="container">
    <div class="row">
      <div class="col-10 offset-md-1">
        <!-- Campaigns -->
        <base-card class="shadow-sm">
          <template #header>
            <div class="d-flex justify-content-end">
              <base-button id="cta-new-campaign" :shadow-none="true" color="primary" rounded @click="handleNewCampaign">
                Create new campaign
              </base-button>
            </div>
          </template>
          
          <template #body>
            <div v-if="hasCampaigns" class="list-group">
              <!-- Campaign -->
              <router-link v-for="campaign in store.campaigns" :key="campaign.id" :to="{ name: 'campaign_view', params: { id: campaign.campaign_id } }" class="list-group-item list-group-item-action p-3 d-flex justify-content-left align-items-center">
                <base-checkbox id="start-campaign" label="" :is-switch="true" />
                <p class="ms-2 m-0">{{ campaign.name }}</p>

                <base-button id="more" color="secondary" size="sm" rounded>
                  More
                </base-button>
              </router-link>
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
    ...mapState(useCampaigns, ['hasCampaigns'])
  },
  methods: {
    async handleNewCampaign () {
      try {
        this.$router.push({ name: 'new_campaign_view', params: { id: 'camp_2' } })
        this.store.campaigns.push({
          id: 2,
          campaign_id: 'cam_123456',
          name: 'Some campaign n°2',
          sender: null,
          sequences: [
            {
              id: 1,
              sequence_id: 'seq_12345',
              email_object: 'Some simple object',
              text: "Some text for me",
              html_text: "Some html text for you",
              days: 3
            }
          ]
        })
      } catch (e) {
        console.error(e)
      }
    }
  }
}
</script>
