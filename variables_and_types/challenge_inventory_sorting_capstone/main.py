# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

b_price = "$1.50"
c_price = "$2.00"
p_price = "$5.40"


itemsspl = items.split(", ")
categoriesspl = categories.split(", ")


candy1 = itemsspl[0]
candy2 = itemsspl[1]
dry_goods = itemsspl[2]

cat1 = categoriesspl[0]
cat2 = categoriesspl[1]


print (f"we have {candy1} for {b_price}" )
	
print ()
