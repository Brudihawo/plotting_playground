"""Testing the plotting library."""
import numpy as np
from plotting import plot_func3d


def sinxy(xs, ys):
    """Calculate sin (x * y)."""
    return np.sin(xs * ys)

def main():
    plot_func3d(sinxy)


if __name__ == "__main__":
    main()
