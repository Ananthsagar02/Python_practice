monthly_sales = [58, 52,40,44,46,33,56,44,55,66,77,88]
month_sales = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

thresold = 50

for sales_amount, month in zip(monthly_sales, month_sales):
    print(sales_amount, month)
    if sales_amount < thresold:
        print(f"Sales of {sales_amount} in {month} is less than the thresold of {thresold}.")
        break
    else:
        print(f"Sales of {sales_amount} in {month} is greater than the thresold of {thresold}.")