pizza_orders = ['pepperoni', 'margherita', 'hawaiian', 'veggie', 'buffalo chicken']
finished_pizzas = []

while pizza_orders:
    current_pizza = pizza_orders.pop(0)
    print(f"Your {current_pizza} pizza pie is finished!")
    finished_pizzas.append(current_pizza)

print()
for pizza in finished_pizzas:
    print(f"The pizza {pizza} was made.")
