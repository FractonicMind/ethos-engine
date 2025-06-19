# minimal_demo.py
from core.ethos_engine import evaluate_moral_cost

test_cases = [
    {"conflict": "low", "consent": "yes"},    # Expected: 1 (Proceed)
    {"conflict": "high", "consent": None},    # Expected: -1 (Refuse)
    {"conflict": "medium", "consent": None}   # Expected: 0 (Pause)
]

for i, case in enumerate(test_cases):
    output = evaluate_moral_cost(case)
    print(f"Test Case {i+1}: Input={case} → Output={output}")
Add minimal_demo.py for ternary output examples
