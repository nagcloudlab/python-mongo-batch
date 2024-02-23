
priceMatrix={
        "123":100.00,
        "456":200.00,
        "789":300.00
    }

class PriceMatrix:
    def get_price(self, item):
        return priceMatrix[item]