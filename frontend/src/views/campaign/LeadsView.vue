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
          <div v-for="lead in leads" :key="lead.id" class="list-group-item p-3">
            {{ lead.email }}
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
    ...mapState(useCampaigns, { leads: 'currentCampaignLeads' }),
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
        this.store.currentCampaignLeads = [
          // {
          //   id: 1,
          //   firstname: 'Julie',
          //   lastname: 'Paul',
          //   email: 'julie@gmail.com',
          //   linkedin: null,
          //   reviewed: true
          // },
          // {
          //   id: 1,
          //   firstname: 'Pauline',
          //   lastname: 'Françoise',
          //   email: 'pauline@gmail.com',
          //   linkedin: null,
          //   reviewed: false
          // }
        ]
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
