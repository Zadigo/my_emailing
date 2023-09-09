import { defineStore } from 'pinia'

import _ from 'lodash'

const useCampaigns = defineStore('campaigns', {
  state: () => ({
    campaigns: [
      // {
      //   id: 1,
      //   campaign_id: 'cam_1235',
      //   name: 'Some campaign',
      //   sender: null,
      //   sequences: [
      //     {
      //       id: 1,
      //       sequence_id: 'seq_12345',
      //       email_object: 'Some simple object',
      //       text: "Some text for me",
      //       html_text: "Some html text for you",
      //       days: 3
      //     }
      //   ]
      // }
    ],
    currentCampaign: {},
    currentCampaignLeads: [],
    currentSequence: {}
  }),
  getters: {
    currentCampaignSequences () {
      return this.currentCampaign.sequences || []
    },
    unreviewedLeads () {
      return _.filter(this.currentCampaignLeads, ['reviewed', false])
    },
    unreviewedLeadsCount () {
      return this.unreviewedLeads.length
    },
    hasCampaigns () {
      // Checks there are campaigns present
      // for the given team
      return this.campaigns.length > 0
    },
    hasCurrentCampaign () {
      // Checks if currentCampaign is populated
      if (!this.hasCampaign) {
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
    }
  }
})

export {
  useCampaigns
}
