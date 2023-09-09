<template>
  <section id="email">
    <base-card>
      <template #body>
        <p class="fw-bold mb-1">Sender</p>
        <span>something@gmail.com</span>
  
        <div class="my-3">
          <p class="fw-bold mb-1">Email</p>
          <base-input id="subject" v-model="email.email_object" placeholder="Email subject" />
          <textarea v-model="email.text" cols="3" class="form-control mt-2"></textarea>
        </div>
      </template>
    </base-card>
  </section>
</template>

<script>
import BaseInput from '@/layouts/bootstrap/BaseInput.vue'
import BaseCard from '@/layouts/bootstrap/cards/BaseCard.vue'
import { mapActions, mapState } from 'pinia';
import { useCampaigns } from '../../store';
export default {
  components: {
    BaseCard,
    BaseInput
  },
  setup () {
  },
  data () {
    return {
      email: {
        sender: null,
        email_object: null,
        text: null,
        html_text: null
      }
    }
  },
  mounted () {
    this.getCurrentSequence(this.$route.params.seq)
    this.email.email_object = this.sequenceEmail.email_object
    this.email.text = this.sequenceEmail.text
    this.email.html_text = this.sequenceEmail.html_text
  },
  methods: {
    ...mapState(useCampaigns, ['sequenceEmail']),
    ...mapActions(useCampaigns, ['getCurrentSequence'])
  }
}
</script>
