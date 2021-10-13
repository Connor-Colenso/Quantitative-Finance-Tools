from rpy2.robjects.packages import importr
import rpy2.robjects.numpy2ri
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
from tools import estimate_parameters

# Import R module.
MASS = importr("MASS")

rpy2.robjects.numpy2ri.activate()


def normal_qq_plot(data, name):
    """
    :param data: Data to be compared against.
    :param name: Name of the plot.
    :return: None.
    """

    # Obtain gaussian approximation of data set.
    mu, sigma = estimate_parameters(data, len(data))

    # Obtain gaussian dist approximation of data set.
    lst = np.random.normal(loc=mu, scale=sigma, size=len(data))

    # Plot Gaussian dist vs data.
    plt.scatter(sorted(np.diff(np.log(data))), sorted(lst)[:-1],
                color="black", s=1)

    # Add red straight line at 45 degrees.
    z = np.linspace(min(lst), max(lst), 10000)
    plt.plot(z, z, color="red", lw=0.7,
             label="Comparison line")

    # Add axis labels, title and legend to clarify graph.
    plt.legend()
    plt.title("Normal Q-Q Plot")
    plt.xlabel("Sample Quantiles")
    plt.ylabel("Theoretical Quantiles")
    plt.savefig(f"{name}.png", dpi=1200)
    plt.show()


def student_t_qq_plot(data, name):
    """
    :param data: Data to be compared against.
    :param name: Name of the plot.
    :return: None

    Plots the data provided against a student-t distribution.
    """

    # Obtain necessary data.
    data_ln_diff = np.diff(np.log(data))
    mu, sigma, shape = MASS.fitdistr(data_ln_diff, "t")[0]

    # Obtain student t-dist approximation of data set.
    pdf = scipy.stats.t(df=shape, loc=mu, scale=sigma)
    lst = pdf.rvs(size=len(data_ln_diff))

    # Plot student t vs data.
    plt.scatter(sorted(data_ln_diff), sorted(lst),
                color="black", s=1)

    # Add red straight line at 45 degrees.
    z = np.linspace(min(data_ln_diff), max(data_ln_diff), 10000)
    plt.plot(z, z, color="red", lw=0.7,
             label="Comparison line")

    # Add axis labels, title and legend to clarify graph.
    plt.legend()
    plt.title("Student t Q-Q Plot")
    plt.xlabel("Sample Quantiles")
    plt.ylabel("Theoretical Quantiles")
    plt.savefig(f"{name}.png", dpi=1200)
    plt.show()