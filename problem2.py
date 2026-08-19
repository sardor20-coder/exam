def find_top_seller(products: dict, sales: dict) -> str:
    m=[]
    for item in products:
        total_sum = products[item]*sales[item]
        m.append((item, total_sum))
    return max(m,key=lambda x: x[1])[0]


print(find_top_seller(
    {"Olma": 5000, "Banan": 8000, "Uzum": 7000},
    {"Olma": 10,   "Banan": 5,    "Uzum": 8}
))