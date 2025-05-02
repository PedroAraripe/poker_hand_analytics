```markdown
# 🃏 Poker Hand Analysis

Este projeto realiza uma análise completa das combinações possíveis de mãos de poker com 5 cartas, categorizando-as e permitindo comparar qualquer mão com o universo de combinações possíveis. Além disso, você pode enviar uma mão via API e receber insights estatísticos sobre sua força relativa.

## 📁 Estrutura do Projeto

```

.
├── constants/
│   └── cards\_combinations\_powers.py              # Definições de cartas e forças
├── data/
│   ├── hand\_summary.csv                          # Estatísticas por categoria
│   ├── poker\_hands\_full.csv                      # Todas as 2.598.960 mãos possíveis
│   └── README.txt
├── data-extract/
│   └── extract\_poker\_hands\_combinations.py       # Gera todas as combinações possíveis
├── data-load/
│   ├── base\_load\_csv.py                          # Função auxiliar de leitura
│   ├── load\_poker\_hands\_combinations.py          # Carrega CSV de combinações
│   └── load\_poker\_hands\_combinations\_grouped.py  # Agrupa as combinações por categoria
├── data-transform/
│   └── transform\_group\_poker\_hands.py            # Formata dados para análise
├── data-visualization/
│   └── visualize\_player\_hand\_synthetic.py        # Gera gráficos da análise da mão do jogador
├── routes/
│   └── hand\_analysis.py                          # Rota da API que analisa uma mão
├── services/
│   └── service\_hand\_analysis\_synthethic.py       # Lógica da análise da força da mão
├── main.py                                       # Inicia o servidor FastAPI
└── requirements.txt                              # Dependências do projeto

````

---

## 🚀 Como Utilizar

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
````

### 2. Iniciar o Servidor FastAPI

Execute na raiz do projeto:

```bash
python -m uvicorn main:app --reload
```

Acesse o servidor local em:
[http://127.0.0.1:8000](http://127.0.0.1:8000)
Documentação interativa em:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🌐 Endpoint Disponível

### `GET /analysis/hand`

Analisa a força relativa de uma mão de poker de 5 cartas, comparando com as 2.598.960 possíveis.

**Parâmetro de query:**

* `player_current_hand` (obrigatório): string com 5 cartas, separadas por vírgulas
  Ex: `"Two%20Pair"`

**Exemplo:**

```
GET /analysis/hand?player_current_hand=Two%20Pair
```

**Resposta esperada:**

```json
{
  "player_current_hand": "Two Pair",
  "hands_weaker_count": [...],
  "hands_stronger_count": [...],
  "hands_same_category_count": [...],
  ...
}
```

---

## ⚙️ Scripts Auxiliares

### 🔄 Geração e Classificação

```bash
python data-extract/extract_poker_hands_combinations.py
```

### 📥 Carregamento de Dados

```bash
python data-load/load_poker_hands_combinations.py
python data-load/load_poker_hands_combinations_grouped.py
```

### 🧹 Transformação para Análise

```bash
python data-transform/transform_group_poker_hands.py
```

### 📊 Visualização

```bash
python data-visualization/visualize_player_hand_synthetic.py
```

Gera gráficos de pizza e barras com as forças comparativas da sua mão em relação às outras possíveis.

---

## 📊 Exemplos de Insights

* Mãos "One Pair" representam cerca de 42% de todas as combinações possíveis.
* "Royal Flush" é extremamente rara (0.00015%).
* Descubra graficamente contra quais categorias sua mão é mais fraca ou mais forte.

---

## 🎯 Objetivo

Este projeto é ideal para quem deseja entender:

* A distribuição estatística das mãos de poker
* Análise combinatória aplicada a jogos de cartas
* Comparação de uma mão específica com o universo completo de mãos

---

## ✅ Requisitos

* Python 3.10+
* Bibliotecas utilizadas:

```txt
pandas
matplotlib
seaborn
fastapi
uvicorn
```

Instale tudo com:

```bash
pip install -r requirements.txt
```