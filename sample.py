
def fizzbuzz(int):
    if int % 5 == 0 and int % 3 == 0:
        return "FizzBuzz"

    elif int % 5 == 0:
        return "Buzz"
       
    elif int % 3 == 0:
        return "Fizz"

    return int