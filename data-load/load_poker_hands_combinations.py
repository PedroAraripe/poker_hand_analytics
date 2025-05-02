import sys
import os
import base_load_csv

# Adiciona o diretório para que o Python encontre 'data-extract'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-extract")))

# Agora, importa a função corretamente
from extract_poker_hands_combinations import extract

base_load_csv.load(
  extract=extract,
  destination_file="poker_hands_full",
  headers="hand,category",
  data_map=lambda hand : f'{hand["hand_str"]},{hand["category"]}'
)