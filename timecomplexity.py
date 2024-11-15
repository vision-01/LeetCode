import time
import numpy as np
from scipy.optimize import curve_fit

def measure_time(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time

def estimate_time_complexity(func, input_generator, sizes, *args, **kwargs):
    times = []
    for size in sizes:
        input_data = input_generator(size)
        exec_time = measure_time(func, input_data, *args, **kwargs)
        times.append(exec_time)
    
    def complexity_model(n, a, b):
        return a * np.log(n) + b
    
    params, _ = curve_fit(complexity_model, sizes, times)
    return params

# Example usage:
if __name__ == "__main__":
    def example_function(data):
        return sorted(data)

    def input_generator(size):
        return list(range(size, 0, -1))

    sizes = [10, 100, 1000, 10000]
    params = estimate_time_complexity(example_function, input_generator, sizes)
    print(f"Estimated time complexity: O(log(n)) with parameters: {params}")