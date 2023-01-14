# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line
Price_Broccoli = 2 
Price_Leek = 2
Price_Potato = 3
Price_Brussel_Sprout = 7

# Calculate the total price
sum_one_each = Price_Broccoli + Price_Leek + Price_Potato + Price_Brussel_Sprout

print ("The total sum is: " + str(sum_one_each)) # Combining string with integer (convert int to str)


# Calculate the average price per item
avg_price = sum_one_each / 4

print ("The average price is: " + str(avg_price))

Num_Potatoes = 7
Num_Broccoli = 5
Num_Leeks =  2
Num_Brussels_Sprout = 10

# Sums the prices of every items * n items
Sum_Total = (  Price_Potato * Num_Potatoes + Price_Broccoli * Num_Broccoli +  Price_Leek * Num_Leeks +  Price_Brussel_Sprout * Num_Broccoli) 
print ("The total sum is: " + str(Sum_Total)) 


# Total price of every item discounted by 30%
Discount_Percentage = ( 30 /100 )
Discounted_Sum_Total = (Sum_Total - Sum_Total * Discount_Percentage)
print ("The total price discount with 30% discount: "  + str(Discounted_Sum_Total))