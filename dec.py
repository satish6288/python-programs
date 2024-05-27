import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result
    return wrapper

# Example usage
@time_decorator
def example_function(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

result = example_function(5)
print(f"Result: {result}")