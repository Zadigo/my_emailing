import { ref } from 'vue'
import _ from 'lodash'
import timezones from '../data/timezones.json'
import clocks from '../data/clocks.json'

/**
 * Composable to work with timezones. These
 * are "pytz" timezones from Python library 
 */
export function useTimeZones () {
  const allTimezones = ref(timezones)

  function findTimezone (name) {
    return _.filter(allTimezones, (item) => {
      return item === name
    })
  }

  return {
    allTimezones,
    findTimezone
  }
}

/**
 * Composable to work with times. These
 * where generated via https://catonmat.net/tools/generate-clock-times 
 */
export function useClocks () {
  const allClocks = ref(clocks)

  function getListFromPoint (clock = '12:00') {
    // Slices the list from a given index to another
    // for example let's say the clock was "02:00", then 
    // this would return "02:30" until the ending of the list
    const index = _.indexOf(allClocks.value, clock)
    console.log(index)
    return allClocks.value.slice(index + 1, allClocks.value.length)
  }
  return {
    allClocks,
    getListFromPoint
  }
}
