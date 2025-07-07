from manim import *
import math

class PieChart(VGroup):
    def __init__(self, data, colors=None, radius=1, label_scale=0.5, **kwargs):
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
            self.slices.append(wedge)
            self.add(wedge)

            # Add label
            mid_angle = angle_start + angle_span / 2
            label_pos = radius * 1.3 * np.array([math.cos(mid_angle), math.sin(mid_angle), 0])
            label_text = Text(label).scale(label_scale).move_to(label_pos)
            self.labels.append(label_text)
            self.add(label_text)

            angle_start += angle_span

class PieChartScene(Scene):
    def construct(self):
        data = {
            "Cats": 40,
            "Dogs": 35,
            "Rabbits": 25
        }

        pie_chart = PieChart(data)
        pie_chart.move_to(ORIGIN)

        self.play(*[
            GrowFromCenter(wedge)
            for wedge in pie_chart.slices
        ])
        self.play(*[
            FadeIn(label)
            for label in pie_chart.labels
        ])

        self.wait(2)

