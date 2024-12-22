# def invest(amount, rate, years):

# year 1: $105.00
# year 2: $110.25
# year 3: $115.76
# year 4: $121.55

def invest(amount, rate, years):
    for i in range(1, years + 1):
        amount = amount * (1 + rate)
        print(f"year {i}: ${amount:.2f}")

print(invest(100, 0.05, 4))