# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

b_price = "$1.50"
c_price = "$2.00"
p_price = "$5.40"

i = items.split(", ")
c = categories.split(", ")

candy1 = i[0]
candy2 = i[1]
dry_goods = i[2]

cat1 = c[0]
cat2 = c[1]

print(f"we have {candy1} for {b_price} in the {cat1}")
	
print(f"we have {candy2} for {c_price} in the {cat1}")
	
print(f"we have {dry_goods} for {p_price} in the {cat2}")