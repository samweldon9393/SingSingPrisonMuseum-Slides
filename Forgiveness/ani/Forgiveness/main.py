from manim import *

class ParoleBoardFailure(Scene):
    def construct(self):
        # Title
        title = Text("How the NY Parole Board Fails", font_size=48, weight=BOLD).scale(0.2)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Subtitle
        subtitle = Text("An algorithm could reduce crime and racial bias while doubling parole", font_size=28).scale(0.2)
        self.play(FadeIn(subtitle, shift=DOWN))
        self.wait(2)
        self.play(FadeOut(subtitle))

        # Data Slide 1: Actual vs Potential Parole Release Rate
        actual = BarChart([20], y_range=[0, 100, 10], bar_names=["Actual"], bar_width=0.5).scale(0.2)
        potential = BarChart([49], y_range=[0, 100, 10], bar_names=["Potential"], bar_width=0.5).scale(0.2)
        actual_bar = actual.bars[0]
        potential_bar = potential.bars[0]
        actual_label = Text("Actual: 20%", font_size=24).next_to(actual_bar, UP).scale(0.2)
        potential_label = Text("With Algorithm: 49%", font_size=24).next_to(potential_bar, UP).scale(0.2)

        group = VGroup(actual, potential).arrange(RIGHT, buff=2)
        self.play(Create(actual), Write(actual_label))
        self.wait(1)
        self.play(Create(potential), Write(potential_label))
        self.wait(2)
        self.play(FadeOut(group), FadeOut(actual_label), FadeOut(potential_label))

        # Data Slide 2: Violent Reoffense Rate
        bars = BarChart([6, 2], y_range=[0, 10, 1], bar_names=["Board Decisions", "Algorithm"], bar_width=0.5).scale(0.2)
        bars_title = Text("3-Year Violent Reoffense Rate", font_size=36).next_to(bars, UP).scale(0.2)
        self.play(FadeIn(bars_title), Create(bars))
        self.wait(2)
        self.play(FadeOut(bars_title), FadeOut(bars))

        # Data Slide 3: Racial Disparity
        racial_chart = BarChart([25, 16], y_range=[0, 30, 5], bar_names=["White", "Black/Hispanic"],
                                bar_width=0.5).scale(0.2)
        racial_title = Text("Parole Rates by Race (2012–2015)", font_size=36).next_to(racial_chart, UP).scale(0.2)
        self.play(FadeIn(racial_title), Create(racial_chart))
        self.wait(2)
        self.play(FadeOut(racial_title), FadeOut(racial_chart))

        # Statement Slide: Data-Driven Reform
        message = Text("Using data, we could:", font_size=40).scale(0.2)
        bullet1 = Text("\u2022 Release twice as many people", font_size=32).next_to(message, DOWN).shift(DOWN * 0.5).scale(0.2)
        bullet2 = Text("\u2022 Cut violent reoffense rates in half", font_size=32).next_to(bullet1, DOWN).scale(0.2)
        bullet3 = Text("\u2022 Eliminate racial disparities", font_size=32).next_to(bullet2, DOWN).scale(0.2)

        self.play(Write(message))
        self.wait(0.5)
        self.play(Write(bullet1))
        self.wait(0.5)
        self.play(Write(bullet2))
        self.wait(0.5)
        self.play(Write(bullet3))
        self.wait(2)

        # Closing Message
        self.play(FadeOut(message, bullet1, bullet2, bullet3))
        close = Text("The New York Parole Board isn’t optimizing for safety.\nWe can do better.", font_size=36).scale(0.2)
        self.play(Write(close))
        self.wait(3)
        self.play(FadeOut(close))

