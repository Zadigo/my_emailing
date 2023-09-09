<template>
  <div id="emailing">
    <base-card id="email-sequence" class="shadow-sm" @click="showEmailComponent">
      <template #body>
        Email : <span class="badge text-bg-light">
          {{ item.email_object }}
        </span>
      </template>
    </base-card>
  </div>
</template>

<script>
import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'

export default {
  components: {
    BaseCard
  },
  props: {
    item: {
      type: Object
    },
    sequence: {
      type: Object
    }
  },
  data () {
    return {
    }
  },
  methods: {
    showEmailComponent () {
      this.$router.push({ name: 'email_view', params: { seq: this.sequence.sequence_id } })
    }
  }
}
</script>

<style scoped>
#email-sequence {
  cursor: pointer;
}

#email-sequence:hover {
  background-color: blue;
}
</style>
