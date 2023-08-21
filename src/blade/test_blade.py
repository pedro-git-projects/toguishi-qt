import pytest
from blade.blade import Blade
from blade.brand import BladeBrand
from blade.model import BladeModel

from item.defects import Defects


@pytest.fixture
def sample_defects():
    return {"defect1": "description1", "defect2": "description2"}


def test_defects_str(sample_defects):
    deff = Defects(**sample_defects)
    expected_str = "defect1: description1, defect2: description2"
    assert str(deff) == expected_str


def test_defects_repr(sample_defects):
    deff = Defects(**sample_defects)
    expected_repr = "Defects(**{'defect1': 'description1', 'defect2': 'description2'})"
    assert repr(deff) == expected_repr


def test_blade_str(sample_defects):
    b = Blade(BladeBrand.WAHL, BladeModel.CINCO_F, Defects(**sample_defects))
    expected_str = (
        "Marca: WAHL\t "
        "Modelo: CINCO_F\t "
        "Defeitos: defect1: description1, defect2: description2"
    )
    assert str(b) == expected_str


def test_blade_repr(sample_defects):
    b = Blade(BladeBrand.WAHL, BladeModel.CINCO_F, Defects(**sample_defects))
    expected_repr = (
        "Blade("
        "BladeBrand.WAHL, "
        "BladeModel.CINCO_F, "
        "Defects(**{'defect1': 'description1', 'defect2': 'description2'})"
        ")"
    )
    print(repr(b))
    assert repr(b) == expected_repr
