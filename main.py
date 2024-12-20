import argparse
import matplotlib.pyplot as mpl
import numpy as np
import mplcursors

from distitribution import Distribution

def chart(distribution: Distribution):
    fig, ax = mpl.subplots()
    bars = ax.bar(distribution.values, distribution.probably, color='#3452ad', align='center', label='Probability')

    ax.set_ylim(0, 1)
    ticks_y = np.linspace(0, 1, 9)
    ax.set_yticks(ticks_y)

    ticks_x = distribution.values
    ax.set_xticks(ticks_x)

    ax.grid(which='major', linestyle='--', linewidth=0.5, color='gray')
    ax.set_title('Distribution')
    ax.set_ylabel('Probability')
    ax.set_xlabel('Value')

    line = ax.axvline(x=distribution.expected_value(), color='green', linestyle='-', linewidth=2, label='Expected Value')
    ax.legend(title=f'Variance: {round(distribution.variance(), 2)}')
    if distribution.is_probably:
        ax.text(0.5, 1.02, 'Entered as a probability')

    mplcursors.cursor(bars, hover=True).connect(
    "add", lambda sel: sel.annotation.set_text(f"y: {sel.target[1]}")  # Виводимо тільки значення y
    )
    mplcursors.cursor(line, hover=True).connect(
        "add", lambda sel: sel.annotation.set_text(f"x: {sel.target[0]}")  # Виводимо тільки значення y
    )
    mpl.show()

def main():
    parser = argparse.ArgumentParser('Random distributions')
    parser.add_argument('values', type=int, nargs='+', help='List of values')
    parser.add_argument('--quantities', '-q', type=float, nargs='+', help='List of quantities')
    args = parser.parse_args()

    distribution = Distribution(args.values, args.quantities)
    chart(distribution)

if __name__ == '__main__':
    main()