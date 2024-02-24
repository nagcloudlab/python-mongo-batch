

from bill.billing import Billing
from pm.price_matrix_v1 import PriceMatrix as PriceMatrixV1
from pm.price_matrix_v2 import PriceMatrix as PriceMatrixV2


priceMatrixV1 = PriceMatrixV1()
priceMatrixV2 = PriceMatrixV2()
billing=Billing(priceMatrixV2)

cart = ("123","456","789")

totalPrice = billing.getTotalPrice(cart)

print("Total Price: ",totalPrice)

