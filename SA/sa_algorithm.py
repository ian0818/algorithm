import random
import math
import matplotlib.pyplot as plt

# 設定物品重量及價值
weights = [70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120]
values = [135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240]

# 背包大小限制
max_weight = 750

# 設定模擬退火演算法參數
num_iterations = 500
initial_temperature = 750
cooling_rate = 0.1

# 隨機初始化一個解
current_solution = [random.choice([0, 1]) for i in range(len(weights))]

# 計算解的價值
def calculate_value(solution):
    total_weight = 0
    total_value = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            total_weight += weights[i]
            total_value += values[i]
    if total_weight > max_weight:
        return 0
    return total_value

# 計算能量差
def calculate_energy_difference(current_value, neighbor_value, temperature):
    return (neighbor_value - current_value) / temperature

# 儲存每個迭代步驟的最佳解及對應的收斂函數值
best_solutions = []
best_values = []

# 開始迭代
for i in range(num_iterations):
    temperature = initial_temperature * math.exp(-cooling_rate * i)
    # 找到一個鄰居解
    index = random.randint(0, len(current_solution) - 1)
    neighbor = current_solution[:]
    neighbor[index] = 1 - neighbor[index]
    # 計算當前解和鄰居解的價值
    current_value = calculate_value(current_solution)
    neighbor_value = calculate_value(neighbor)
    # 如果鄰居解的價值比當前解高，則接受鄰居解
    if neighbor_value > current_value:
        current_solution = neighbor
    # 如果鄰居解的價值比當前解低，則以一定機率接受鄰居解
    else:
        energy_difference = calculate_energy_difference(current_value, neighbor_value, temperature)
        acceptance_probability = math.exp(energy_difference)
        if random.random() < acceptance_probability:
            current_solution = neighbor
    # 儲存每個迭代步驟的最佳解及對應的收斂函數值
    best_solution = current_solution
    best_value = calculate_value(current_solution)
    best_solutions.append(best_solution)
    best_values.append(best_value)

# 繪製收斂函數圖形
plt.plot(best_values)
plt.xlabel('Iteration')
plt.ylabel('Convergence Function')
plt.title('Convergence of Simulated Annealing Algorithm')
plt.show()

# 顯示最佳解
print("Best solution:", best_solution)
print("Best value:", best_value)