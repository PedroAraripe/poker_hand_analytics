def load(
  extract,
  destination_file,
  data_frame_index_label,
  headers=None,
  data_map=None,
):
  output_file = f"data/{destination_file}.csv"
  data = extract()

  if(data_frame_index_label != None):
    data.to_csv(f"{output_file}", index_label=data_frame_index_label)
  else:
    with open(output_file, "w") as f:
        f.write(f"{headers}\n")
        for hand in data:
            f.write(f"{data_map(hand)}\n")

  print(f"Arquivo gerado com sucesso: {output_file}")