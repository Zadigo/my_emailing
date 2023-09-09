<template>
  <div :style="`background-image: url(${image});`" class="intro intro-100 bg-image">
    <div ref="mask" class="mask">
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    image: {
      type: String,
      required: true
    },
    opacity: {
      type: Number,
      default: 0.3
    }
  },
  mounted () {
    // style="background-color: rgba(0, 0, 0, 0.3);"
    this.$refs.mask.style.backgroundColor = `rgba(0, 0, 0, ${this.opacity})`
  }
}
</script>
