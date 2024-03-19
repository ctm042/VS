from time import time
import matplotlib.pyplot as plt
 
def example1(S):
    n = len(S)
    total = 0
    for j in range(n):
        total += S[j]
    return total
 
def example2(S):
    n = len(S)
    total = 0
    for j in range(0, n, 2):
        total += S[j]
    return total
 
def example3(S):
    n = len(S)
    total = 0
    for j in range(n):
        for k in range(1 + j):
            total += S[k]
    return total
 
def example4(S):
    n = len(S)
    prefix = 0
    total = 0
    for j in range(n):
        prefix += S[j]
        total += prefix
    return total

if __name__ == "__main__":
    #for (s in [])
    # Experiment setup
    # function_list = [example1, example2, example3, example4]
    # input_sizes = [10, 100, 1000, 10000,20000, 50000, 100000, 200000]
    # for func in function_list:
    #     execution_times = []
    #     for size in input_sizes:
    #         S = list(range(size)) # Creating input list
    #         start_time = time()
    #         func(S)
    #         end_time = time()
    #         execution_time = end_time - start_time
    #         execution_times.append(execution_time)
    #         print(f"Function {func.__name__} with input size {size}: Execution time = {execution_time}")

    #     plt.plot(input_sizes, execution_times, label=func.__name__)

    # plt.xlabel('Input Size')
    # plt.ylabel('Execution Time (s)')
    # plt.title('Runtime Analysis of Functions')
    # plt.legend()
    # plt.show()

    sizes = []
    for n in range(6,32):
        sizes.append(2**n)

    for size in sizes:
        print(size)

    for function in [example1, example2, example4]:
        times = []
        for size in sizes:
            start_time = time()
            function(range(size))
            end_time = time()
            print(f"{function.__name__}({size}) = {end_time-start_time}")
            with open('log.txt', 'a') as file:
                file.write(f"{function.__name__}\t{size}\t{end_time-start_time}\n")



            
