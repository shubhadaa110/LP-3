import time

# Recursive Fibonacci function
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# Non-Recursive (Iterative) Fibonacci function
def fib_non_recursive(n):
    n1, n2 = 0, 1
    print(n1, end=" ")
    if n > 1:
        print(n2, end=" ")
    for _ in range(2, n):
        n3 = n1 + n2
        print(n3, end=" ")
        n1, n2 = n2, n3
    print()

def main():
    n = int(input("Enter the number of elements in Fibonacci sequence: "))
    print("\nSelect the method to generate Fibonacci sequence:")
    print("1. Recursive")
    print("2. Non-Recursive (Iterative)")
    print("3. Both")
    choice = int(input("\nEnter your choice (1/2/3): "))

    if choice == 1 or choice == 3:
        print("\nFibonacci Sequence (Recursive): ", end="")
        start1 = time.time()
        for i in range(n):
            print(fib_recursive(i), end=" ")
        end1 = time.time()
        time_recursive = (end1 - start1) * 1_000_000  # microseconds
        print(f"\nTime Taken (Recursive): {time_recursive:.2f} microseconds")

    if choice == 2 or choice == 3:
        print("\nFibonacci Sequence (Non-Recursive): ", end="")
        start2 = time.time()
        fib_non_recursive(n)
        end2 = time.time()
        time_nonrecursive = (end2 - start2) * 1_000_000  # microseconds
        print(f"Time Taken (Non-Recursive): {time_nonrecursive:.2f} microseconds")

    # Time & Space Complexity Analysis
    if choice == 3:
        print("\n=== Time and Space Complexity Analysis ===")
        print(f"Recursive Time Taken: {time_recursive:.2f} microseconds")
        print("Recursive Time Complexity: O(2^n)")
        print("Recursive Space Complexity: O(n)\n")
        print(f"Non-Recursive Time Taken: {time_nonrecursive:.2f} microseconds")
        print("Non-Recursive Time Complexity: O(n)")
        print("Non-Recursive Space Complexity: O(1)")
if __name__ == "__main__":
    main()
