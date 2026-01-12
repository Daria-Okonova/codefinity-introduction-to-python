# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

b_price = "$1.50"
c_price = "$2.00"
p_price = "$5.40"

i = items.split(", ")
c = categories.split(", ")

candy1 = items[0:9]
candy2 = items[11:20]
dry_goods = items[22:]

cat1 = c[0]
cat2 = c[1]

print(f"we have {candy1} for {b_price} in the {cat1}")
	
print(f"we have {candy2} for {c_price} in the {cat1}")
	
print(f"we have {dry_goods} for {p_price} in the {cat2}")