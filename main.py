import argparse
import matplotlib.pyplot as mpl
import numpy as np

from distitribution import Distribution

def chart(distribution: Distribution):
    fig, ax = mpl.subplots()
    ticks_x = range(distribution.probably.size)
    ax.bar(ticks_x, distribution.probably, color='#3452ad', align='center')

    ax.set_ylim(0, 1)
    # ticks_y = np.unique(np.concatenate((distribution.probably, np.linspace(0, 1, 5))))
    ticks_y = np.linspace(0, 1, 9)
    ax.set_yticks(ticks_y)

    ax.set_xlim(-0.5, distribution.value.size - 0.5)
    ax.set_xticks(ticks_x)
    ax.set_xticklabels(distribution.value)

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