# logitbook 📓

> *Building modern language models from the ground up — architectures, training, alignment, and interpretability.*

**by [Mehak Singal](https://github.com/mehak1309)**

---

This is my personal research notebook. Every folder is something I actually built and trained.

---

## what's inside

```
logitbook/
│
├── architectures/          # Model architectures built from scratch
│   ├── transformer/        # Attention is All You Need — the original
│   ├── gpt2/               # GPT-2: autoregressive language modelling
│   ├── llama/              # LLaMA 2/3: RoPE, GQA, RMSNorm
│   ├── bert/               # BERT: masked language modelling
│   └── mamba/              # Mamba: state space models
│
├── training/               # The full pipeline: pretrain → align
│   ├── pretraining/        # Next-token prediction on raw text
│   ├── sft/                # Supervised fine-tuning on instruction data
│   ├── rlhf/               # Reward modelling + PPO trainer
│   └── dpo/                # Direct Preference Optimisation
│
├── implementations/        # Key techniques, paper-faithful
│   ├── rope/               # Rotary Position Embeddings (Su et al. 2021)
│   ├── flash_attention/    # Memory-efficient attention (Dao et al. 2022)
│   ├── lora/               # Low-Rank Adaptation (Hu et al. 2021)
│   └── qlora/              # Quantised LoRA (Dettmers et al. 2023)
│
├── interpretability/       # What did the model actually learn?
│   ├── attention_viz/      # Visualising attention heads
│   ├── probing/            # Probing classifiers on hidden states
│   └── activation_patching/# Causal tracing of model behaviour
│


```

---

<!-- ## why this exists -->

<!-- I learn best by building things from scratch and writing about what confused me. Each implementation here comes with a `README.md` that explains:

- the core idea in plain language
- what I found surprising or non-obvious
- what broke and why
- links to the original paper

This is a living notebook, not a polished library. Expect rough edges — and honest ones. -->

---

<!-- ## the arc

The repo is structured to tell one coherent story:

```
build a transformer
    → pretrain it on raw text
        → fine-tune it to follow instructions (SFT)
            → align it to human preferences (RLHF / DPO)
                → understand what it actually learned (interpretability)
```

That pipeline is how every modern language model — GPT-4, Claude, Gemini — comes to exist. Understanding it end to end is the point. -->

---

## implementations

| module | paper | what it does |
|--------|-------|-------------|
| `architectures/transformer` | [Vaswani et al. 2017](https://arxiv.org/abs/1706.03762) | scaled dot-product attention, multi-head attention, encoder-decoder |
| `architectures/gpt2` | [Radford et al. 2019](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) | decoder-only autoregressive LM |
| `architectures/llama` | [Touvron et al. 2023](https://arxiv.org/abs/2302.13971) | RoPE, grouped query attention, RMSNorm, SwiGLU |
<!-- | `architectures/bert` | [Devlin et al. 2018](https://arxiv.org/abs/1810.04805) | masked LM, next sentence prediction |
| `architectures/mamba` | [Gu & Dao 2023](https://arxiv.org/abs/2312.00752) | selective state space model |
| `implementations/rope` | [Su et al. 2021](https://arxiv.org/abs/2104.09864) | rotary position embeddings |
| `implementations/flash_attention` | [Dao et al. 2022](https://arxiv.org/abs/2205.14135) | IO-aware exact attention |
| `implementations/lora` | [Hu et al. 2021](https://arxiv.org/abs/2106.09685) | low-rank weight adaptation |
| `implementations/qlora` | [Dettmers et al. 2023](https://arxiv.org/abs/2305.14314) | 4-bit quantised fine-tuning |
| `training/rlhf` | [Stiennon et al. 2020](https://arxiv.org/abs/2009.01325) | reward model + PPO |
| `training/dpo` | [Rafailov et al. 2023](https://arxiv.org/abs/2305.18290) | direct preference optimisation | -->

---

<!-- ## running anything

```bash
git clone https://github.com/mehak1309/logitbook.git
cd logitbook
pip install -r requirements.txt

# example: run the transformer
python architectures/transformer/transformer.py -->
```

<!-- Each folder has its own `README.md` with specific instructions and expected outputs.

--- -->
<!-- 
## experiments

The `experiments/` folder is where I write honestly about what happened — loss curves, surprises, failures, things I had to look up three times before they clicked. Some of the most useful entries are the ones where things didn't work. -->

---

<!-- ## what's coming

- [ ] Mamba implementation (in progress)
- [ ] Full RLHF pipeline with a small reward model
- [ ] Activation patching on a fine-tuned GPT-2
- [ ] Mixture of Experts (MoE) layer
- [ ] Speculative decoding -->

---

## connect

I write about everything I'm learning on [Substack](https://mehak1309.substack.com) and post updates on [LinkedIn](https://linkedin.com/in/mehak1309).

<!-- I write about everything I'm learning on [Substack](https://mehak1309.substack.com) and post updates on [X / Twitter](https://twitter.com/mehak1309) and [LinkedIn](https://linkedin.com/in/mehak1309). -->



---

*Built by [Mehak Singal](https://github.com/mehak1309)*