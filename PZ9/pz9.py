# находит наибольший и наименьший рост вручную, по тому что если использовать min и max меня пошлют и не примут работу......

height = {
    "Андрей": 178,
    "Виктор": 150,
    "Максим": 200,
}

max_h = None
min_h = None

for name in height:
    h = height[name]
    if max_h is None or h > max_h:
        max_h = h
    if min_h is None or h < min_h:
        min_h = h

print("Наибольший:", max_h)
print("Наименьший:", min_h)
