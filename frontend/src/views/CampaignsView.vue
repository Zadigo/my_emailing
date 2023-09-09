<template>
  <div class="container">
    <div class="row">
      <div class="col-10 offset-md-1">
        <base-card class="shadow-sm">
          <template #header>
            <div class="d-flex justify-content-end">
              <base-button id="cta-new-campaign" :shadow-none="true" color="primary" rounded @click="handleNewCampaign">
                Create new campaign
              </base-button>
            </div>
          </template>
          
          <template #body>
            <div class="list-group">
              <router-link v-for="campaign in store.campaigns" :key="campaign.id" :to="{ name: 'campaign_view', params: { id: campaign.campaign_id } }" class="list-group-item list-group-item-action p-3 d-flex justify-content-left align-items-center">
                <base-checkbox id="start-campaign" label="" :is-switch="true" />
                <p class="ms-2 m-0">{{ campaign.name }}</p>

                <base-button id="more" color="secondary" size="sm" rounded>
                  More
                </base-button>
              </router-link>
            </div>
          </template>
        </base-card>
      </div>
    </div>
  </div>
</template>

<script>
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
  methods: {
    async handleNewCampaign () {
      try {
        this.$router.push({ name: 'new_campaign_view', params: { id: 'camp_2' } })
        this.store.campaigns.push({
          id: 2,
          campaign_id: 'cam_1235',
          name: 'Some campaign 2',
          sequences: [
            {
              id: 1,
              sequence_id: 'seq_45456',
              items: [
                {
                  email_object: 'Another object',
                  component: 'email-sequence'
                },
                {
                  days: 3,
                  component: 'date-sequence'
                }
              ]
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
