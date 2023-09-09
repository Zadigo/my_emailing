<template>
  <section class="settings">
    <base-card class="shadow-sm">
      <template #body>
        <div class="row">
          <div class="col-3">
            <nav class="nav nav-pills nav-fill flex-column">
              <a v-for="tab in settingsTabs" :key="tab.id" :class="{ active: tab.id === currentTab }" class="nav-link" :aria-current="{ page: tab.id === currentTab }" href @click.prevent="currentTab = tab.id">
                {{ tab.tab_title }}
              </a>
            </nav>
          </div>
    
          <div class="col-9">
            <component :is="activeComponent" />
          </div>
        </div>
      </template>
    </base-card>
  </section>
</template>

<script>
import CampaignSettings from '@/components/settings/CampaignSettings.vue'
import ScheduleSettings from '@/components/settings/ScheduleSettings.vue'
import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'

export default {
  components: {
    BaseCard,
    CampaignSettings,
    ScheduleSettings
  },
  data () {
    return {
      settingsComponents: ['campaign-settings', 'schedule-settings'],
      currentTab: 0,
      settingsTabs: [
        {
          id: 0,
          tab_title: 'Campaign'
        },
        {
          id: 1,
          tab_title: 'Schedules'
        }
      ]
    }
  },
  computed: {
    activeSettings () {
      return this.settingsTabs[this.currentTab]
    },
    activeComponent () {
      return this.settingsComponents[this.currentTab]
    }
  }
}
</script>
