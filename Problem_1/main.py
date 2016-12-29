'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def main():
    multiples = [3, 5]
    total = 0
    for n in range(1000):
        if any(n % multiple == 0 for multiple in multiples):
            total += n
    print(total)

main()
