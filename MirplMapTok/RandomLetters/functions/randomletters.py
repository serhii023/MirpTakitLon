import random
import string

# next isn't necessary
# ALPHA_NUMERIC = string.ascii_letters + string.digits

def randname(size_from: int=50, size_to: int=70):
    """Returns random string-name with size in [50, 70]
    
    Args:
        size_from (int): lower bounder of random string name, must be greather 0.
        size_to (int): upper bounder of random string name, must be greather 0.
    """

    # TODO: write that function and delete placeholder

    random_name = ""
    for i in range(random.randint(size_from, size_to)):
        random_name += random.choice(string.ascii_lowercase)

    return random_name


def main():
    for i in range(20):
        print(randname(size_from=50, size_to=60))


if __name__ == "__main__":
    main()

