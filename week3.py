def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        discount_amount = (price * discount_percent) / 100
        final_price = price - discount_amount
        return final_price
    else:
        return price


try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    
    final_price = calculate_discount(price, discount_percent)
    
    
    if discount_percent >= 20:
        print(f"The final price after applying the discount is: {final_price:.2f}")
    else:
        print(f"No discount was applied. The original price is: {price:.2f}")
except ValueError:
    print("Invalid input! Please enter numerical values for price and discount percentage.")
