import random
import matplotlib.pyplot as plt

# 設定物品重量及價值
weights = [70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120]
values = [135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240]

# 背包大小限制
max_weight = 750

# 設定爬山演算法參數
num_iterations = 500
num_neighbors = 1

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

# 儲存每個迭代步驟的最佳解及對應的收斂函數值
best_solutions = []
best_values = []

# 開始迭代
for i in range(num_iterations):
    best_neighbor = current_solution
    best_neighbor_value = calculate_value(current_solution)
    # 找到最好的鄰居解
    for j in range(num_neighbors):
        neighbor = current_solution[:]
        index = random.randint(0, len(current_solution) - 1)
        neighbor[index] = 1 - neighbor[index]
        neighbor_value = calculate_value(neighbor)
        # 如果鄰居的目標函數值比目前狀態的值高，則更新狀態
        if neighbor_value > best_neighbor_value:
            best_neighbor = neighbor
            best_neighbor_value = neighbor_value
    # 比較最好的鄰居解和當前解
    if best_neighbor_value > calculate_value(current_solution):
        current_solution = best_neighbor
    # 儲存每個迭代步驟的最佳解及對應的收斂函數值
    best_solution = current_solution
    best_value = calculate_value(current_solution)
    best_solutions.append(best_solution)
    best_values.append(best_value)

# 繪製收斂函數圖形
plt.plot(best_values)
plt.xlabel('Iteration')
plt.ylabel('Convergence Function')
plt.title('Convergence of Hill Climbing Algorithm')
plt.show()

# 顯示最佳解
print("Best solution:", best_solution)
print("Best value:", best_value)