# 🃏 Poker Hand Analysis

Este projeto realiza uma análise completa das combinações possíveis de mãos de poker com 5 cartas, categorizando-as e permitindo comparar qualquer mão com o universo de combinações possíveis.

## 📁 Estrutura do Projeto

```
.
├── constants.py                   # Constantes auxiliares (naipes, valores, categorias)
├── generate_poker_combinatios.py # Gera todas as combinações possíveis de mãos de poker (52C5)
├── extract_poker_categories.py   # Classifica as mãos geradas em categorias (Flush, Full House etc.) e calcula distribuições
├── hand_summary.csv              # Resumo final das distribuições geradas por categoria
├── poker.py                      # Script interativo para comparar sua mão com todas as outras
├── poker_hands_full.csv          # Arquivo com todas as 2.598.960 mãos possíveis e suas respectivas categorias
```

## 🚀 Como Utilizar

1. **Gerar todas as combinações possíveis de mãos:**

   ```bash
   python generate_poker_combinatios.py
   ```

   Isso criará o arquivo `poker_hands_full.csv`, com todas as 2.598.960 mãos de poker possíveis.

2. **Classificar as mãos e gerar resumo estatístico:**

   ```bash
   python extract_poker_categories.py
   ```

   Esse script classifica as mãos (Ex: Full House, Flush etc.) e gera o arquivo `hand_summary.csv` com a contagem e porcentagem de cada categoria.

3. **Comparar sua mão com o universo de combinações:**

   ```bash
   python poker.py
   ```

   O script irá:

   * Identificar a categoria da sua mão
   * Mostrar quantas mãos são mais fortes, mais fracas ou da mesma categoria
   * Exibir gráficos de pizza e barras com a distribuição

## 📊 Exemplos de Insights

* Você pode descobrir que mãos do tipo "One Pair" representam cerca de 42% de todas as combinações possíveis.
* "Royal Flush" ocorre em apenas 0.00015% das vezes.
* Veja graficamente contra quais categorias sua mão atual é mais fraca ou mais forte.

## 🧠 Objetivo

Esse projeto é ideal para quem deseja entender:

* A distribuição estatística das mãos de poker
* Análise combinatória aplicada a jogos de cartas
* Como comparar uma mão específica com o universo completo do jogo

## 📝 Requisitos

* Python 3.7+
* Bibliotecas:

  * `pandas`
  * `matplotlib`
  * `seaborn`

Instale as dependências com:

```bash
pip install -r requirements.txt
```

## 📄 Licença

Este projeto é livre para uso educacional e não possui restrições comerciais explícitas. Sinta-se à vontade para modificar e compartilhar!

---

Se quiser, posso gerar também um `requirements.txt` para facilitar a instalação dos pacotes. Deseja isso?
