'''Docstring'''
from typing import List
import matplotlib.pyplot as plt
import matplotlib


def lineplot(
    x_data: List[float],
    y_data: List[float],
    x_label: str = "",
    y_label: str = "",
    title: str = ""
) -> None:
    '''Docstring'''
    # Create the plot object
    fig, ax = plt.subplots()

    # Plot the best fit line, set the linewidth (lw), color and
    # transparency (alpha) of the line
    ax.plot(x_data, y_data, lw=2, color='#539caf', alpha=1)

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    fig.savefig('output.png', bbox_inches='tight')


lineplot([1, 2, 3, 4, 5], [1, 3, 2, 4, 5])
