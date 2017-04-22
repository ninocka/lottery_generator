import random

def lottery():
    a = int(raw_input("Please enter how many random lottery numbers from 1 - 39 would you like to have: "))
    lotto = (random.sample(xrange(1, 40), a))
    for i in lotto:
        print i
    lotto_result = (sorted(lotto))
    print "Your LOTTERY numbers are %s, Good luck!" % str(lotto_result)[1:-1]  #str(lotto)[1:-1] shortens string for 1 character on both sides
    # random.sample(population, k) k = length list of unique elements chosen from the population sequence.
    # xrange for a sample from a range of integers
    # sorted - sorted list

def main():
        print "Welcome to the Lottery numbers generator."
        while True:
            game = raw_input("1 to start, 2 to quit: ")
            if game == "1":
                lottery()
            elif game == "2":
                print "Goodbye"
                exit()

if __name__ == "__main__":
    main()
