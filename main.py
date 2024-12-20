import argparse
import matplotlib.pyplot as mpl
import numpy as np

from distitribution import Distribution

def chart(distribution: Distribution):
    fig, ax = mpl.subplots()
    ax.bar(distribution.value, distribution.probably, color='#3452ad')
    ax.set_ylim(0, 1)
    ticks = np.unique(np.concatenate((distribution.probably, np.linspace(0, 1, 5))))
    ax.set_yticks(ticks)
    ax.grid(which='major', linestyle='--', linewidth=0.5, color='gray')
    ax.set_title('Distribution')
    ax.set_ylabel('Probability')
    ax.set_xlabel('Value')
    mpl.show()

def main():
    parser = argparse.ArgumentParser('Random distributions')
    parser.add_argument('value', type=int, nargs='+', help='List of results')
    parser.add_argument('--numbers', type=int, nargs='+', help='List of numbers')
    args = parser.parse_args()

    distribution = Distribution(args.value, args.numbers)
    chart(distribution)

if __name__ == '__main__':
    main()