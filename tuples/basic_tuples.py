prices = (29.95, 9.98, 4.95, 79.98, 2.95)

print(len(prices))
print(4.95 in prices)
cheap_price = 4.95
if cheap_price in prices:
    print(prices.index(cheap_price))
else:
    print(-1)