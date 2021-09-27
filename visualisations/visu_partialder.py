"""Visualise mixed partial derivatives."""
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.cm import get_cmap
from matplotlib.colors import Normalize

from plotting import plot_func3d
from plotting import plot_func2d
from plotting import plot_surf_colorfunc3d


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


def sq_diff_a(xs, ys, a):
    """Calculate a - x^2 - y^2."""
    return a - np.power(xs, 2) - np.power(ys, 2)


def circle(xs, ys):
    """Circular function."""
    return np.exp(- np.power(sq_diff_a(xs, ys, 4), 2))


def exp_func(xs):
    """Exponential function with offset."""
    return np.exp(-(np.power(xs - 4, 2))) + np.exp(-(np.power(xs + 4, 2)))


def d_dx_dy_circle(xs, ys):
    """Mixed derivative of cirular function."""
    return 8 * xs * ys * np.exp(- np.power(sq_diff_a(xs, ys, 4), 2)) \
        * (-1 + 2 * np.power(sq_diff_a(xs, ys, 4), 2))




def main():
    # plot_func3d(simple_poly, ax=ax, name="x^2 * y + 2 * y^3 * x",
    #             show=False,
    #             color='tab:orange',
    #             form="surface")

    # plot_func3d(simple_poly_d_dxy, ax=ax, name="d_dx_dy",
    #             show=True, color='tab:blue')

    # plot_func2d(exp_func, xbounds=(-4, 4))
    plot_surf_colorfunc3d(sinxy, d_dxy_sinxy)



if __name__ == '__main__':
    main()
