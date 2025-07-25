from manim import *
import math

# Configure rendering settings
config.pixel_height = 1080 
config.pixel_width = 1920
config.frame_rate = 30

class PieChart(VGroup):
    def __init__(self, data, colors=None, radius=2.0, label_scale=0.5, **kwargs):
        super().__init__(**kwargs)
        total = sum(data.values())
        angle_start = 0
        self.slices = []
        self.labels = []

        if colors is None:
            colors = [BLUE_D, GREEN_D, RED_D, YELLOW_D, PURPLE_D]

        for i, (label, value) in enumerate(data.items()):
            angle_span = (value / total) * TAU
            wedge = AnnularSector(
                inner_radius=0,
                outer_radius=radius,
                angle=angle_span,
                start_angle=angle_start,
                color=colors[i % len(colors)],
                stroke_width=.5,
                stroke_color=WHITE,
            )
            wedge.set_fill(color=colors[i % len(colors)], opacity=0.8)
            self.slices.append(wedge)
            self.add(wedge)

            # Add label with percentage
            mid_angle = angle_start + angle_span / 2
            label_pos = radius * 0.7 * np.array([math.cos(mid_angle), math.sin(mid_angle), 0])
            
            percentage = f"{value}%"
            label_text = VGroup(
                Text(label, font="Arial", weight=BOLD).scale(label_scale),
                Text(percentage, font="Arial").scale(label_scale * 0.6)
            ).arrange(DOWN, buff=0.05)
            
            label_text.move_to(label_pos)
            self.labels.append(label_text)
            self.add(label_text)

            angle_start += angle_span

class PrisonDataVisualization(Scene):
    def construct(self):
        # Main title sequence
        self.show_main_title()
        
        # Visit data visualization
        self.show_visit_data()
        
        # Misconduct data visualization
        self.show_misconduct_data()
        
        # Connection analysis
        self.show_connection_analysis()
        
        # Final conclusion
        self.show_conclusion()

    def show_main_title(self):
        """Display the main title with professional styling"""
        title = Text(
            "The Impact of Prison Visits on Inmate Behavior",
            font="Arial",
            weight=BOLD,
            font_size=36,
            gradient=(BLUE_A, BLUE_D)
        )
        
        subtitle = Text(
            "A Data-Driven Analysis",
            font="Arial",
            font_size=24,
            color=GRAY_B
        ).shift(DOWN * 0.6)
        
        title_group = VGroup(title, subtitle)
        
        # Background rectangle
        bg = BackgroundRectangle(
            title_group,
            fill_opacity=0.1,
            fill_color=BLUE_D,
            buff=0.4,
            corner_radius=0.2
        )
        
        full_title = VGroup(bg, title_group)
        full_title.move_to(ORIGIN)
        full_title.scale(0.3)
        
        self.play(FadeIn(full_title, shift=UP), run_time=2)
        self.wait(3)
        self.play(FadeOut(full_title, shift=UP), run_time=1.5)

    def show_visit_data(self):
        """Display visit frequency data with pie chart"""
        self.create_section_title("Prison Visit Frequency")
        
        visit_data = {
            "None": 75,
            "Some": 20,
            "Many": 5
        }
        
        colors = [RED_D, YELLOW_D, GREEN_D]
        pie_chart = PieChart(visit_data, colors=colors, radius=1.5)
        pie_chart.shift(LEFT * .5)
        pie_chart.scale(0.3)
        
        # Key finding text
        finding = VGroup(
            Text("Key Finding:", font="Arial", weight=BOLD, font_size=24, color=RED_D),
            Text("75% of inmates", font="Arial", weight=BOLD, font_size=20),
            Text("receive no visits", font="Arial", font_size=18, color=GRAY_B)
        ).arrange(DOWN, buff=0.2).shift(RIGHT * .5)
        finding.scale(0.3)
        
        # Animate pie chart creation
        self.animate_pie_chart(pie_chart)
        self.wait(1)
        
        # Show key finding
        self.play(FadeIn(finding, shift=RIGHT), run_time=2)
        self.wait(3)
        
        # Clear screen
        self.play(FadeOut(VGroup(pie_chart, finding)), run_time=1.5)

    def show_misconduct_data(self):
        """Display misconduct data with pie chart"""
        self.create_section_title("Inmate Misconduct Incidents")
        
        misconduct_data = {
            "None": 69,
            "Some": 26,
            "Many": 5
        }
        
        colors = [GREEN_D, YELLOW_D, RED_D]
        pie_chart = PieChart(misconduct_data, colors=colors, radius=1.5)
        pie_chart.shift(LEFT * .5)
        pie_chart.scale(0.3)
        
        # Key finding text
        finding = VGroup(
            Text("Key Finding:", font="Arial", weight=BOLD, font_size=24, color=GREEN_D),
            Text("69% of inmates", font="Arial", weight=BOLD, font_size=20),
            Text("had no infractions", font="Arial", font_size=18, color=GRAY_B)
        ).arrange(DOWN, buff=0.2).shift(RIGHT * .5)
        finding.scale(0.3)
        
        # Animate pie chart creation
        self.animate_pie_chart(pie_chart)
        self.wait(1)
        
        # Show key finding
        self.play(FadeIn(finding, shift=RIGHT), run_time=2)
        self.wait(3)
        
        # Clear screen
        self.play(FadeOut(VGroup(pie_chart, finding)), run_time=1.5)

    def show_connection_analysis(self):
        """Show the correlation between visits and misconduct"""
        self.create_section_title("The Connection: Visits vs. Misconduct")
        
        # Study citation
        citation = VGroup(
            Text("Study: Joshua Cochran, FSU College of Criminology (2012)", 
                 font="Arial", font_size=16, color=GRAY_B),
            Text("One-year analysis comparing visit frequency with misconduct citations", 
                 font="Arial", font_size=14, color=GRAY_C)
        ).arrange(DOWN, buff=0.1).move_to(ORIGIN)
        citation.scale(0.3)
        
        self.play(FadeIn(citation), run_time=2)
        self.wait(3)
        self.play(FadeOut(citation), run_time=1)
        
        # Create dual line graph
        self.create_dual_line_graph()

    def create_dual_line_graph(self):
        self.title_sequence("Is there a connection between visits and misconduct?")

        self.wait(1)
        y_values = [66.8, 70.7, 78.0, 77.3]
        plane, graph, x_labels = self.line_graph(y_values, [60, 110, 10], '#0f19f5')
        self.add(plane)
        self.add(x_labels)
        self.wait(1)

        graph_text = Text("The X-axis ", font_size=13, font="Arial")
        bg = BackgroundRectangle(graph_text, fill_opacity=0.5, fill_color=BLACK, buff=0.1)
        graph_text = Text("This line represents inmates with no misconduct", font_size=13, font="Arial")
        bg = BackgroundRectangle(graph_text, fill_opacity=0.5, fill_color=BLACK, buff=0.1)
        group = VGroup(bg, graph_text)
        group.set_z_index(1000)
        self.play(Write(group))
        self.wait(1)
        group.set_opacity(0.5)
        self.play(Create(graph), run_time=6)
        self.play(FadeOut(group))
        self.play(FadeOut(graph))


        graph_text = Text("This line represents inmates with heavy misconduct", font_size=13, font="Arial")
        bg = BackgroundRectangle(graph_text, fill_opacity=0.5, fill_color=BLACK, buff=0.1)
        group = VGroup(bg, graph_text)
        group.set_z_index(1000)
        self.play(Write(group))
        group.shift(DOWN*.1)
        self.wait(1)
        group.set_opacity(0.5)
        y_values = [5.6, 8.1, 0.7, 0]
        new_plane, graph, x_labels = self.line_graph(y_values, [-10, 20, 5], '#f50f0f')
        VGroup(new_plane, graph, x_labels).shift(DOWN*.15)
        self.play(ReplacementTransform(plane, new_plane))
        self.wait(1)
        self.play(Create(graph), run_time=6)
        self.play(FadeOut(group))
        '''
        """Create a professional dual-line graph"""
        # Create axes
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 80, 20],
            x_length=6,
            y_length=4,
            axis_config={
                "color": WHITE,
                "stroke_width": 2,
                "include_numbers": True,
                "font_size": 18
            },
            x_axis_config={"include_numbers": False},
            tips=False
        ).move_to(ORIGIN)
        axes.scale(0.3)
        
        # Data points
        x_values = [1, 2, 3, 4]
        no_misconduct_y = [66.8, 70.7, 78.0, 77.3]
        heavy_misconduct_y = [5.6, 8.1, 0.7, 0]
        
        # Create graphs
        no_misconduct_graph = axes.plot_line_graph(
            x_values, no_misconduct_y,
            line_color=GREEN_C,
            add_vertex_dots=True,
            vertex_dot_radius=0.06,
            stroke_width=3
        )
        no_misconduct_graph.scale(0.3)
        
        heavy_misconduct_graph = axes.plot_line_graph(
            x_values, heavy_misconduct_y,
            line_color=RED_C,
            add_vertex_dots=True,
            vertex_dot_radius=0.06,
            stroke_width=3
        )
        heavy_misconduct_graph.scale(0.3)
        
        # X-axis labels
        x_labels = ["No Visits", "Few Visits", "Some Visits", "Many Visits"]
        x_label_group = VGroup()
        
        for i, label in enumerate(x_labels):
            text = Text(label, font="Arial", font_size=14)
            text.next_to(axes.c2p(i + 1, 0), DOWN, buff=0.3)
            x_label_group.add(text)
        x_label_group.scale(0.3)
        
        # Y-axis title
        y_title = Text("Percentage of Inmates", font="Arial", font_size=16, color=WHITE)
        y_title.rotate(90 * DEGREES)
        y_title.next_to(axes.y_axis, LEFT, buff=0.3)
        y_title.scale(0.3)
        
        # Legend
        legend = VGroup(
            VGroup(
                Line(ORIGIN, RIGHT * 0.4, color=GREEN_C, stroke_width=4),
                Text("No Misconduct", font="Arial", font_size=14, color=GREEN_C)
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Line(ORIGIN, RIGHT * 0.4, color=RED_C, stroke_width=4),
                Text("Heavy Misconduct", font="Arial", font_size=14, color=RED_C)
            ).arrange(RIGHT, buff=0.2)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        
        legend.to_corner(UR, buff=0.3)
        
        # Background
        bg = BackgroundRectangle(
            legend,
            fill_opacity=0.8,
            fill_color=BLACK,
            buff=0.15,
            corner_radius=0.1
        )
        legend_group = VGroup(bg, legend)
        legend_group.scale(0.3)
        
        # Animate the graph
        self.play(Create(axes), run_time=2)
        self.play(Write(x_label_group), Write(y_title), run_time=1.5)
        self.play(FadeIn(legend_group), run_time=1)
        
        # Animate first line
        self.play(Create(no_misconduct_graph), run_time=3)
        self.wait(2)
        
        # Animate second line
        self.play(Create(heavy_misconduct_graph), run_time=3)
        self.wait(3)
        
        # Clear for conclusion
        self.play(FadeOut(VGroup(axes, no_misconduct_graph, heavy_misconduct_graph, 
                                x_label_group, y_title, legend_group)), run_time=2)
        '''

    def line_graph(self, y_values, y_range, color):
        plane = Axes(
            x_range=[0, 5, 1],
            y_range=y_range,
            x_length=4,
            y_length=2,
            axis_config={
                "color": WHITE,
                "stroke_width": 1,
                "include_numbers": True,
                "font_size": 18
            },
            x_axis_config={"include_numbers": False},
            tips=False
        ).move_to(ORIGIN)
        plane.center()

        x_values = [1, 2, 3, 4]
        graph = plane.plot_line_graph(x_values,y_values,z_values=None,line_color=ManimColor(color),add_vertex_dots=True,vertex_dot_radius=0.06,vertex_dot_style=None)

        labels = ["No Visits", "Some Visits", "Some Visits", "Many Visits"]
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

    def show_conclusion(self):
        """Display the main conclusion"""
        conclusion_title = Text(
            "Conclusion",
            font="Arial",
            weight=BOLD,
            font_size=32,
            color=BLUE_D
        )
        
        conclusion_points = VGroup(
            Text("• More visits correlate with less misconduct", 
                 font="Arial", font_size=22, color=GREEN_D),
            Text("• Family connections improve inmate behavior", 
                 font="Arial", font_size=22, color=GREEN_D),
            Text("• Prison visitation programs show measurable impact", 
                 font="Arial", font_size=22, color=GREEN_D)
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        
        conclusion_group = VGroup(conclusion_title, conclusion_points)
        conclusion_group.arrange(DOWN, buff=0.8)
        conclusion_group.move_to(ORIGIN)
        conclusion_group.scale(0.3)
        
        self.play(FadeIn(conclusion_title, shift=UP), run_time=2)
        self.wait(1)
        
        for point in conclusion_points:
            self.play(FadeIn(point, shift=RIGHT), run_time=1.5)
            self.wait(1)
        
        self.wait(3)

    def create_section_title(self, text):
        """Create and animate a section title"""
        title = Text(
            text,
            font="Arial",
            weight=BOLD,
            font_size=24,
            color=BLUE_D
        )
        
        underline = Line(
            LEFT * title.width / 2,
            RIGHT * title.width / 2,
            color=BLUE_D,
            stroke_width=2
        ).next_to(title, DOWN, buff=0.05)
        
        title_group = VGroup(title, underline)
        title_group.to_edge(UP, buff=0.3)
        title_group.scale(0.3)
        
        self.play(Write(title), Create(underline), run_time=1.5)
        self.wait(0.5)
        
        # Move to corner
        title_group.generate_target()
        title_group.target.scale(0.7).to_corner(UL, buff=0.2)
        self.play(MoveToTarget(title_group), run_time=1)
        
        return title_group

    def animate_pie_chart(self, pie_chart):
        """Animate pie chart creation with professional timing"""
        # Create slices one by one
        for i, (wedge, label) in enumerate(zip(pie_chart.slices, pie_chart.labels)):
            if i == 0:
                # First slice appears immediately
                self.play(
                    Create(wedge),
                    FadeIn(label, shift=wedge.get_center() * 0.3),
                    run_time=1.5
                )
            else:
                # Subsequent slices with smooth rotation
                self.play(
                    Create(wedge),
                    FadeIn(label, shift=wedge.get_center() * 0.3),
                    run_time=1.2
                )
            self.wait(0.5)
        
        # Slight rotation for visual appeal
        self.play(Rotate(pie_chart, 5 * DEGREES), run_time=1)
        self.play(Rotate(pie_chart, -5 * DEGREES), run_time=1)

    def title_sequence(self, text, size=13):
        # Initial large title
        t = Text(text, font_size=size, font="Arial")
        bg = BackgroundRectangle(t, fill_opacity=.5, fill_color=BLACK, buff=0.1)
        title = VGroup(bg, t)

        # Step 1: Animate it onto the center
        self.play(FadeIn(title))
        self.wait(2.5)  # Pause to linger

        # Step 2: Shrink and move to top
        title_target = title.copy().scale(0.5).shift(UP)

        self.play(Transform(title, title_target))
        self.wait(0.5)

    def explanation_text(self):
        text1 = Text("A 2012 study by Joshua Cochran of FSU College of Criminology", font_size=8, font="Arail")
        text2 = Text("compared the frequency an inmate was visited over a one year", font_size=8, font="Arail")
        text3 = Text("period with the number of misconduct citations they received.", font_size=8, font="Arial")
        text4 = Text("By grouping together inmates with similar visit and infraction", font_size=8, font="Arial")
        text5 = Text("patterns, the study revealed that inmates who received more", font_size=8, font="Arial")
        text6 = Text("visits committed less misconduct.", font_size=8, font="Arial")
        group = VGroup(text1.shift(UP*.45), text2.shift(UP*.3), text3.shift(UP*.15), text4, text5.shift(DOWN*.15), text6.shift(DOWN*.3))
        return group
