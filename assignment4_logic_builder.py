# Assignment (17/02/2026)

# Assignment Name : Logic Builder
# Description : Print numbers 1–50
# with Fizz/Buzz logic and count occurrences using loops and functions.



def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

def fizzbuzz_range(start, end):
    
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0

    for i in range(start, end + 1):
        result = fizzbuzz(i)
        print(result)

        # Count occurrences
        if result == "Fizz":
            fizz_count += 1
        elif result == "Buzz":
            buzz_count += 1
        elif result == "FizzBuzz":
            fizzbuzz_count += 1
    print("\n--- Summary ---")
    print(f"Fizz occurred {fizz_count} times")
    print(f"Buzz occurred {buzz_count} times")
    print(f"FizzBuzz occurred {fizzbuzz_count} times")
fizzbuzz_range(1, 50)