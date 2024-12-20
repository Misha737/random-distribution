import argparse
import matplotlib.pyplot as mpl
import numpy as np
import mplcursors

from distitribution import Distribution

def chart(distribution: Distribution):
    fig, ax = mpl.subplots()
    bars = ax.bar(distribution.value, distribution.probably, color='#3452ad', align='center', label='Probability')

    ax.set_ylim(0, 1)
    ticks_y = np.linspace(0, 1, 9)
    ax.set_yticks(ticks_y)

    ticks_x = distribution.value
    ax.set_xticks(ticks_x)

    ax.grid(which='major', linestyle='--', linewidth=0.5, color='gray')
    ax.set_title('Distribution')
    ax.set_ylabel('Probability')
    ax.set_xlabel('Value')

    ax.axvline(x=distribution.expected_value(), color='green', linestyle='-', linewidth=2, label='Expected Value')
    ax.legend(title=f'Variance: {round(distribution.variance(), 2)}')

    mplcursors.cursor(bars, hover=True).connect(
    "add", lambda sel: sel.annotation.set_text(f"Значення: {sel.target[1]}")  # Виводимо тільки значення y
)
    mpl.show()

def main():
    parser = argparse.ArgumentParser('Random distributions')
    parser.add_argument('value', type=int, nargs='+', help='List of values')
    parser.add_argument('--numbers', '-n', type=float, nargs='+', help='List of numbers')
    args = parser.parse_args()

    distribution = Distribution(args.value, args.numbers)
    chart(distribution)

if __name__ == '__main__':
    main()