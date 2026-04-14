for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)

n=0
while n < 10:
    print(n, 'while')
    n += 1

products = ["iPhone", "iPad", "MacBook"]
regions = ["US", "EU", "ASIA"]
revenues = [1000, 2000, 3000]

for product in products:
    for region in regions:
        print(f"{product} {region}")