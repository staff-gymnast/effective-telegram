from manim import *

class CalculusVideo(Scene):
    def construct(self):
        self.play_calculus_intro()
        self.play_limits()
        self.play_derivative()
        self.play_integration()

    def play_calculus_intro(self):
        title = Text("Introduction to Calculus")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

    def play_limits(self):
        title = Text("Limits")
        definition = Text("The limit of a function is the value that the function approaches as the input approaches some value.")
        self.play(Write(title))
        self.wait(2)
        self.play(Transform(title, definition))
        self.wait(2)
        self.play(FadeOut(title))

    def play_derivative(self):
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 8, 1],
            axis_config={"color": BLUE},
        )

        graph = axes.plot(lambda x: x**2, color=WHITE)
        tangent_line = TangentLine(
            graph, alpha=0.5, length=5, color=RED
        )

        self.play(Create(axes))
        self.play(Create(graph))
        self.wait(1)
        self.play(Create(tangent_line))
        self.wait(2)
        self.play(FadeOut(axes), FadeOut(graph), FadeOut(tangent_line))

    def play_integration(self):
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 10, 1],
            axis_config={"color": BLUE},
        )

        graph = axes.plot(lambda x: x**2, color=WHITE)
        area = axes.get_area(graph, x_range=[1, 3], color=[GREEN, BLUE])

        self.play(Create(axes))
        self.play(Create(graph))
        self.wait(1)
        self.play(Create(area))
        self.wait(2)
