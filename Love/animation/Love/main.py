from manim import *
import math

#with register_font("./monument-grotesk-regular.ttf"):
#    a = Text("Hello", font="Monument")

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
            label_text = Text(label, font="Monument Grotesk").scale(label_scale).move_to(label_pos)
            self.labels.append(label_text)
            self.add(label_text)

            angle_start += angle_span

class WholeScene(Scene):

    def construct(self):
        '''
        intro = Text("The importance of connection in prison", font_size=18, font="Monument Grotesk")
        self.play(Write(intro))
        self.wait(5)
        self.play(FadeOut(intro))

        self.title_sequence("How  many  visits do inmates get?", 18)
        visit_data = {
            "Many": 5,
            "Some": 20,
            "None": 75
        }
        visit_text = "~75% of inmates studied got no visits"
        self.make_pie_chart(visit_data, visit_text)
        Scene.clear(self)

        self.title_sequence("How many infractions do inmates get?", 13)
        misconduct_data = {
            "Many": 5,
            "Some": 26,
            "None": 69
        }
        misconduct_text = "~69% of inmates studied had no infractions"
        self.make_pie_chart(misconduct_data, misconduct_text)
        Scene.clear(self)

        self.title_sequence("Is there a connection between visits and misconduct?")
        expl = self.explanation_text()
        self.play(expl)
        self.wait(10)
        self.play(FadeOut(expl))

        '''

        self.wait(1)
        y_values = [66.8, 70.7, 78.0, 77.3]
        plane, graph, x_labels = self.line_graph(y_values, [60, 110, 10], '#0f19f5')
        self.add(plane)
        self.add(x_labels)
        self.wait(1)

        self.title_sequence("Here's how visit frequency impacts misconduct")
        graph_text = Text("This line represents inmates with no misconduct", font_size=13, font="Monument Grotesk")
        bg = BackgroundRectangle(graph_text, fill_opacity=0.5, fill_color=BLACK, buff=0.1)
        group = VGroup(bg, graph_text)
        group.set_z_index(1000)
        self.play(Write(group))
        self.wait(1)
        group.set_opacity(0.5)
        self.play(Create(graph), run_time=6)
        self.play(FadeOut(group))
        self.play(FadeOut(graph))


        graph_text = Text("This line represents inmates with heavy misconduct", font_size=13, font="Monument Grotesk")
        bg = BackgroundRectangle(graph_text, fill_opacity=0.5, fill_color=BLACK, buff=0.1)
        group = VGroup(bg, graph_text)
        group.set_z_index(1000)
        self.play(Write(group))
        self.wait(1)
        group.set_opacity(0.5)
        y_values = [5.6, 8.1, 0.7, 0]
        new_plane, graph, x_labels = self.line_graph(y_values, [-10, 20, 5], '#f50f0f')
        self.play(ReplacementTransform(plane, new_plane))
        self.wait(1)
        self.play(Create(graph), run_time=6)
        self.play(FadeOut(group))
        self.play(FadeOut(graph))


    def title_sequence(self, text, size=13):
        # Initial large title
        t = Text(text, font_size=size, font="Monument Grotesk")
        bg = BackgroundRectangle(t, fill_opacity=.5, fill_color=BLACK, buff=0.1)
        title = VGroup(bg, t)

        # Step 1: Animate it onto the center
        self.play(FadeIn(title))
        self.wait(2.5)  # Pause to linger

        # Step 2: Shrink and move to top
        title_target = title.copy().scale(0.5).shift(UP)

        self.play(Transform(title, title_target))
        self.wait(0.5)

    def make_pie_chart(self, data, text):

        pie_chart = PieChart(data)
        pie_chart.move_to(ORIGIN)
        pie_chart.labels[0].shift(DOWN*.035)
        pie_chart.labels[-1].move_to(ORIGIN).shift(DOWN*.3)

        for wedge, label in zip(pie_chart.slices, pie_chart.labels):
            self.play(
                Create(wedge),
                FadeIn(label, shift=UP)
            )
            self.wait(2)  # optional pause between each

        self.wait(2)

        small_slices = VGroup(pie_chart.slices[0], pie_chart.slices[1], pie_chart.labels[0], pie_chart.labels[1])
        self.play(FadeOut(small_slices))
        self.wait(1)
        msg = Text(text, font_size=14, font="Monument Grotesk")
        bg = BackgroundRectangle(msg, fill_opacity=0.5, fill_color=BLACK, buff=0.1)
        group = VGroup(bg, msg)

        self.play(ReplacementTransform(pie_chart.labels[-1], group))

        self.wait(2)
        self.play(
                FadeOut(msg),
                FadeOut(pie_chart.slices[-1])
        )

    def explanation_text(self):
        text1 = Text("A 2012 study by Joshua Cochran of FSU College of Criminology", font_size=8, font="Ubuntu Mono")
        text2 = Text("compared the frequency an inmate was visited over a one year", font_size=8, font="Ubuntu Mono")
        text3 = Text("period with the number of misconduct citations they received.", font_size=8, font="Ubuntu Mono")
        text4 = Text("By grouping together inmates with similar visit and infraction", font_size=8, font="Ubuntu Mono")
        text5 = Text("patterns, the study revealed that inmates who received more", font_size=8, font="Ubuntu Mono")
        text6 = Text("visits committed less misconduct.", font_size=8, font="Ubuntu Mono")
        group = VGroup(text1.shift(UP*.45), text2.shift(UP*.3), text3.shift(UP*.15), text4, text5.shift(DOWN*.15), text6.shift(DOWN*.3))
        return group

    def line_graph(self, y_values, y_range, color):
        plane = NumberPlane(
            x_range = (0, 5, 1),
            y_range = y_range,
            x_length = 4,
            y_length = 2,
            x_axis_config={"include_numbers": False},
            axis_config={"include_numbers": True, "color":WHITE},
            background_line_style={
                "stroke_color": GRAY,         # 👈 grid line color
                "stroke_width": 1,
                "stroke_opacity": 0.5,
            },
        )
        plane.center()

        x_values = [1, 2, 3, 4]
        graph = plane.plot_line_graph(x_values,y_values,z_values=None,line_color=ManimColor(color),add_vertex_dots=True,vertex_dot_radius=0.06,vertex_dot_style=None)

        labels = ["No Visits", "Visited Early", "Visited Late", "Many Visits"]
        x_labels = VGroup()

        for x, label in zip(x_values, labels):
            text = Text(label, font_size=22).scale(0.4)
            bg = BackgroundRectangle(text, fill_opacity=1, fill_color=BLACK, buff=0.1)
            group = VGroup(bg, text)
            group.move_to(plane.c2p((x)*1.08, 45))  # Adjust y as needed for label placement
            x_labels.add(group)

        for label in plane.y_axis.numbers:
            label.shift(LEFT*0.5)


        VGroup(plane, graph, x_labels).scale(0.5)
        return plane, graph, x_labels
