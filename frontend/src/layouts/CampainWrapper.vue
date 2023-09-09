<template>
  <div class="row">
    <div class="col-8 offset-md-2 py-3 mb-3">
      <ul class="nav nav-pills nav-fill">
        <li v-for="tab in tabs" :key="tab.name" class="nav-item">
          <router-link :to="{ name: tab.name }" :class="{ active: tab.name === $route.name }" class="nav-link" :aria-current="{ page: tab.name === $route.name }">
            {{ tab.title }}
            <span v-show="tab.name === 'lemlist_review_view'" class="badge text-bg-secondary ms-2">4</span>
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
          title: 'Sequences'
        },
        {
          name: 'leads_view',
          title: 'Leads'
        },
        {
          name: 'review_view',
          title: 'Review'
        }
      ]
    }
  },
 computed: {
    ...mapState(useCampaigns, { sequences: 'currentCampaignSequences' }),
    ...mapState(useCampaigns, ['hasCurrentCampaign'])
  },
  beforeMount () {
    this.getCurrentCampaign(this.$route.params.id)
    if (!this.hasCurrentCampaign) {
      this.$router.push({ name: 'home_view' })
    }
  },
  methods: {
    ...mapActions(useCampaigns, ['getCurrentCampaign'])
  }
}
</script>
