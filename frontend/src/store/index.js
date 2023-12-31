import { defineStore } from 'pinia'
import { client } from '@/plugins/axios'
import _ from 'lodash'

const useCampaigns = defineStore('campaigns', {
  state: () => ({
    campaigns: [],
    currentCampaign: {},
    currentCampaignLeads: [],
    currentSequence: {}
  }),
  getters: {
    currentCampaignSequences () {
      return this.currentCampaign.sequence_set || []
    },
    unreviewedLeads () {
      // Leads that have not yet been reviewed to be sent
      return _.filter(this.currentCampaignLeads, ['reviewed', false])
    },
    unreviewedLeadsCount () {
      // Count of the leads that have not yet been reviewed to be sent
      return this.unreviewedLeads.length
    },
    hasCampaigns () {
      // Checks there are campaigns present
      // for the given team
      return this.campaigns.length > 0
    },
    hasSequences () {
      return this.currentCampaignSequences.length > 0
    },
    hasLeads () {
      return this.currentCampaignLeads.length > 0
    },
    hasCurrentCampaign () {
      // Checks if currentCampaign is populated
      if (!this.hasCampaigns) {
        return false
      }

      if (Object.keys(this.currentCampaign).length > 0) {
        return true
      } else {
        return false
      }
    }
  },
  actions: {
    getCurrentSequence (sequenceId) {
      this.currentSequence = _.find(this.currentCampaignSequences, ['sequence_id', sequenceId]) || {}
    },
    getCurrentCampaign (id) {
      // Gets the currently viewed campaign by using
      // the ID from the url
      this.currentCampaign = _.find(this.campaigns, ['campaign_id', id]) || {}
    },

    async getCampaigns () {
      try {
        const response = await client.get('/campaigns')
        this.campaigns = response.data
      } catch (e) {
        console.error(e)
      }
    },

    async getLeads () {
      try {
        const response = await client.get(`/campaigns/${this.currentCampaign.campaign_id}/leads`)
        this.currentCampaignLeads = response.data
      } catch (e) {
        console.log(e)
      }
    },

    async reloadCampaigns (campaignId) {
      if (!this.hasCampaigns) {
        this.getCampaigns()
      }
      setTimeout(() => {
        this.getCurrentCampaign(campaignId)
      }, 300);
    }
  }
})

export {
  useCampaigns
}
