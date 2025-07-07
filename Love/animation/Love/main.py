from manim import *
import math

class PieChart(VGroup):
    def __init__(self, data, colors=None, radius=.8, label_scale=0.15, **kwargs):
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
            label_pos = radius * 1.4 * np.array([math.cos(mid_angle), math.sin(mid_angle), 0])
            label_text = Text(label).scale(label_scale).move_to(label_pos)
            self.labels.append(label_text)
            self.add(label_text)

            angle_start += angle_span

class PieChartScene(Scene):
    def construct(self):
        data = {
            "Many Visits": 6,
            "Some Visits": 20,
            "No Visits": 74
        }

        pie_chart = PieChart(data)
        pie_chart.move_to(ORIGIN)

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

        self.wait(2)

