class Cosmeticos:
    n_rutno = 0

    @classmethod
    def turnos(cls):
        cls.n_rutno += 1
        yield f"C-{cls.n_rutno}"