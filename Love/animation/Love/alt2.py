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
                stroke_width=0.5,
                stroke_color=WHITE,
            )
            wedge.set_fill(color=colors[i % len(colors)], opacity=0.9)
            self.slices.append(wedge)
            self.add(wedge)

            # Add label with percentage
            mid_angle = angle_start + angle_span / 2
            label_pos = radius * 0.75 * np.array([math.cos(mid_angle), math.sin(mid_angle), 0])

            percentage = f"{value}%"
            label_text = VGroup(
                Text(label, font="Arial", font_size=48, weight=BOLD, color=WHITE).scale(label_scale),
                Text(percentage, font="Arial", font_size=58, color=WHITE).scale(label_scale * 0.5)
            ).arrange(DOWN, buff=0.05)

            label_text.move_to(label_pos)
            self.labels.append(label_text)
            self.add(label_text)

            angle_start += angle_span

class PrisonDataVisualization(Scene):
    def construct(self):
        # Set background color for professional look
        self.camera.background_color = "#1a1a1a"
        
        # Main title sequence
        self.show_main_title()
        self.citation()

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
            "Love Doesn't Stop at the Gates",
            font="Arial",
            weight=BOLD,
            font_size=48,
            gradient=(BLUE_A, BLUE_D)
        )

        subtitle = Text(
            "How visit frequency impacts incarcerated people's lives",
            font="Arial",
            font_size=28,
            color=GRAY_A
        ).shift(DOWN * 0.8)

        title_group = VGroup(title, subtitle)

        # Professional background with subtle animation
        bg = RoundedRectangle(
            width=title_group.width + 1.5,
            height=title_group.height + 1.0,
            corner_radius=0.0,
            fill_opacity=0.15,
            fill_color=BLUE_D,
            stroke_color=BLUE_C,
            stroke_width=2
        )

        full_title = VGroup(bg, title_group)
        full_title.move_to(ORIGIN).scale(0.2)

        # Smooth entrance animation
        self.play(
            DrawBorderThenFill(bg),
            FadeIn(title, shift=UP * 0.5),
            run_time=2
        )
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=1.5)
        self.wait(3)
        self.play(FadeOut(full_title, shift=UP * 0.5), run_time=1.5)

    def show_visit_data(self):
        """Display visit frequency data with pie chart"""
        section_title = self.create_section_title("Prison Visit Frequency")

        visit_data = {
            "None": 75,
            "Some": 20,
            "Many": 5
        }

        colors = [RED_C, YELLOW_C, GREEN_C]
        pie_chart = PieChart(visit_data, colors=colors, radius=2.5)
        pie_chart.shift(LEFT*0.75).scale(0.2)

        # Enhanced key finding with better positioning
        finding = VGroup(
            Text("Key Finding:", font="Arial", weight=BOLD, font_size=32, color=RED_C),
            Text("75% of incarcerated men", font="Arial", weight=BOLD, font_size=28, color=WHITE),
            Text("received no visits", font="Arial", font_size=24, color=GRAY_A)
        ).arrange(DOWN, buff=0.3).shift(RIGHT*0.75).scale(0.2)

        # Animate pie chart creation
        self.animate_pie_chart(pie_chart)
        self.wait(1)

        # Show key finding with staggered animation
        for item in finding:
            self.play(FadeIn(item), run_time=1)
            self.wait(0.5)

        self.wait(3)
        self.play(FadeOut(VGroup(pie_chart, finding, section_title)), run_time=1.5)

    def show_misconduct_data(self):
        """Display misconduct data with pie chart"""
        section_title = self.create_section_title("Misconduct Incidents")

        misconduct_data = {
            "None": 69,
            "Some": 26,
            "Many": 5
        }

        colors = [GREEN_C, YELLOW_C, RED_C]
        pie_chart = PieChart(misconduct_data, colors=colors, radius=2.5)
        pie_chart.shift(LEFT*0.75).scale(0.2)

        # Enhanced key finding
        finding = VGroup(
            Text("Key Finding:", font="Arial", weight=BOLD, font_size=32, color=GREEN_C),
            Text("69% of incarcerated men", font="Arial", weight=BOLD, font_size=28, color=WHITE),
            Text("had no infractions", font="Arial", font_size=24, color=GRAY_A)
        ).arrange(DOWN, buff=0.3).shift(RIGHT*0.75).scale(0.2)

        # Animate pie chart creation
        self.animate_pie_chart(pie_chart)
        self.wait(1)

        # Show key finding with staggered animation
        for item in finding:
            self.play(FadeIn(item), run_time=1)
            self.wait(0.5)

        self.wait(3)
        self.play(FadeOut(VGroup(pie_chart, finding, section_title)), run_time=1.5)

    def citation(self):
        # Study citation with better formatting
        citation = VGroup(
            Text("Study: Joshua Cochran, FSU College of Criminology (2012)",
                 font="Arial", font_size=24, color=BLUE_A, weight=BOLD),
            Text("One-year analysis comparing visit frequency with misconduct citations",
                 font="Arial", font_size=20, color=GRAY_A)
        ).arrange(DOWN, buff=0.3).move_to(ORIGIN)

        # Citation background
        citation_bg = RoundedRectangle(
            width=citation.width + 1,
            height=citation.height + 0.5,
            corner_radius=0.0,
            fill_opacity=0.1,
            fill_color=BLUE_D,
            stroke_color=BLUE_C,
            stroke_width=1
        )

        citation_group = VGroup(citation_bg, citation).scale(0.2)

        self.play(DrawBorderThenFill(citation_bg), run_time=1)
        self.play(FadeIn(citation), run_time=2)
        self.wait(3)
        self.play(FadeOut(VGroup(citation_group)), run_time=1.5)

    def show_connection_analysis(self):
        """Show the correlation between visits and misconduct"""
        section_title = self.create_section_title("The Connection: Visits vs. Misconduct")


        # Create dual line graph
        self.create_dual_line_graph()

    def create_dual_line_graph(self):
        """Create professional dual-line graph with proper animations"""
        title = self.title_sequence("Is there a connection between visits and misconduct?")
        self.play(FadeOut(title))
        self.wait(1)

        # First graph - No misconduct
        y_values_no_misconduct = [66.8, 70.7, 78.0, 77.3]
        plane, graph1, x_labels = self.line_graph(
            y_values_no_misconduct, [60, 85, 5], GREEN_C
        )
        
        self.add(plane)
        x_labels.next_to(plane.x_axis, DOWN, buff=0.1).shift(UP*0.1)
        self.add(x_labels)
        self.wait(1)

        # No misconduct subtitle 
        sub1 = self.create_subtitle("This line represents visit frequency for incarcerated men with no misconduct")

        # Animate first line
        self.play(Create(graph1), run_time=4)
        self.wait(2)

        ex1 = self.title_sequence("Men who received less citations received more visits")
        self.play(FadeOut(ex1))


        # Second graph - Heavy misconduct
        y_values_heavy_misconduct = [5.6, 8.1, 0.7, 0]
        new_plane, graph2, x_labels2 = self.line_graph(
            y_values_heavy_misconduct, [-10, 20, 5], '#f50f0f'
        )
        VGroup(new_plane, graph2, x_labels2).shift(DOWN*.15)
        self.wait(1)
        graph2.move_to(graph1)
        self.play(FadeOut(graph1), FadeOut(sub1))
        new_plane.move_to(plane)
        self.play(ReplacementTransform(plane, new_plane))


        # No misconduct subtitle 
        sub2 = self.create_subtitle("This line represents visit frequency for incarcerated men with heavy misconduct")

        # Add explanation for second line
        explanation = Text("Inmates with heavy misconduct", font_size=20, font="Arial", color=RED_C)
        explanation_bg = BackgroundRectangle(explanation, fill_opacity=0.8, fill_color=BLACK, buff=0.2)
        explanation_group = VGroup(explanation_bg, explanation).move_to(UP * 2).scale(0.2)
        
        self.play(FadeIn(explanation_group), run_time=1)
        self.wait(1)
        self.play(explanation_group.animate.set_opacity(0.6))
        
        self.play(Create(graph2), run_time=4)
        ex2 = self.title_sequence("Men who received more citations received less visits")
        self.play(FadeOut(ex2))

        self.play(FadeOut(explanation_group), run_time=1)
        
        self.wait(3)
        self.play(FadeOut(VGroup(plane, new_plane, graph2, x_labels, sub2)), run_time=2)

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
            text = Text(label, color=WHITE, font='Arial', font_size=22).scale(0.4)
            text.move_to(plane.c2p((x)*1.08, 45))  # Adjust y as needed for label placement
            x_labels.add(text)

        for label in plane.y_axis.numbers:
            label.shift(LEFT*0.5)


        VGroup(plane, graph, x_labels).scale(0.5)
        return plane, graph, x_labels

    def create_line_graph(self, y_values, y_range, color, description):
        """Create a professional line graph"""
        plane = Axes(
            x_range=[0, 5, 1],
            y_range=y_range,
            x_length=8,
            y_length=4,
            axis_config={
                "color": GRAY_A,
                "stroke_width": 2,
                "include_numbers": True,
                "font_size": 20
            },
            x_axis_config={"include_numbers": False},
            tips=False
        ).move_to(ORIGIN)

        x_values = [1, 2, 3, 4]
        graph = plane.plot_line_graph(
            x_values, y_values,
            line_color=color,
            add_vertex_dots=True,
            vertex_dot_radius=0.08,
            stroke_width=4
        )

        # Enhanced x-axis labels
        labels = ["No Visits", "Few Visits", "Some Visits", "Many Visits"]
        x_labels = VGroup()

        for x, label in zip(x_values, labels):
            text = Text(label, font_size=18, font="Arial", color=WHITE)
            text_bg = RoundedRectangle(
                width=text.width + 0.3,
                height=text.height + 0.2,
                corner_radius=0.1,
                fill_opacity=0.8,
                fill_color=BLACK,
                stroke_color=GRAY_C,
                stroke_width=1
            )
            group = VGroup(text_bg, text)
            group.move_to(plane.c2p(x, y_range[0] - (y_range[1] - y_range[0]) * 0.1))
            x_labels.add(group)

        # Y-axis label
        y_label = Text("Percentage of inmates", font="Arial", font_size=18, color=GRAY_A)
        y_label.rotate(90 * DEGREES)
        y_label.next_to(plane.y_axis, LEFT, buff=0.5)

        return plane, graph, VGroup(x_labels, y_label)

    def create_second_line_graph(self, plane, y_values, color):
        """Create second line graph on existing axes"""
        # Scale y_values to fit the existing y_range of the plane
        scaled_y_values = [val * 10 + 60 for val in y_values]  # Scale to match first graph range
        
        x_values = [1, 2, 3, 4]
        graph = plane.plot_line_graph(
            x_values, scaled_y_values,
            line_color=color,
            add_vertex_dots=True,
            vertex_dot_radius=0.08,
            stroke_width=4
        )
        return graph

    def show_conclusion(self):
        """Display the main conclusion with enhanced styling"""
        conclusion_title = Text(
            "Conclusion",
            font="Arial",
            weight=BOLD,
            font_size=48,
            color=BLUE_C,
            gradient=(BLUE_A, BLUE_D)
        )

        conclusion_points = VGroup(
            Text("• More visits correlate with better outcomes",
                 font="Arial", font_size=28, color=GREEN_C, weight=MEDIUM),
            Text("• Connection to the outside world matters",
                 font="Arial", font_size=28, color=GREEN_C, weight=MEDIUM),
            Text("• Family and friend support makes a measurable difference",
                 font="Arial", font_size=28, color=GREEN_C, weight=MEDIUM)
        ).arrange(DOWN, buff=0.6, aligned_edge=LEFT)

        # Background for conclusion
        conclusion_bg = RoundedRectangle(
            width=conclusion_points.width + 2,
            height=conclusion_points.height + 1,
            corner_radius=0.0,
            fill_opacity=0.1,
            fill_color=GREEN_D,
            stroke_color=GREEN_C,
            stroke_width=2
        )

        conclusion_group = VGroup(conclusion_title, conclusion_points)
        conclusion_group.arrange(DOWN, buff=1.2)
        conclusion_group.move_to(ORIGIN)

        conclusion_bg.move_to(conclusion_points.get_center())
        full_conclusion = VGroup(conclusion_bg, conclusion_group).scale(0.2)

        self.play(FadeIn(conclusion_title, shift=UP * 0.5), run_time=2)
        self.wait(1)
        self.play(DrawBorderThenFill(conclusion_bg), run_time=1.5)

        for point in conclusion_points:
            self.play(FadeIn(point, shift=RIGHT * 0.5), run_time=1.5)
            self.wait(1)

        self.wait(4)

    def create_section_title(self, text):
        """Create and animate a professional section title"""
        title = Text(
            text,
            font="Arial",
            weight=BOLD,
            font_size=46,
            color=BLUE_C,
            gradient=(BLUE_A, BLUE_D)
        ).scale(0.2)

        # Enhanced underline with gradient effect
        underline = Line(
            LEFT * title.width / 2,
            RIGHT * title.width / 2,
            color=BLUE_C,
            stroke_width=2
        ).next_to(title, DOWN, buff=0.1)

        title_group = VGroup(title, underline)

        self.play(
            FadeIn(title, run_time=1.5),
            Create(underline, run_time=1),
        )
        self.wait(0.5)

        # Smooth transition to corner
        title_group.generate_target()
        title_group.target.scale(0.4).shift(UP*0.8)
        self.play(MoveToTarget(title_group), run_time=1.2)

        return title_group

    def create_subtitle(self, text):
        """Create and animate a professional section title"""
        title = Text(
            text,
            font="Arial",
            weight=BOLD,
            font_size=36,
            color=BLUE_C,
            gradient=(BLUE_A, BLUE_D)
        ).scale(0.2)

        self.play(
            FadeIn(title, run_time=1.5),
        )
        self.wait(0.5)

        # Smooth transition to corner
        title.generate_target()
        title.target.scale(0.4).shift(DOWN)
        self.play(MoveToTarget(title), run_time=1.2)

        return title

    def animate_pie_chart(self, pie_chart):
        """Animate pie chart creation with professional timing and effects"""
        # Initial rotation for dynamic entrance
        pie_chart.rotate(-PI/4)
        
        # Create slices with smooth animations
        for i, (wedge, label) in enumerate(zip(pie_chart.slices, pie_chart.labels)):
            # Wedge appears with a draw effect
            self.play(
                DrawBorderThenFill(wedge),
                run_time=1.2
            )
            
            # Label fades in with slight delay and movement
            self.play(
                FadeIn(label, shift=wedge.get_center() * 0.2),
                run_time=0.8
            )
            
            if i < len(pie_chart.slices) - 1:
                self.wait(0.3)

        # Final subtle rotation for visual appeal
        self.play(Rotate(pie_chart, PI/4), run_time=1.5)
        self.wait(0.5)

    def title_sequence(self, text, size=24):
        """Create professional title sequence"""
        title_text = Text(text, font_size=size, font="Arial", color=WHITE, weight=BOLD)
        
        # Enhanced background
        bg = RoundedRectangle(
            width=title_text.width + 1,
            height=title_text.height + 0.5,
            corner_radius=0.0,
            fill_opacity=0.8,
            fill_color=BLACK,
            stroke_color=BLUE_C,
            stroke_width=2
        )
        
        title = VGroup(bg, title_text).scale(0.2)

        # Smooth entrance
        self.play(DrawBorderThenFill(bg), FadeIn(title_text), run_time=1.5)
        self.wait(2.5)


        return title
