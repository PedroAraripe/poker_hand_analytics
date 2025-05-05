
<template>
  <div class="w-screen h-screen flex items-center justify-center">
    <form @submit.prevent="onSubmit">
      <FormField v-slot="{ componentField }" name="category">
        <FormItem>
          <FormLabel>Categoria da Mão</FormLabel>

          <Select default-value="Royal Flush" v-bind="componentField">
            <FormControl class="w-50">
              <SelectTrigger>
                <SelectValue placeholder="Selecione uma categoria" />
              </SelectTrigger>
            </FormControl>
            <SelectContent>
              <SelectGroup>
                <SelectItem value="High Card"> Carta Mais Alta </SelectItem>
                <SelectItem value="One Pair"> Um Par </SelectItem>
                <SelectItem value="Two Pair"> Dois Pares </SelectItem>
                <SelectItem value="Three of a Kind">
                  Três de Um Tipo
                </SelectItem>
                <SelectItem value="Straight"> Sequência </SelectItem>
                <SelectItem value="Flush"> Flush </SelectItem>
                <SelectItem value="Full House"> Full House </SelectItem>
                <SelectItem value="Four of a Kind">
                  Quatro de Um Tipo
                </SelectItem>
                <SelectItem value="Straight Flush">
                  Flush Sequência
                </SelectItem>
                <SelectItem value="Royal Flush"> Sequência Real </SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>

          <!-- <FormDescription class="mt-2 max-w-50 overflow-hidden">
            Você pode ver qual tipo de categoria sua mão se enquadra
            <a href="/examples/forms">aqui</a>.
          </FormDescription> -->
          <FormMessage />
        </FormItem>
      </FormField>

      <Button class="mt-4 border-2 w-full" type="submit">
        Visualizar análise
      </Button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { Button } from "@/components/ui/button";
import {
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { usePokerHandStatusStore } from "@/stores/pokerHand";
import { pokerHands, type IPokerHand } from "@/types/handTypes";

import { toTypedSchema } from "@vee-validate/zod";
import { useForm } from "vee-validate";
import { useRouter } from "vue-router";
import * as z from "zod";

const pokerHandStatusStore = usePokerHandStatusStore();

const router = useRouter();

const formSchema = toTypedSchema(
  z.object({
    category: z.string({
      required_error: "Por favor selecione uma categoria.",
    }),
  })
);

const { handleSubmit } = useForm({
  validationSchema: formSchema,
  initialValues: {
    category: "Royal Flush",
  },
});

const onSubmit = handleSubmit((values) => {
  const category = values.category;

  if (pokerHands.includes(category as IPokerHand)) {
    router.push({ name: "analysis", query: { player_hand: category } });
  }
});
</script>
