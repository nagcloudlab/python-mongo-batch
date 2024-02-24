
priceMatrix={
        "123":200.00,
        "456":400.00,
        "789":500.00
    }

class PriceMatrix:
    def get_price(self, item):
        return priceMatrix[item]