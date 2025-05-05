export const pokerHands = [
  'High Card',
  'One Pair',
  'Two Pair',
  'Three of a Kind',
  'Straight',
  'Flush',
  'Full House',
  'Four of a Kind',
  'Straight Flush',
  'Royal Flush',
]

export type IPokerHand = (typeof pokerHands)[number]

export interface IHandCategoryStatus {
  category: string
  hand: number
  percentage: number
  hand_power: number
}
