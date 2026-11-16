"""Auditable weighted scoring for a fictional strategy case."""
from math import isclose

def weighted_score(scores, weights):
    if len(scores) != len(weights) or not scores:
        raise ValueError("Scores and weights must be nonempty and aligned")
    if not isclose(sum(weights), 1.0, abs_tol=1e-9):
        raise ValueError("Weights must sum to 1")
    if any(not isinstance(s, (int,float)) or isinstance(s,bool) or not 1 <= s <= 5 for s in scores):
        raise ValueError("Scores must be numbers between 1 and 5")
    if any(not isinstance(w, (int,float)) or isinstance(w,bool) or w < 0 for w in weights):
        raise ValueError("Weights must be nonnegative")
    return round(sum(s*w for s,w in zip(scores,weights)), 4)

def rank_cases(cases, weights):
    result = [{"Use Case": name, "Weighted Score": weighted_score(scores, weights)} for name, scores in cases]
    return sorted(result, key=lambda r: (-r["Weighted Score"], r["Use Case"]))

def scenario_override(cases, use_case, criterion_index, new_score):
    if not isinstance(criterion_index,int) or not 0 <= criterion_index < len(cases[0][1]):
        raise ValueError("Invalid criterion index")
    if not 1 <= new_score <= 5:
        raise ValueError("Scenario score outside 1..5")
    if use_case not in [name for name,_ in cases]:
        raise ValueError("Unknown use case")
    return [(name, [new_score if i==criterion_index and name==use_case else v for i,v in enumerate(scores)]) for name,scores in cases]
