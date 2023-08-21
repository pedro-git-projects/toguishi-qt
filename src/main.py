from blade.blade import Blade
from blade.brand import BladeBrand
from blade.model import BladeModel
from item.defects import Defects


def main():
    defec = {"defect1": "description1", "defect2": "description2"}
    deff = Defects(**{"defect1": "description1", "defect2": "description2"})
    print(repr(deff))
    b = Blade(BladeBrand.WAHL, BladeModel.CINCO_F, Defects(**defec))
    print(b)


if __name__ == "__main__":
    main()
