import cProfile
from memory_profiler import profile

@profile
def my_function():
    result = []
    for i in range(10000):
        result.append(i * i)
    return result

if __name__ == "__main__":
    cProfile.run('my_function()')
    my_function()

