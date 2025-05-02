import sys
import os
import base_load_csv

# Adiciona o diretório para que o Python encontre 'data-extract'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data-transform")))

# Agora, importa a função corretamente
from transform_group_poker_hands import transform

base_load_csv.load(
  extract=transform,
  destination_file="hand_summary",
  data_frame_index_label="category",
)