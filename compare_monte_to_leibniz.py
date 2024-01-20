import random
import math
import time


def monte_carlo_func(tolerance):
    """By analyzing the results of random samples,
    Monte Carlo method provides an estimate or approximation of the pi value.

    Args:
        tolerance (float): maximim allowable diffrence from the true value of pi

    Returns:
        float : an estimation of pi
    """

    in_circle = 0
    out_of_circle = 0
    monte_pi = 0

    while (
        abs(monte_pi - math.pi) > tolerance
    ):  #  Continue iterating until our estimated pi is within the tolerated
        rand_x = random.uniform(
            -1, 1
        )  # genetrates a float for random point on "X" axis
        rand_y = random.uniform(
            -1, 1
        )  # genetrates a float for random point on "Y" axis

        if (
            math.sqrt((rand_x**2) + (rand_y**2)) <= 1
        ):  # calculates the distance of the random point to the origin and compare it to the radian of the circle
            # if random point in the area of circle
            in_circle += 1
        else:
            out_of_circle += 1
        monte_pi = 4 * (in_circle / (in_circle + out_of_circle))
        # area of square =  2r*2r = 4r**2
        # area of circle =  pi*r**2
        # area of circle = pi* (area of square)/4
        # pi = 4 * (area of circle / area of square)   -> ⬆ used for calculation of monte_pi
    return monte_pi


def leibniz_func(tolerance):
    leibniz_pi = 1
    for i in range(1, 2**32):
        leibniz_pi += ((-1) ** i) / ((i * 2) + 1)
        if abs((math.pi - leibniz_pi * 4)) <= tolerance:
            break
    return 4 * leibniz_pi


def compare_funcs(func1, func2, tolerance, iter):
    """Compare two functions to estimate π by how fast they get close to the real pi.
    This function takes two functions, 'func1' and 'func2,' and sees which one is
    faster at estimating pi with a desired accuracy. It runs each method
    'iterations' times to make the comparison.

    Args:
        func1 : The first method to compare.
        func2 : The second method to compare.
        tolerance (float): How close the estimate needs to be to the real pi.
        iterations (int): How many times to run each method for comparison.

    Returns:
        tuple: A tuple with counts of which method was quicker to get close to pi
        in terms of time.
    """
    tottime_for_func1 = 0
    tottime_for_func2 = 0
    for i in range(iter):
        start_time_for_func1 = time.time()
        func1(tolerance)
        time_for_func1 = time.time() - start_time_for_func1
        start_time_for_func2 = time.time()
        func2(tolerance)
        time_for_func2 = time.time() - start_time_for_func2
        if time_for_func2 > time_for_func1:
            tottime_for_func1 += 1
        else:
            tottime_for_func2 += 1
    print("Summing Up...\n")
    time.sleep(1)
    return (tottime_for_func1, tottime_for_func2)


def main():
    print("Calculation in Progress...")
    tolerance = 1 / 1000
    iterations = 1000
    monte, leibniz = compare_funcs(monte_carlo_func, leibniz_func, tolerance, iterations)
    print(
        monte,
        " times out of a thousand the Monte Carlo method is faster than the Leibniz formula at converging to within one thousandth of the true value of pi  ",
    )


if __name__ == "__main__":
    main()

