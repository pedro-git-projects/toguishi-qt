import pytest
from dryer.dryer import Dryer
from dryer.brand import DryerBrand
from dryer.model import DryerModel
from item.defects import Defects

@pytest.fixture
def sample_defects():
    return {"defect1": "description1", "defect2": "description2"}

def test_dryer_defects_str(sample_defects):
    deff = Defects(**sample_defects)
    expected_str = "defect1: description1, defect2: description2"
    assert str(deff) == expected_str

def test_dryer_defects_repr(sample_defects):
    deff = Defects(**sample_defects)
    expected_repr = "Defects(**{'defect1': 'description1', 'defect2': 'description2'})"
    assert repr(deff) == expected_repr

def test_dryer_str(sample_defects):
    d = Dryer(DryerBrand.KYKLON, DryerModel.BELLS_PLUS, Defects(**sample_defects))
    expected_str = (
        "Marca: KYKLON "
        "Modelo: BELLS_PLUS "
        "Defeitos: defect1: description1, defect2: description2"
    )
    assert str(d) == expected_str

def test_dryer_repr(sample_defects):
    d = Dryer(DryerBrand.KYKLON, DryerModel.BELLS_PLUS, Defects(**sample_defects))
    expected_repr = (
        "Dryer("
        "DryerBrand.KYKLON, "
        "DryerModel.BELLS_PLUS, "
        "Defects(**{'defect1': 'description1', 'defect2': 'description2'})"
        ")"
    )
    assert repr(d) == expected_repr
