def f(x):
    return -x**2 + 10*x

def steepest_hill_climb(start_x, step_size, num_neighbors, max_iterations):
    x = start_x
    for _ in range(max_iterations):
        neighbors = [x + step_size * i for i in range(-num_neighbors, num_neighbors + 1)]
        best_x = x
        best_val = f(x)
        for nx in neighbors:
            val = f(nx)
            if val > best_val:
                best_x = nx
                best_val = val
        if best_x == x:
            break
        x = best_x
    return x, f(x)

result_x, result_val = steepest_hill_climb(start_x=0, step_size=0.1, num_neighbors=5, max_iterations=100)
print("Best x:", result_x)
print("Maximum value:", result_val)

    