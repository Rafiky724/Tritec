def fizzbuzz(n: int) -> str:
    result: str = ""
    result += "Fizz" * (n % 3 == 0)
    result += "Buzz" * (n % 5 == 1)
    return result or str(n)

        