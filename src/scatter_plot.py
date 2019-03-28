import matplotlib.pyplot as plt
import numpy as np
from typing import List


def scatterplot(
        x_data: List[float],
        y_data: List[float],
        x_label: str = "",
        y_label: str = "",
        title: str = "",
        color: str = "r",
        yscale_log: bool = False
) -> None:
    '''Docstring'''
    # Create the plot object
    fig, ax = plt.subplots()

    print(fig)

    # Plot the data, set the size (s), color and transparency (alpha)
    # of the points
    ax.scatter(x_data, y_data, s=10, color=color, alpha=0.75)

    if yscale_log == True:
        ax.set_yscale('log')

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    # plt.show()
    fig.savefig('output.png', bbox_inches='tight')


scatterplot([1, 2, 3, 4, 5], [1, 3, 2, 4, 5])
