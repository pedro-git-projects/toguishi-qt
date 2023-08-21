class Defects:
    def __init__(self, **defects):
        self.defects = defects

    def __iter__(self):
        return iter(self.defects.items())

    def __repr__(self):
        defect_items = ", ".join(
            [
                f"'{defect}': '{description}'"
                for defect, description in self.defects.items()
            ]
        )
        return f"Defects(**{{{defect_items}}})"

    def __str__(self):
        return ", ".join(
            [f"{defect}: {description}" for defect, description in self.defects.items()]
        )
