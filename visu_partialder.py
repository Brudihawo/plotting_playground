"""Visualise mixed partial derivatives."""
from matplotlib import pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap
import numpy as np

from plotting import plot_func3d


def sinxy(xs, ys):
    """Caclulate sin(x * y)."""
    return np.sin(xs * ys)


def d_dxy_sinxy(xs, ys):
    """Calculate first mixed derivative of sin(x * y)."""
    return np.cos(xs * ys) - xs * ys * np.sin(xs * ys)


def simple_poly(xs, ys):
    """Calculate x^2 * y + 2 * y^3 * x."""
    return np.power(xs, 2) * ys * np.power(ys, 3) * xs


def simple_poly_d_dxy(xs, ys):
    """Derivative of simple_poly."""
    return 2 * xs + 6 * np.power(ys, 2)


def main():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # plot_func3d(simple_poly, ax=ax, name="x^2 * y + 2 * y^3 * x",
    #             show=False,
    #             color='tab:orange')

    # plot_func3d(simple_poly_d_dxy, ax=ax, name="d_dx_dy",
    #             show=True, color='tab:blue')

    coords = np.linspace(-4, 4, 150)
    xs, ys = np.meshgrid(coords, coords)

    zs = sinxy(xs, ys)
    dvals = d_dxy_sinxy(xs, ys)

    norm = Normalize()
    norm.autoscale(dvals)

    cmap = get_cmap('viridis')
    colors = cmap(norm(dvals))

    surf = ax.plot_surface(xs, ys, zs, facecolors=colors, cstride=1, rstride=1)
    plt.colorbar(surf)
    plt.show()


if __name__ == '__main__':
    main()
