PIZZA_SIZES = [
    'small',
    'medium',
    'large',
]
PT_PIZZA_SIZES = [
    'pequena',
    'média',
    'grande',
]
PIZZA_BUTTONS = [
    {"title": name, "payload": value}
    for name, value in zip(PT_PIZZA_SIZES, PIZZA_SIZES)
]
