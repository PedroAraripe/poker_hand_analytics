<template>
  <div class="greetings">
    <DonutChart v-bind="chartResume" />

    <BarChart v-bind="chartStronger" />

    <BarChart v-bind="chartWeaker" />

    <Transition>
      <LoadingCard v-if="isLoadingHandStatusFirstTime" />
    </Transition>
  </div>
</template>

<script setup lang="ts">
import { usePokerHandStatusStore } from '@/stores/counter'
import LoadingCard from './LoadingCard.vue'
import { computed, ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { pokerHands, type IPokerHand } from '@/types/handTypes'
import { DonutChart } from '@/components/ui/chart-donut'

import BarChart from '@/components/ui/chart-bar/BarChart.vue'

const pokerHandStore = usePokerHandStatusStore()

const chartResume = computed(() => {
  const data = [
    {
      name: 'Combinações mais fracas',
      total: pokerHandStore.handStatus?.hands_stronger_total_count,
      predicted: pokerHandStore.handStatus?.hands_stronger_total_count,
    },
    {
      name: 'Combinações da mesma categoria',
      total: pokerHandStore.handStatus?.hands_same_category_total_count,
      predicted: pokerHandStore.handStatus?.hands_same_category_total_count,
    },
    {
      name: 'Combinações mais fortes',
      total: pokerHandStore.handStatus?.hands_weaker_total_count,
      predicted: pokerHandStore.handStatus?.hands_weaker_total_count,
    },
  ].map((d) => {
    return {
      ...d,
      total: d?.total > 0 && d?.total < 1 ? 1 : d?.total,
      valueFormatter: (val) => val + 1000,
    }
  })

  return {
    data,
    index: 'name',
    category: 'total',
    colors: ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple'],
  }
})

const chartStronger = computed(() => {
  const data =
    pokerHandStore.handStatus?.hand_stronger_summary_sorted.map((c) => ({
      'Mãos de Poker %': c.percentage,
      'Categoria Carta': c.category,
    })) || []

  return {
    data,
    index: 'Categoria Carta',
    categories: ['Mãos de Poker %'],
    'y-formatter': (tick, i) => `${tick}%`,
  }
})

const chartWeaker = computed(() => {
  const data =
    pokerHandStore.handStatus?.hand_weaker_summary_sorted.map((c) => ({
      '% Distribuição de combinações': c.percentage,
      'Categoria Carta': c.category,
    })) || []

  return {
    data,
    index: 'Categoria Carta',
    categories: ['Mãos de Poker %'],
    'y-formatter': (tick, i) => `${tick}%`,
  }
})

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
      setTimeout(() => (isLoadingHandStatusFirstTime.value = false), 0)
      // setTimeout(() => (isLoadingHandStatusFirstTime.value = false), 3000)
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
