from manim import *
import math

class PieChart(VGroup):
    def __init__(self, data, colors=None, radius=.9, label_scale=0.2, **kwargs):
        super().__init__(**kwargs)
        total = sum(data.values())
        angle_start = 0
        self.slices = []
        self.labels = []

        if colors is None:
            colors = color_gradient([BLUE, GREEN, YELLOW, RED], len(data))

        for i, (label, value) in enumerate(data.items()):
            angle_span = (value / total) * TAU
            wedge = AnnularSector(
                inner_radius=0,
                outer_radius=radius,
                angle=angle_span,
                start_angle=angle_start,
                color=colors[i % len(colors)],
                stroke_width=1,
            )
            wedge.set_fill(color=wedge.get_fill_color(), opacity=0.5)
            self.slices.append(wedge)
            self.add(wedge)

            # Add label
            mid_angle = angle_start + angle_span / 2
            label_pos = radius * .7 * np.array([math.cos(mid_angle), math.sin(mid_angle), 0])
            label_text = Text(label).scale(label_scale).move_to(label_pos)
            self.labels.append(label_text)
            self.add(label_text)

            angle_start += angle_span

class WholeScene(Scene):
    def construct(self):
        self.title_sequence("How many visits do inmates get?", 18)
        self.make_pie_chart()
        Scene.clear(self)
        self.title_sequence("How many infractions do inmates get?", 13)

    def title_sequence(self, text, size):
        # Initial large title
        title = Text(text, font_size=size)

        # Step 1: Animate it onto the center
        self.play(Write(title))
        self.wait(1.5)  # Pause to linger

        # Step 2: Shrink and move to top
        title_target = title.copy().scale(0.5).shift(UP)

        self.play(Transform(title, title_target))
        self.wait(0.5)

    def make_pie_chart(self):
        data = {
            "Many": 5,
            "Some": 20,
            "None": 75
        }

        pie_chart = PieChart(data)
        pie_chart.move_to(ORIGIN)
        pie_chart.labels[0].shift(DOWN*.04)
        pie_chart.labels[-1].move_to(ORIGIN).shift(DOWN*.3)

        for wedge, label in zip(pie_chart.slices, pie_chart.labels):
            self.play(
                Create(wedge),
                FadeIn(label, shift=UP)
            )
            self.wait(2)  # optional pause between each

        self.wait(2)

        for i, d in enumerate(data):
            if i < len(data) - 1:
                self.play(
                        FadeOut(pie_chart.slices[i]),
                        FadeOut(pie_chart.labels[i])
                )
                self.wait(1)
        msg = Text("~75% of inmates studied had no visitors", font_size=14)
        bg = BackgroundRectangle(msg, fill_opacity=0.5, fill_color=BLACK, buff=0.1)
        group = VGroup(bg, msg)

        self.play(ReplacementTransform(pie_chart.labels[-1], group))

        self.wait(2)
        self.play(
                FadeOut(msg),
                FadeOut(pie_chart.slices[-1])
        )


