import random

def generate_matrix(rows, cols, min_val=-200, max_val=200):
    """Генерирует матрицу заданного размера со случайными числами."""
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(random.randint(min_val, max_val))
        matrix.append(row)
    return matrix

def add_matrices(matrix_1, matrix_2):
    """Складывает две матрицы одинаковой размерности."""
    if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
        raise ValueError("Матрицы должны иметь одинаковую размерность для сложения.")
    
    rows = len(matrix_1)
    cols = len(matrix_1[0])
    result = []
    
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix_1[i][j] + matrix_2[i][j])
        result.append(new_row)
    
    return result

# --- Пример использования для матрицы 10x10 ---
size_rows, size_cols = 10, 10
matrix_1 = generate_matrix(size_rows, size_cols)
matrix_2 = generate_matrix(size_rows, size_cols)
matrix_3 = add_matrices(matrix_1, matrix_2)

print("Матрица 1:")
for row in matrix_1:
    print(row)

print("\nМатрица 2:")
for row in matrix_2:
    print(row)

print("\nМатрица 3 (сумма):")
for row in matrix_3:
    print(row)

# --- Проверка на другой размерности (например, 4x3) ---
r, c = 4, 3
m1_small = generate_matrix(r, c)
m2_small = generate_matrix(r, c)
m3_small = add_matrices(m1_small, m2_small)

print(f"\nПроверка для матриц {r}x{c}:")
print("Малая матрица 1:", m1_small)
print("Малая матрица 2:", m2_small)
print("Малая матрица 3 (сумма):", m3_small)
