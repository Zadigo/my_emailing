<template>
  <div class="row">
    <div class="col-12">
      <h2 class="h4">Campaign settings</h2>
      <hr class="mb-3">

      <p class="fw-bold mb-1">Stop the campaign for people that</p>
      <base-list-group-checkbox :items="[{ name: 'a' }, { name: 'b' }]" />

      <p class="fw-bold mt-4 mb-1">Create a new task when people</p>
      <base-list-group-checkbox :items="[{ name: 'a' }, { name: 'b' }]" />
    </div>
  </div>
</template>

<script>
import BaseListGroupCheckbox from '@/layouts/bootstrap/listgroup/BaseListGroupCheckbox.vue'

export default {
  components: {
    BaseListGroupCheckbox
  }
}
</script>
