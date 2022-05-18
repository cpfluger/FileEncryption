import random


# Pre generated primes
first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]


#generate Primenumber of given bits length
def n_bit_random(n):
    return random.randrange(2 ** (n - 1) + 1, 2 ** n - 1)


def get_low_level_prime(n):

    while True:
        # Obtain a random number
        pc = n_bit_random(n)
        # Test divisibility by pre-generated
        # primes
        for divisor in first_primes_list:
            if pc % divisor == 0 and divisor ** 2 <= pc:
                break
        else:
            return pc


def is_miller_rabin_passed(mrc):
    #20 Miller Rabin tests
    max_divisions_by_two = 0
    ec = mrc - 1
    while ec % 2 == 0:
        ec >>= 1
        max_divisions_by_two += 1
    assert (2 ** max_divisions_by_two * ec == mrc - 1)


    def trial_composite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(max_divisions_by_two):
            if pow(round_tester, 2 ** i * ec, mrc) == mrc - 1:
                return False
        return True


    # Set number of trials here
    number_of_rabin_trials = 20
    for i in range(number_of_rabin_trials):
        round_tester = random.randrange(2, mrc)
        if trial_composite(round_tester):
            return False
    return True


#calculate euclidic algorithm
def euclidic_algorithm(dividend, divisor):
    quotient = 0
    rest = 1

    while(rest != 0 or rest != 0.0):
        quotient = dividend / divisor
        rest = dividend % divisor
        #print("{} : {} = {}; Rest: {}".format(dividend, divisor, quotient, rest))
        dividend = divisor
        divisor = rest
    return dividend


#checks wether 2 given numbers are relatively prime
def is_relatively_prime_to(relative_number, number_to_test):
    if euclidic_algorithm(relative_number, number_to_test) == (1 or 1.0):
        return True
    return False


#extended euclidic algorithm
def extended_euclidic_algortihtm(a, b):
    if b==0:
        return a, 1, 0
    else:
        g, u, v = extended_euclidic_algortihtm(b, a%b)
        q=a//b
        return g, v, u-q*v
