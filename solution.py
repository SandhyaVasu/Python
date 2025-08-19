import bisect
import time
import matplotlib.pyplot as plt

def perfect_number_harmony_checker(n):
    if not isinstance(n, int) or n <= 0:
        return "input invalid"
    divisors = [1] if n != 1 else []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    if sum(divisors) == n and n != 0 and n != 1:
        return (True, divisors)
    else:
        return False


def collatz_chaotic_path_generator(n):
    if not isinstance(n, int) or n <= 0:
        return "input invalid"
    seq = []
    seen = set()
    limit = 1000 if n > 10**6 else None
    steps = 0
    current = n
    while True:
        seq.append(current)
        if current == 1:
            break
        if limit is not None and steps >= limit:
            seq.append("truncated")
            break
        if current in seen:
            # Loop detected, stop
            break
        seen.add(current)
        steps += 1
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3 * current + 1
    return seq


def is_prime(num):
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def next_prime_after(num):
    candidate = num + 1
    while True:
        if is_prime(candidate):
            return candidate
        candidate += 1


def prime_code_breaker(n):
    if not isinstance(n, int) or n < 0:
        return "input invalid"
    if n == 1:
        return "neither"
    if n < 2:
        return "input invalid"
    if is_prime(n):
        np = next_prime_after(n)
        return ('prime', np)
    else:
        return "composite"


def analyze_search_performance():
    targets = [1, 50000, 104000]
    nums = list(range(1, 100001))

    # Part 1: Search for targets in nums
    for target in targets:
        # Linear search timing
        start = time.perf_counter()
        found_linear = False
        for num in nums:
            if num == target:
                found_linear = True
                break
        end = time.perf_counter()
        linear_time = end - start

        # Binary search timing using bisect
        start = time.perf_counter()
        idx = bisect.bisect_left(nums, target)
        found_binary = (idx < len(nums) and nums[idx] == target)
        end = time.perf_counter()
        binary_time = end - start

        speedup = linear_time / binary_time if binary_time > 0 else float('inf')

        print(f"Target {target}: Linear search time = {linear_time:.6f} s, "
              f"Binary search time = {binary_time:.6f} s, Speedup = {speedup:.2f}")

    # Part 2: Compare worst-case (missing element) search times for variable sizes
    sizes = [10, 100, 1000, 10000, 100000, 1000000]
    linear_times = []
    binary_times = []
    for size in sizes:
        lst = list(range(1, size + 1))
        target = size + 1  # definitely not in list - worst case

        # Time linear search
        start = time.perf_counter()
        found_linear = False
        for num in lst:
            if num == target:
                found_linear = True
                break
        end = time.perf_counter()
        linear_times.append(end - start)

        # Time binary search
        start = time.perf_counter()
        idx = bisect.bisect_left(lst, target)
        found_binary = (idx < len(lst) and lst[idx] == target)
        end = time.perf_counter()
        binary_times.append(end - start)

    # Plot
    plt.figure(figsize=(10,6))
    plt.plot(sizes, linear_times, label='Linear Search')
    plt.plot(sizes, binary_times, label='Binary Search')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('List Size (log scale)')
    plt.ylabel('Search Time (seconds, log scale)')
    plt.title('Linear vs Binary Search Performance\n(Worst-case Missing Element)')
    plt.legend()
    plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.tight_layout()
    plt.savefig('search_performance.png')
