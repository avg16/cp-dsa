n, m = map(int, input().split())
prices = list(map(int, input().split()))
neg_prices = [price for price in prices if price < 0]
neg_prices.sort(reverse=True)
total_earned = 0
for i in range(min(m, len(neg_prices))):
    total_earned += abs(neg_prices[i])

print(total_earned)