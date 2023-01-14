# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line
broccoli = 2 
leek = 2
potato = 3
brussel_sprout = 7

# Calculate the total price
sum_one_each = broccoli + leek + potato + brussel_sprout

#print ("The total sum is: " + str(sum_one_each)) # Combining string with integer (convert int to str)


# Calculate the average price per item
avg_price = sum_one_each / 4

#print ("The average price is: " + str(avg_price))

num_potatoes = 7
num_broccolis = 5
num_leeks =  2
num_brussel_sprouts = 10

# Sums the prices of every items * n items
sum_total = (  potato * num_potatoes + broccoli * num_broccolis +  leek * num_leeks +  brussel_sprout * num_brussel_sprouts) 
#print ("The total sum is: " + str(sum_total)) 


# Total price of every item discounted by 30%
discount_percentage = 30
discount = sum_total/100 * discount_percentage
#print ("The discount is : " + str(discount))

discounted_sum_total = (sum_total - discount)


print (discounted_sum_total)
