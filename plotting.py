"""Small Plotting Library for 3D function plots."""
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.cm import get_cmap
from matplotlib.colors import Normalize


def plot_func3d(func, n_samples=100, xbounds=(-1.0, 1.0), ybounds=(-1.0, 1.0),
                ax=None, name=None, show=True, form='wireframe', **kwargs):
    """Plot a 3D function.

    Args:
        func (callable): function with signature x, y -> z
        n_samples (int): number of samples per dimension
        xbounds (tuple(float)): bounds in x
        ybounds (tuple(float)): bounds in y
        ax: Optional, Axes to plot on
        name: Optional, function description. Defaults to function name
        form: 'wireframe' or 'surface'. How to plot the function
        **kwargs: kwargs to pass to maptlotlib.Axes3D.plot_surface or plot_wireframe
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
        plt.show()


def plot_surf_colorfunc3d(func, colorfunc, n_samples=100,
                          xbounds=(-1.0, 1.0), ybounds=(-1.0, 1.0),
                          ax=None, name=None, show=True, **kwargs):
    """Plot a 3D function as a surface and color by another function.

    Args:
        func (callable): function with signature x, y -> z
        n_samples (int): number of samples per dimension
        xbounds (tuple(float)): bounds in x
        ybounds (tuple(float)): bounds in y
        ax: Optional, Axes to plot on
        name (str): Optional, function description. Defaults to function name
        **kwargs: kwargs to pass to maptlotlib.Axes3D.plot_surface
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    coords = np.linspace(-2, 2, 100)
    xs, ys = np.meshgrid(coords, coords)

    zs = func(xs, ys)
    dvals = np.abs(colorfunc(xs, ys))

    norm = Normalize()
    norm.autoscale(dvals)

    cmap = get_cmap('viridis')
    colors = cmap(norm(dvals))

    surf = ax.plot_surface(xs, ys, zs, facecolors=colors)
    plt.colorbar(surf)
    plt.show()


def plot_func2d(func, n_samples=100, xbounds=(-1.0, 1.0),
                ax=None, name=None, show=True, form='line', **kwargs):
    """Plot a 2D function.

    Args:
        func (callable): function with signature x, y -> z
        n_samples (int): number of samples per dimension
        xbounds (tuple(float)): bounds in x
        ybounds (tuple(float)): bounds in y
        ax: Optional, Axes to plot on
        name: Optional, function description. Defaults to function name

    """
    xs = np.linspace(xbounds[0], xbounds[1], n_samples)
    ys = func(xs)

    if name is None:
        name = func.__name__

    if ax is None:
        fig, ax = plt.subplots()

    if form == 'line':
        ax.plot(xs, ys, label=name, **kwargs)
    elif form == 'scatter':
        ax.scatter(xs, ys, label=name, **kwargs)
    else:
        raise ValueError(f"Unknown plot type {form}")

    if show:
        plt.legend()
        plt.show()
