from manim import *
import numpy as np
import math

RED = "#FF644E"
BLUE = "#00a2ff"

class TaylorSeries(Scene):
    def construct(self):
        # Set the range for the x-axis
        x_range = (-12, 12)

        # Define the function for the sine curve
        def sine(x):
            return np.sin(x)

        # Define the function for the Taylor expansion
        def taylor_expansion(x, n):
            summation = 0
            for i in range(n + 1):
                term = (-1) ** i * x ** (2 * i + 1) / math.factorial(2 * i + 1)
                summation += term
            return summation

        # Create axes
        axes = Axes(
            x_range=x_range,
            y_range=(-2, 2),
            x_length=12,
            y_length=6,
            tips=False,
            axis_config = {"include_ticks": False},
        )

        # Plot the sine curve
        sine_curve = axes.plot(sine, color=RED)

        # Plot the Taylor expansion
        taylor_curve0 = axes.plot(lambda x: taylor_expansion(x, 0), color=BLUE)
        taylor_curve1 = axes.plot(lambda x: taylor_expansion(x, 1), color=BLUE)
        taylor_curve2 = axes.plot(lambda x: taylor_expansion(x, 2), color=BLUE)
        taylor_curve3 = axes.plot(lambda x: taylor_expansion(x, 3), color=BLUE)
        taylor_curve4 = axes.plot(lambda x: taylor_expansion(x, 4), color=BLUE)
        taylor_curve5 = axes.plot(lambda x: taylor_expansion(x, 5), color=BLUE)


        # Animate the plots
        #self.play(Create(axes))
        self.play(Create(sine_curve), run_time=3)
        self.play(Create(taylor_curve0), run_time=3)
        self.play(ReplacementTransform(taylor_curve0, taylor_curve1, clone=False), run_time=3/2)
        self.play(ReplacementTransform(taylor_curve1, taylor_curve2, clone=False), run_time=3/2)
        self.play(ReplacementTransform(taylor_curve2, taylor_curve3, clone=False), run_time=3/2)
        self.play(ReplacementTransform(taylor_curve3, taylor_curve4, clone=False), run_time=3/2)
        self.play(ReplacementTransform(taylor_curve4, taylor_curve5, clone=False), run_time=3/2)
        self.wait(2)