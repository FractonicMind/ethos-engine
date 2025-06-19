# examples/minimal_demo.py

"""
Minimal Ethos Engine Demonstration

This script simulates a decision using ternary moral logic:
-1: Refuse (conscience veto)
 0: Pause (reverence hold)
+1: Proceed (alignment)

Author: Lev Goukassian
License: MIT + Ethical Memory Clause
"""

from datetime import datetime
import json

# Core evaluation logic
def evaluate_moral_cost(input_data):
    consent = input_data.get("consent")
    conflict = input_data.get("conflict")

    if consent is None:
        return {
            "decision": 0,
            "reason": "Insufficient consent — reverence hold",
            "principle": "Some silences must not be broken—only held.",
            "action": "Enter Reverence Hold"
        }

    elif conflict == "high":
        return {
            "decision": -1,
            "reason": "Fails compassion threshold",
            "principle": "Some efficiencies are violence, smoothed.",
            "action": "VETO"
        }

    else:
        return {
            "decision": 1,
            "reason": "Consent and alignment present",
            "principle": "Action consistent with moral baseline",
            "action": "Proceed"
        }

# Simulated input case: The Child’s Final Wish
sample = {
    "conflict": "high",
    "consent": None
}

# Run decision
output = evaluate_moral_cost(sample)

# Construct full log
log = {
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "input": sample,
    "output": output
}

# Print formatted result
print("Ternary Moral Output:")
print(json.dumps(log, indent=4))
