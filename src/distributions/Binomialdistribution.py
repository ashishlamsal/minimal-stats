import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution


class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) the total number of trials
    """

    #       A binomial distribution is defined by two variables:
    #           the probability of getting a positive outcome
    #           the number of trials

    #       If you know these two values, you can calculate the mean and the standard deviation
    #
    #       For example, if you flip a fair coin 25 times, p = 0.5 and n = 25
    #       You can then calculate the mean and standard deviation with the following formula:
    #           mean = p * n
    #           standard deviation = sqrt(n * p * (1 - p))

    #

    def __init__(self, prob=.5, size=20):
        self.p = prob
        self.n = size
        super().__init__(self.calculate_mean(), self.calculate_stdev())

    def calculate_mean(self):
        """Function to calculate the mean from p and n

        Args: 
            None

        Returns: 
            float: mean of the data set

        """

        self.mean = self.n * self.p
        return self.mean

    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.

        Args: 
            None

        Returns: 
            float: standard deviation of the data set

        """

        self.stdev = math.sqrt(self.n * self.p * (1 - self.p))
        return self.stdev

    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set.
        Assume that the data is a list of zeros and ones like [0 1 0 1 1 0 1]

        Args: 
            None

        Returns: 
            float: the p value
            float: the n value

        """

        self.n = len(self.data)
        self.p = self.data.count(1) / len(self.data)
        self.calculate_mean()
        self.calculate_stdev()
        return self.p, self.n

    def plot_bar(self):
        """Function to output a bar graph of the instance variable data using 
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """

        #       For example, say you have a coin where heads = 1 and tails = 0.
        #       If you flipped a coin 35 times, and the coin landed on
        #       heads 20 times and tails 15 times, the bar chart would have two bars:
        #       0 on the x-axis and 15 on the y-axis
        #       1 on the x-axis and 20 on the y-axis

        x = ['0', '1']
        y = [(1 - self.p) * self.n, self.p * self.n]

        # creating the bar plot
        plt.bar(x, y, color='maroon', width=0.2)
        plt.xlabel("Possible outcome")
        plt.ylabel("Count")
        plt.title("Bar graph of data")

        plt.show()

    def pmf(self, k):
        """Probability mass function calculator for the binomial distribution.

        Args:
            k (float): point for calculating the probability mass function


        Returns:
            float: probability mass function output
        """

        return math.comb(self.n, k) * pow(self.p, k) * pow(1 - self.p, self.n - k)

    def plot_bar_pmf(self):
        """Function to plot the pmf of the binomial distribution

        Args:
            None

        Returns:
            list: x values for the pmf plot
            list: y values for the pmf plot

        """

        # defining list of r values
        r_values = list(range(self.n + 1))

        # list of pmf values
        dist = [self.pmf(r) for r in r_values]

        # plotting the graph
        plt.bar(r_values, dist)
        plt.xlabel("Outcome")
        plt.ylabel("Probability")
        plt.title("Binomial distribution")
        plt.show()

        return r_values, dist

    def __add__(self, other):
        """Function to add together two Binomial distributions with equal p

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution

        """

        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError:
            raise

        return Binomial(self.p, self.n + other.n)

    def __repr__(self):
        """Function to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Binomial

        """
        
        return f'b = Binomial(p={self.p}, n={self.n})'

    def __str__(self):
        """Function to output the representation of the Binomial instance

        Args:
            None

        Returns:
            string: representation of the Binomial

        """

        return f'mean {self.mean}, standard deviation {self.stdev}, p {self.p}, n {self.n}'
