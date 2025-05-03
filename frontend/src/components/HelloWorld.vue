<template>
  <div class="greetings">
    <h1 class="green">
      Sua mão é mais poderosa do que {{ pokerHandStatusStore.handStatus?.hands_stronger_count }}%
      das possíveis mãos de oponentes e {{ pokerHandStatusStore.handStatus?.hands_weaker_count }}%
      mais fraca do que outras possíveis mãos
    </h1>
    <Transition>
      <LoadingCard v-if="isLoadingHandStatusFirstTime" />
    </Transition>
  </div>
</template>

<script setup lang="ts">
import { usePokerHandStatusStore } from '@/stores/counter'
import LoadingCard from './LoadingCard.vue'
import { ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { pokerHands, type IPokerHand } from '@/types/handTypes'
defineProps<{
  msg: string
}>()

const pokerHandStatusStore = usePokerHandStatusStore()

const isLoadingHandStatusFirstTime = ref(true)

const route = useRoute()
const router = useRouter()

watch(
  () => pokerHandStatusStore.isLoading,
  (val) => {
    if (!val) {
      setTimeout(() => (isLoadingHandStatusFirstTime.value = false), 3000)
    }
  },
  { immediate: true }
)

watch(
  () => route.query?.player_hand,
  (val) => {
    if (!val) {
      router.push('/')
    }

    const pokerHand = val as IPokerHand

    if (val && pokerHands.includes(pokerHand)) {
      // pokerHandStatusStore.loadHandStatus(category as IPokerHand)
      pokerHandStatusStore.loadHandStatus(pokerHand)
    }
  },
  { immediate: true, deep: true }
)
</script>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}

.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
