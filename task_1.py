from pulp import *

# Ініціалізація моделі
model = LpProblem("Maximize_Profit", LpMaximize)

# Оголошення змінних рішення
Lemonade = LpVariable("Lemonade", lowBound=0, cat='Integer')
Fruit_Juice = LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

# Обмеження ресурсів
water_constraint = 2 * Lemonade + Fruit_Juice <= 100
sugar_constraint = Lemonade <= 50
lemon_juice_constraint = Lemonade <= 30
fruit_puree_constraint = 2 * Fruit_Juice <= 40

# Додавання обмежень до моделі
model += water_constraint
model += sugar_constraint
model += lemon_juice_constraint
model += fruit_puree_constraint

# Функція максимізації
model += Lemonade + Fruit_Juice

# Вирішення задачі
model.solve()

# Виведення результату
print("Production of Lemonade:", Lemonade.varValue)
print("Production of Fruit Juice:", Fruit_Juice.varValue)
