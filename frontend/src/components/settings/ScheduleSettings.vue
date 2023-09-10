<template>
  <div class="row">
    <div class="col-12">
      <h2 class="h4">Campaign schedules</h2>
      <hr class="mb-3">
      
      <div class="d-flex justify-content-end">
        <base-button id="cta-new-schedule" class="mb-4" color="secondary" rounded @click="showCreateSchedule=!showCreateSchedule">
          <font-awesome-icon :icon="['fas', 'calendar']" class="me-3" />Create new schedule
        </base-button>
      </div>
      
      <!-- Create schedule -->
      <div v-if="showCreateSchedule" class="rounded-3 bg-light p-4 mt-3">
        <div class="schedule-name p-1">
          <p class="fw-bold mb-1">Schedule name</p>
          <base-input id="schedule-name" v-model="scheduleTemplate.name" class="p-3 w-50" />
        </div>

        <div class="timezone p-1 mt-4">
          <p class="fw-bold mb-1">Timezone</p>
          <base-select id="timezone" v-model="scheduleTemplate.timezone" :items="allTimezones" class="p-3 w-50" />
        </div>

        <div class="sending-days p-1 mt-4">
          <p class="fw-bold mb-1">Send on these days</p>
          <base-checkbox v-for="day in sendingDays" :id="day.toLowerCase()" :key="day" v-model="scheduleTemplate[`${day}`]" :label="day" :aria-label="day" class="form-check-inline" />
        </div>

        <div class="sending-hours p-1 mt-4">
          <p class="fw-bold mb-1">Between</p>
          <div class="d-flex justify-content-left gap-3">
            <base-select id="start-time-at" v-model="scheduleTemplate.start_time_at" :items="allClocks" class="p-3" />
            <base-select id="end-time-at" v-model="scheduleTemplate.end_time_at" :items="endTimeAtList" class="p-3" />
          </div>
        </div>

        <base-button id="cta-new-schedule" class="mt-4" size="lg" color="secondary" rounded>
          <font-awesome-icon :icon="['fas', 'plus']" class="me-3" />Add schedule
        </base-button>
      </div>

      <!-- Schedules -->
      <div v-else class="schedules">
        <div v-for="(schedule, i) in currentCampaign.schedule_set" :key="schedule.schedule_id" class="rounded-3 bg-light p-3">
          <div class="d-flex justify-content-between align-items-center mb-2">
            <p class="fw-bold m-0">{{ schedule.name || 'Unnamed schedule' }}</p>
            <base-button :id="`cta-schedule-action-${i}`" color="light" floating>
              <font-awesome-icon :icon="['fas', 'ellipsis-vertical']" />
            </base-button>
          </div>
          <div class="schedule d-flex justify-content-around align-items-centers gap-2 text-body-tertiary">
            <span class="d-block text-center">{{ schedule.list_of_sending_days[0] }}/7 days</span>
            <span class="d-block text-center">Start at {{ schedule.start_time_at }}</span>
            <span class="d-block text-center">End at {{ schedule.end_time_at }}</span>
            <span class="d-block text-center">Send every {{ schedule.interval }} minutes</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// import _ from 'lodash'
import { useTimeZones, useClocks } from '@/composables/timezones'
import { useCampaigns } from '@/store'
import { mapState } from 'pinia'
import dayjs from '../../plugins/dayjs'
import BaseButton from '@/layouts/bootstrap/buttons/BaseButton.vue'
import BaseCheckbox from '@/layouts/bootstrap/BaseCheckbox.vue'
import BaseInput from '@/layouts/bootstrap/BaseInput.vue'
import BaseSelect from '@/layouts/bootstrap/BaseSelect.vue'
// import BaseListGroupCheckbox from '@/layouts/bootstrap/listgroup/BaseListGroupCheckbox.vue'

export default {
  components: {
    BaseButton,
    BaseCheckbox,
    BaseInput,
    BaseSelect
    // BaseListGroupCheckbox
  },
  setup () {
    const { allTimezones } = useTimeZones()
    const { allClocks, getListFromPoint } = useClocks()
    return {
      dayjs,
      allTimezones,
      allClocks,
      getListFromPoint
    }
  },
  data () {
    return {
      showCreateSchedule: false,
      sendingDays: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
      scheduleTemplate: {
        name: null,
        timezone: 'UTC',
        start_time_at: "12:00",
        end_time_at: "23:59",
        sending_days: {
          Monday: false,
          Tuesday: false,
          Wednesday: false,
          Thursday: false,
          Friday: false,
          Saturday: false,
          Sunday: false
        }
      }
    }
  },
  computed: {
    ...mapState(useCampaigns, ['currentCampaign']),
    endTimeAtList () {
      return this.getListFromPoint(this.scheduleTemplate.start_time_at)
    }
  }
}
</script>

<style scoped>
.schedule span:not(:last-child)::after {
  content: "|";
  padding-left: .5rem;
}
</style>
