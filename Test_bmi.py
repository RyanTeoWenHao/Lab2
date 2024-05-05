import bmi
def test_bmi_normal_weight():
    assert(bmi.calculate_bmi(1.65,55)==0)
def test_over_weight():
    assert(bmi.calculate_bmi(0.165,55)==1)
def test_under_weight():
    assert(bmi.calculate_bmi(16.5,55)==-1)
