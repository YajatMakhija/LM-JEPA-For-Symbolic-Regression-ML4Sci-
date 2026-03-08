"""
operators.py — Operator definitions

Defines all operators, their arities, and default weights.
Weights can be overridden by scanning real data (see scanner.py).
"""

# Each operator: arity and default weight
OPERATORS = {
    # binary
    "ADD":  {"arity": 2, "weight": 15},
    "SUB":  {"arity": 2, "weight": 12},
    "MUL":  {"arity": 2, "weight": 25},
    "DIV":  {"arity": 2, "weight": 18},
    "POW":  {"arity": 2, "weight": 10},
    # unary
    "sin":  {"arity": 1, "weight": 5},
    "cos":  {"arity": 1, "weight": 5},
    "exp":  {"arity": 1, "weight": 5},
    "sqrt": {"arity": 1, "weight": 3},
    "log":  {"arity": 1, "weight": 2},
    "NEG":  {"arity": 1, "weight": 5},
}

# default variable pool
DEFAULT_VARS = [
    "theta", "x", "y", "z",
    "x1", "x2", "x3", "x4", "x5",
    "t", "m", "r", "v", "a", "F", "E",
    "q", "c", "G", "k",
    "sigma", "epsilon", "omega", "phi", "psi", "rho", "mu",
]

# safe POW exponents (avoids overflow)
SAFE_EXPONENTS = [2, 3, -1, -2, 0.5, -0.5, 1.5, 1.0/3]


def get_names():
    return list(OPERATORS.keys())


def get_weights():
    return {op: OPERATORS[op]["weight"] for op in OPERATORS}


def get_arity(op):
    return OPERATORS[op]["arity"]


if __name__ == "__main__":
    print("Operators:")
    for op, cfg in OPERATORS.items():
        print(f"  {op:6s}  arity={cfg['arity']}  weight={cfg['weight']}")
    print(f"\nDefault variables: {DEFAULT_VARS}")