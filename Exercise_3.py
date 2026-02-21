# Tuple
brands = ('Asrock','Asus','Gigabyte')

# Store brands in a temp variable
temp = list(brands)

# Change the third index
temp[2] = "EVGA"

# Store temp in a new brands variable
brands = tuple(temp)

# Print the tuple using a for loop
for brands in brands:
 print(brands)
