<template>
  <section id="new">
    <div class="row">
      <base-card id="new-sequence" class="shadow-sm">
        <template #body>
          <div class="row">
            <div v-for="i in 4" :key="i" class="col-3 text-center">
              <base-card id="new-sequence-1" class="shadow-none border">
                <template #body>
                  Manual
                </template>
              </base-card>
            </div>
          </div>
        </template>
      </base-card>
    </div>
  </section>
</template>

<script>
import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'

export default {
  components: {
    BaseCard
  }
}
</script>

<style scoped>
[id^="new-sequence-"] {
  cursor: pointer;
}
</style>
