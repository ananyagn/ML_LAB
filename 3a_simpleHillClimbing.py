def f(x):
    return -x**2+10*x
def hill_climbing(start_x,step_size,max_iterations):
    x=start_x
    for i in range(max_iterations):
        current=f(x)
        next_x=x+step_size
        next_val=f(next_x)
        if next_val>current:
            x=next_x
        else:
            break
    return x,f(x)
result_x,result_val=hill_climbing(start_x=0,step_size=0.1,max_iterations=100)
print(f"Best x:{result_x}")
print(f"Maximum value:{result_val}")
