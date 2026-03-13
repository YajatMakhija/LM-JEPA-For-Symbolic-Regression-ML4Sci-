# LM JEPA For Symbolic Regression ML4Sci Yajat Makhija

A reduced-size LM-JEPA (Latent Masking Joint Embedding Predictive Architecture) approach to symbolic regression, developed as part of the ML4Sci evaluation tasks.

## Overview

This project applies JEPA-style self-supervised learning to discover symbolic expressions from numerical data. The model learns latent representations of equations and reconstructs them as symbolic token sequences.

**Evaluation tasks completed:** Common Task 1.1 · Specific Task 2.7

---

## Data Preprocessing (Task 1.1)

Structured pipeline to convert raw equations from `FeynmanEquations.csv` into a model-ready tokenized format.

**Steps:**

1. **Operator normalization** — `**` → `^`, operators mapped to word tokens (`*` → `MUL`, `^` → `POW`, etc.)
2. **Infix → Prefix conversion** — following [Lample & Charton (2019)](https://arxiv.org/abs/1904.01557)
3. **Constant masking** — numeric constants replaced with `<C_0>`, `<C_1>`, etc. (named constants like `pi`, `G`, `c` kept as variables)
4. **Vocabulary construction** — unique tokens extracted; variable names and ranges stored separately

**Example:**
```
Original:   (x1 + x2) / x3**2
Normalized: (x1 + x2) / x3^2
Prefix:     DIV ADD x1 x2 POW x3 2
```

### Synthetic Data Generation

Generated **50,000 synthetic expressions** to supplement the original 100 Feynman equations.

Operator weights were derived from scanning the Feynman dataset. Filtering was applied to remove trivial expressions, invalid operations (e.g. division by zero), and redundant forms (e.g. `exp(log(x))`).

---

## LM-JEPA Pretraining (Task 2.7)

### Approach 1 — Joint Training

Trained the context encoder, predictor, and target encoder together on 500 sampled data points per equation (Trained on AI Feynman dataset).

| Component | Epochs | Final Loss |
|-----------|--------|------------|
| Encoder + Predictor (MSE) | 100 | 0.11 |
| Decoder | 400 | 0.20 (94.5% train acc) |

**Result:** 49% exact match accuracy on Feynman equations.

### Approach 2 — Modular Training

Each component trained independently for better control (Trained on 50k Synthetic equations):

| Component | Method | Epochs | Result |
|-----------|--------|--------|--------|
| Target Encoder | Masked LM (15–20% masking) | 30 | Loss 1.87, 28% token acc on Feynman |
| Context Encoder | Transformer (4 heads, 2 layers, dim=128) | 20 | Cosine sim 0.047, MSE 0.02 |
| Decoder | GRU (2 layers, hidden=768) | 50 | Loss 1.21 |

**End-to-end result:** 10% token accuracy on synthetic data, 3% on Feynman. 0% exact match on both.

---

## Project Structure

```
├── Common_Task_1.1.ipynb                               # Data preprocessing pipeline
├── Specific_Task_2.7.ipynb                             # Approach 1 — joint training
├── TargetEncoder_ContextEncoder_Training.ipynb         # Approach 2 — target encoder (MLM)
├── decoder.ipynb                                       # Approach 2 — decoder (GRU)
├── testing.ipynb                                       # End-to-end inference & evaluation
├── data_scanner.ipynb                                  # Operator frequency analysis
├── data_generator.ipynb                                # Synthetic expression generation
└── data/
    ├── FeynmanEquations.csv
    ├── FeynmanEquations_Preprocessed.csv
    └── synthetic_data.csv
```

## Targets

- Optimize model efficiency
- Integration with LLMs

## References

- Lample & Charton, *Deep Learning for Symbolic Mathematics* (2019)
- LeCun et al., *A Path Towards Autonomous Machine Intelligence* (JEPA)
- Udrescu & Tegmark, *AI Feynman* datasetfurther improvements.
---

