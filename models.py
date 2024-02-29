class _Model:
    def body(self) -> dict:
        pass


class Company(_Model):
    def __init__(self, title: str, code: str):
        self.title = title
        self.code = code

    def body(self) -> dict:
        return {"title": self.title, "code": self.code}


class Stock(_Model):
    def __init__(self, cost: float):
        self.cost = cost

    def body(self) -> dict:
        return {"cost": self.cost}


class CompanyToStock(_Model):
    def __init__(self, company: Company, stock: Stock):
        self.company = company
        self.stock = stock

    def body(self) -> dict:
        return {
            "company": self.company.body(),
            "stock": self.stock.body(),
        }
