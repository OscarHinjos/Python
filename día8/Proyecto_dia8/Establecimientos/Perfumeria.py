class Perfumeria:
    n_rutno = 0

    @classmethod
    def turnos(cls):
        cls.n_rutno += 1
        yield f"P-{cls.n_rutno}"




