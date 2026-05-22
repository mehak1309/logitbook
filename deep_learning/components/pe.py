import math

def positional_encoding(T, n_embd):
  PE = []
  for pos in range(T):
    row = []
    for i in range(n_embd):
      angle = pos / (10000 ** (2 * (i // 2) / n_embd))
      if i % 2 == 0:
        row.append(math.sin(angle))
      else:
        row.append(math.cos(angle))
      PE.append(row)
  return PE
  
pe = positional_encoding(4, 8)
print(pe)