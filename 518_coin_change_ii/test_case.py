from solution import Solution

def __main__():
    solution_instance = Solution()
    print(solution_instance.change(5, [1,2,5]))
    print(solution_instance.change(3, [2]))
    print(solution_instance.change(0, [1,2]))
    print(solution_instance.change(10, [10]))

__main__()
