"""Small Plotting Library for 3D function plots."""
from matplotlib import pyplot as plt
import numpy as np


def plot_func3d(func, n_samples=100, xbounds=(-1.0, 1.0), ybounds=(-1.0, 1.0),
                ax=None, name=None, show=True, form='wireframe', **kwargs):
    """Plot a 2D function.

    Args:
        func (callable): function with signature x, y -> z
        n_samples (int): number of samples per dimension
        xbounds (tuple(float)): bounds in x
        ybounds (tuple(float)): bounds in y
        ax: Optional, Axes to plot on
        name: Optional, function description. Defaults to function name

    """
    xs, ys = np.meshgrid(
        np.linspace(xbounds[0], xbounds[1], n_samples),
        np.linspace(xbounds[0], xbounds[1], n_samples)
    )

    zs = func(xs, ys)

    if name is None:
        name = func.__name__

    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

    if form == 'wireframe':
        ax.plot_wireframe(xs, ys, zs, label=name, **kwargs)
    elif form == 'surface':
        ax.plot_surface(xs, ys, zs, label=name, **kwargs)
    else:
        raise ValueError(f"Unknown plot type {form}")

    if show:
        plt.legend()
        plt.show()
