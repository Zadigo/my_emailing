import _ from 'lodash'
import { defineStore } from 'pinia'

const useCampaigns = defineStore('campaigns', {
  state: () => ({
    campaigns: [
      {
        id: 1,
        campaign_id: 'cam_1235',
        name: 'Some campaign',
        sender: null,
        sequences: [
          {
            id: 1,
            sequence_id: 'seq_12345',
            items: [
              {
                email_object: 'Some simple object',
                text: "Some text for me",
                html_text: "Some html text for you",
                component: 'email-sequence'
              },
              {
                days: 3,
                component: 'date-sequence'
              }
            ]
          }
        ]
      }
    ],
    currentCampaign: {},
    currentCampaignLeads: [],
    currentSequence: {},
    sequenceEmail: {}
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
    }
  },
  actions: {
    getCurrentSequence (sequenceId) {
      this.currentSequence = _.find(this.currentCampaignSequences, ['sequence_id', sequenceId]) || {}
      this.getSequenceEmail()
    },
    getViewedCampaign (id) {
      this.currentCampaign = _.find(this.campaigns, ['campaign_id', id])
    },
    getSequenceEmail () {
      this.sequenceEmail = this.currentSequence.items[0]
    }
  }
})

export {
  useCampaigns
}
