<template>
  <span class="typewriter">
    {{ displayText }}<span class="cursor" :class="{ blink: showCursor }">|</span>
  </span>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps<{
  phrases: string[]
  typingSpeed?: number
  deletingSpeed?: number
  pauseDuration?: number
}>()

const displayText = ref('')
const showCursor = ref(true)
const currentPhraseIndex = ref(0)
const isDeleting = ref(false)

const typingSpeed = props.typingSpeed ?? 80
const deletingSpeed = props.deletingSpeed ?? 40
const pauseDuration = props.pauseDuration ?? 2500

let timeoutId: ReturnType<typeof setTimeout> | null = null
let cursorInterval: ReturnType<typeof setInterval> | null = null

const tick = () => {
  const currentPhrase = props.phrases[currentPhraseIndex.value]

  if (isDeleting.value) {
    displayText.value = currentPhrase.substring(0, displayText.value.length - 1)
    if (displayText.value.length === 0) {
      isDeleting.value = false
      currentPhraseIndex.value = (currentPhraseIndex.value + 1) % props.phrases.length
      timeoutId = setTimeout(tick, 300)
    } else {
      timeoutId = setTimeout(tick, deletingSpeed)
    }
  } else {
    displayText.value = currentPhrase.substring(0, displayText.value.length + 1)
    if (displayText.value.length === currentPhrase.length) {
      isDeleting.value = true
      timeoutId = setTimeout(tick, pauseDuration)
    } else {
      timeoutId = setTimeout(tick, typingSpeed)
    }
  }
}

onMounted(() => {
  timeoutId = setTimeout(tick, 500)
  cursorInterval = setInterval(() => {
    showCursor.value = !showCursor.value
  }, 530)
})

onUnmounted(() => {
  if (timeoutId) clearTimeout(timeoutId)
  if (cursorInterval) clearInterval(cursorInterval)
})
</script>

<style scoped>
.typewriter {
  display: inline;
}

.cursor {
  display: inline;
  font-weight: 300;
  color: var(--accent-glow-strong);
  opacity: 1;
  transition: opacity 0.1s;
}

.cursor.blink {
  opacity: 0;
}
</style>
