from dummyfw.util import mean
import numpy as np

# main method
def main():
    vec = np.array([2, 4, 6, 8, 10])
    print (f'The mean of the vector {vec} is {mean(vec)}')


if __name__ == "__main__":
    main()