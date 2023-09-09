<template>
  <section id="leads">
    <base-card class="shadow-sm">
      <template #header>
        <div class="d-flex justify-content-between align-items-center">
          <base-input id="search" v-model="search" placeholder="Email, firstname, lastname..." class="w-50 p-2" />
          <base-button id="cta-import-leads" size="md" rounded @click="handleImportLeads">
            Import new leads
          </base-button>
        </div>
      </template>
      
      <template #body>
        <div class="list-group">
          <div v-for="lead in leads" :key="lead.id" class="list-group-item list-group-item-action p-3 d-flex justify-content-around gap-3 align-items-center text-left">
            <span>{{ lead.email }}</span>
            <span v-if="lead.reviewed" class="badge text-bg-success">Reviewed</span>
            <router-link v-else-if="!lead.reviewed" :to="{ name: 'review_view', query: {id: lead.id } }" class="badge text-bg-light">To review</router-link>
            <span>{{ lead.firstname }}</span>
            <span>{{ lead.lastname }}</span>
          </div>
        </div>
      </template>
    </base-card>
  </section>
</template>

<script>
import _ from 'lodash'
import BaseCard from '../../layouts/bootstrap/cards/BaseCard.vue'
import BaseButton from '../../layouts/bootstrap/buttons/BaseButton.vue'
import BaseInput from '../../layouts/bootstrap/BaseInput.vue'
import { useCampaigns } from '../../store'
import { mapState } from 'pinia'
export default {
  components: {
    BaseButton,
    BaseCard,
    BaseInput
  },
  setup () {
    const store = useCampaigns()
    return {
      store
    }
  },
  data () {
    return {
      search: null
    }
  },
  computed: {
    ...mapState(useCampaigns, { 
      campaign: 'currentCampaign',
      leads: 'currentCampaignLeads'
    }),
    searchedLeads () {
      if (!this.search) {
        return this.leads
      } else {
        return _.filter(this.leads, (lead) => {
          try {
            const truthArray = Object.keys(lead).map((key) => {
              const value = lead[key]
              if (value === null || !value) {
                return false
              }
  
              if (typeof value === 'object') {
                return false
              }

              return (
                value === this.search ||
                value.includes(this.search) ||
                value.toLowerCase() === this.search || 
                value.toLowerCase().includes(this.search)
              )
            })
            return truthArray.some(x => x === true)
          } catch (e) {
            console.error(e)
            return false
          }
        })
      }
    }
  },
  created () {
    this.getLeads()
  },
  methods: {
    async getLeads () {
      try {
        const response = await this.$http.get(`/campaigns/${this.campaign.campaign_id}/leads`)
        this.store.currentCampaignLeads = response.data
      } catch (e) {
        console.log(e)
      }
    },
    async handleImportLeads () {
      try {
        // pass
      } catch (e) {
        console.error(e)
      }
    }
  }
}
</script>
