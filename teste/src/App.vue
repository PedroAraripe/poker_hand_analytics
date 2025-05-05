<template>
  <div>
    <Transition>
      <LoadingCard v-if="!isHome && isLoadingHandStatusFirstTime" />
    </Transition>

    <RouterView
      :style="
        !isHome && isLoadingHandStatusFirstTime
          ? { height: '0px', overflow: 'hidden' }
          : { 'overflow-x': 'hidden' }
      "
    />
  </div>
</template>

<script lang="ts" setup>
import { computed, ref, watch } from "vue";
import { usePokerHandStatusStore } from "@/stores/pokerHand";
import { RouterView, useRoute } from "vue-router";
import LoadingCard from "./pages/components/LoadingCard.vue";

const pokerHandStatusStore = usePokerHandStatusStore();

const isLoadingHandStatusFirstTime = ref(true);

const route = useRoute();

const isHome = computed(() => route.path === "/");

watch(
  () => pokerHandStatusStore.isLoading,
  (val) => {
    if (!val) {
      setTimeout(() => (isLoadingHandStatusFirstTime.value = false), 1500);
    }
  },
  { immediate: true }
);
</script>