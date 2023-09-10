<template>
  <div class="row">
    <div class="col-8 offset-md-2 py-3 mb-3">
      <ul class="nav nav-pills nav-fill">
        <li v-for="tab in tabs" :key="tab.name" class="nav-item">
          <router-link :to="{ name: tab.name }" :class="{ active: tab.name === $route.name }" class="nav-link" :aria-current="{ page: tab.name === $route.name }">
            {{ tab.title }}
            <span v-show="tab.name === 'leads_view'" class="badge text-bg-secondary ms-2">
              {{ campaign.number_of_leads }}
            </span>
            <span v-show="tab.name === 'review_view'" class="badge text-bg-secondary ms-2">
              {{ campaign.unreviewed_leads }}
            </span>
          </router-link>
        </li>

        <li class="nav-item">
          <router-link :to="{ name: 'settings_view' }" :class="{ active: $route.name === 'settings_view' }" class="nav-link" :aria-current="{ page: $route.name === 'settings_view' }">
            <font-awesome-icon :icon="['fas', 'gear']" class="me-2 fa-1x" /> Settings
          </router-link>
        </li>
      </ul>
    </div>

    <div class="col-8 offset-md-2">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'pinia'
import { useCampaigns } from '../store'

export default {
  data () {
    return {
      tabs: [
        {
          name: 'campaign_view',
          title: '1. Sequences'
        },
        {
          name: 'leads_view',
          title: '2. Leads'
        },
        {
          name: 'review_view',
          title: '3. Review'
        }
      ]
    }
  },
 computed: {
    ...mapState(useCampaigns, { 
      campaign: 'currentCampaign',
      sequences: 'currentCampaignSequences'
    }),
    ...mapState(useCampaigns, ['hasCurrentCampaign', 'unreviewedLeadsCount']),
  },
  beforeMount () {
    this.getCurrentCampaign(this.$route.params.id)
    // if (!this.hasCurrentCampaign) {
    //   this.$router.push({ name: 'home_view' })
    // }
  },
  methods: {
    ...mapActions(useCampaigns, ['getCurrentCampaign'])
  }
}
</script>
