from random import randint
import time


def calcule_factorial_without_memoization(n: int):
    if n == 0 or n == 1:
        return 1
    return n * calcule_factorial_without_memoization(n - 1)


def calcule_factorial_with_memoization(n: int, memo: dict):
    if n == 0 or n == 1:
        return 1
    elif memo.get(n) is not None:
        return memo[n]
    else:
        memo[n] = n * calcule_factorial_with_memoization(n - 1, memo)
        return memo[n]


def main():
    numbers = [randint(0, 500) for i in range(0, 10000)]

    print("=== WITHOUT MEMOIZE ===")
    start_time = time.time()
    for n in numbers:
        calcule_factorial_without_memoization(n)
    print(f"{time.time() - start_time} seconds")

    print("=== WITH MEMOIZE ===")
    memo = {}
    start_time = time.time()
    for n in numbers:
        calcule_factorial_with_memoization(n, memo)
    print(f"{time.time() - start_time} seconds")


if __name__ == "__main__":
    main()
