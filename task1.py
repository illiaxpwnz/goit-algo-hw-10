import pulp

# Створення проблеми лінійного програмування
problem = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('Fruit Juice', lowBound=0, cat='Continuous')
problem += lemonade + fruit_juice, "Total_Products"

# Обмеження на ресурси
problem += 2 * lemonade + 1 * fruit_juice <= 100, "Water"
problem += 1 * lemonade <= 50, "Sugar"
problem += 1 * lemonade <= 30, "Lemon_Juice"
problem += 2 * fruit_juice <= 40, "Fruit_Juice"

problem.solve()

print(f"Status: {pulp.LpStatus[problem.status]}")
print(f"Лимонад: {pulp.value(lemonade)} од.")
print(f"Фруктовий сік: {pulp.value(fruit_juice)} од.")
print(f"Загальна кількість напоїв: {pulp.value(problem.objective)}")
