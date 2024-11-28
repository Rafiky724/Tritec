def fizzbuzz(n):
    return "Fizz" * (n % 3 == 0) + "Buzz" * (n % 5 == 0) or str(n)