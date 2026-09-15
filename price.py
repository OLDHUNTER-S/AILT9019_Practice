def final_price(price, discount):
    return price * (1 - discount)

print(final_price(100, 0.2))
print(final_price(100, 0))


def discount_amount(price, discount):
    return price * discount