import { ref, computed, type Ref } from 'vue'
import { defineStore } from 'pinia'
import axios, { type AxiosResponse } from 'axios'
import type { IHandCategoryStatus, IPokerHand } from '@/types/handTypes'
export interface IPlayerHandStatus {
  hand_weaker_summary_sorted: IHandCategoryStatus[]
  hand_stronger_summary_sorted: IHandCategoryStatus[]
  hand_same_category_sorted: IHandCategoryStatus[]
  player_current_hand: string
  hands_same_category_count: number
  hands_stronger_count: number
  hands_weaker_count: number
  hands_same_category_total_count: number
  hands_stronger_total_count: number
  hands_weaker_total_count: number
}

export const usePokerHandStatusStore = defineStore('poker-hand-status-store', () => {
  const isLoading = ref(true)
  const handStatus: Ref<IPlayerHandStatus | undefined> = ref()

  async function loadHandStatus(userHand: IPokerHand = 'Two Pair') {
    try {
      let baseUrl = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
        ? 'http://127.0.0.1:8000'
        : 'https://www.lucasdata.com.br';

      isLoading.value = true;

      axios
        .get(`${baseUrl}/analysis/hand?player_current_hand=${userHand}`)
        .then((r: AxiosResponse<IPlayerHandStatus>) => {
          handStatus.value = r.data;
        });
    } catch (e) {
      console.error(e)
    } finally {
      isLoading.value = false
    }
  }

  return { isLoading, handStatus, loadHandStatus }
})
