from string import ascii_letters,digits
from random import sample
def get_rand_str(length):
    return ''.join(sample(ascii_letters+digits,k=length))

if __name__ == '__main__':
    print(get_rand_str(20))