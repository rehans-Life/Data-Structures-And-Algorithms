def factorial(n):
    # Base Condition

    # We know factorial of 1 is 1:
    if n in [0,1]:
        return 1

    # For example factorial of 4! can be written as 4 * (3)!    

    return n * factorial(n - 1)

print(factorial(18))

# Now im going to make a diagram in my notebook to completly
# understand whats happening behind the scenes.