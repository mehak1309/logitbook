import torch

def online_softmax(x):
  # x (B, T, T)
  m = torch.full_like(x[..., :1], -float("inf")) # (B, T, 1) # running max
  d = torch.zeros_like(x[..., :1]) # (B, T, 1) running denominator
  for k in range(x.shape[-1]):
    xi = x[..., k:k+1] # (B, T, 1)
    max_m = torch.max(m, xi) # max_m so far
    d = d * torch.exp(m-max_m) + torch.exp(xi-max_m)
    m = max_m
  return torch.exp(x - max_m) / d