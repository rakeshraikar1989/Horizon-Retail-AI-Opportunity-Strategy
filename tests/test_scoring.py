import pytest
from src.scoring import weighted_score, rank_cases, scenario_override
W=[.30,.20,.20,.15,.15]
CASES=[('Inventory Demand Forecasting',[5,3,3,3,3]),('Customer Enquiry Automation',[4,3,4,4,4]),('AI-Assisted Marketing',[4,2,3,2,3]),('AI-Assisted Store Inspection',[3,1,2,3,2])]

def test_original_results():
    assert [weighted_score(s,W) for _,s in CASES] == [3.6,3.8,2.95,2.25]

def test_original_ranking():
    assert rank_cases(CASES,W)[0]['Use Case']=='Customer Enquiry Automation'

def test_sensitivity_reverses_leader():
    revised=scenario_override(CASES,'Customer Enquiry Automation',1,1)
    assert weighted_score(revised[1][1],W)==3.4
    assert rank_cases(revised,W)[0]['Use Case']=='Inventory Demand Forecasting'

@pytest.mark.parametrize('scores,weights', [([0,3,4,4,4],W),([4,3,4,4,4],[.2]*4),([4,3,4,4,6],W)])
def test_invalid_input(scores,weights):
    with pytest.raises(ValueError): weighted_score(scores,weights)
