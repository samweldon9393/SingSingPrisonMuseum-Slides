from manim import *
import numpy as np

# Define colors
ACCENT_COLOR = "#00d4ff"
WARNING_COLOR = "#ff6b35"
SUCCESS_COLOR = "#4ecdc4"
TEXT_COLOR = WHITE

class ParoleVisualization(Scene):
    def construct(self):
        # Set background color
        self.camera.background_color = "#0f1419"
        
        
        # Title sequence
        self.title_sequence()
        
        # Hook
        self.hook_sequence()
        
        # Racial disparities
        self.racial_disparity_sequence()
        
        # Scale of the problem
        self.scale_sequence()
        
        # The solution
        self.solution_sequence()
        
        # Call to action
        self.call_to_action()

    def title_sequence(self):
        title = Text("Forgiveness - And To Whom Its Given", font_size=60, color=ACCENT_COLOR, weight=BOLD).scale(0.2)
        subtitle = Text("A Closer Look At Parole", font_size=36, color=TEXT_COLOR).scale(0.2)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title), run_time=1.5)
        self.play(Write(subtitle), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(title, subtitle))

    def hook_sequence(self):
        hook_text = Text(
            "What if we could cut\nincarceration in HALF\nwithout increasing crime?",
            font_size=48,
            color=TEXT_COLOR,
            line_spacing=1.2
        ).scale(0.2)
        
        # Emphasize "HALF"
        hook_text[21:25].set_color(WARNING_COLOR)  # "HALF"
        
        self.play(Write(hook_text), run_time=2.5)
        self.wait(1.5)
        self.play(FadeOut(hook_text))

    def racial_disparity_sequence(self):
        title = Text("Racial Disparities", font_size=44, color=ACCENT_COLOR).scale(0.2)
        title.shift(UP*0.8)
        
        # Create bar chart for racial disparities
        axes = Axes(
            x_range=[0, 3, 1],
            y_range=[0, 30, 5],
            x_length=8,
            y_length=4,
            axis_config={"color": WHITE, "stroke_width": 2},
            tips=False
        ).scale(0.2)
        axes.center()

        
        # Data for bars
        white_bar = Rectangle(height=25*4/30, width=1.5, color=WHITE, fill_opacity=0.8).scale(0.2)
        black_bar = Rectangle(height=16.7*4/30, width=1.5, color="#ff6b35", fill_opacity=0.8).scale(0.2)
        hispanic_bar = Rectangle(height=16.7*4/30, width=1.5, color="#ff6b35", fill_opacity=0.8).scale(0.2)
        
        # Position bars
        white_bar.move_to(axes.c2p(0.5, 12.5))
        black_bar.move_to(axes.c2p(1.5, 8.35))
        hispanic_bar.move_to(axes.c2p(2.5, 8.35))
        
        # Labels
        white_label = Text("White\n25%", font_size=24, color=WHITE).scale(0.2)
        black_label = Text("Black\n16.7%", font_size=24, color="#ff6b35").scale(0.2)
        hispanic_label = Text("Hispanic\n16.7%", font_size=24, color="#ff6b35").scale(0.2)
        
        white_label.next_to(white_bar, DOWN*0.3, buff=0.6)
        black_label.next_to(black_bar, DOWN*0.3, buff=0.6)
        hispanic_label.next_to(hispanic_bar, DOWN*0.3, buff=0.6)
        
        
        self.play(Write(title))
        subtitle = self.create_subtitle("Rate of people released at their first parole hearing")
        self.play(Create(axes))
        self.play(
            DrawBorderThenFill(white_bar),
            DrawBorderThenFill(black_bar),
            DrawBorderThenFill(hispanic_bar),
            run_time=2
        )
        self.play(
            Write(white_label),
            Write(black_label),
            Write(hispanic_label),
            run_time=1.5
        )
        self.wait(2)
        self.play(FadeOut(title, axes, white_bar, black_bar, hispanic_bar, 
                          white_label, black_label, hispanic_label, subtitle))

    def scale_sequence(self):
        title = Text("The Scale of the Problem", font_size=44, color=ACCENT_COLOR).scale(0.2)
        title.shift(UP*0.6)
        
        # Create dots representing hearings
        total_text = Text("19,713 Parole Hearings", font_size=36, color=TEXT_COLOR).scale(0.2)
        total_text.next_to(title, DOWN, buff=1)
        
        # Create grid of dots
        dots = VGroup()
        for i in range(20):
            for j in range(20):
                dot = Dot(radius=0.08, color=WHITE, fill_opacity=0.6)
                dot.move_to([i*0.3 - 3, j*0.2 - 2, 0])
                dots.add(dot)
        dots.scale(0.2)
        
        # Highlight released dots (about 20%)
        released_dots = dots[:80]  # Roughly 20% of 400 dots
        
        self.play(Write(title))
        self.play(Write(total_text))
        self.play(Create(dots), run_time=2)
        
        released_text = Text("Only 4,168 Released (21%)", font_size=32, color=WARNING_COLOR).scale(0.2)
        released_text.shift(DOWN*0.6)
        
        self.play(
            released_dots.animate.set_color(SUCCESS_COLOR).set_fill(opacity=1),
            Write(released_text),
            run_time=2
        )
        self.wait(2)
        self.play(FadeOut(released_text))

        possible_dots = dots[80:196]  # Roughly 20% of 400 dots

        possible_text = Text("We could have released another 5491 (49%) without increasing crime", font_size=32, color=WARNING_COLOR).scale(0.2)
        possible_text.shift(DOWN*0.6)
        
        self.play(
            possible_dots.animate.set_color(WARNING_COLOR).set_fill(opacity=1),
            Write(possible_text),
            run_time=2
        )
        self.wait(2)
        self.play(FadeOut(title, total_text, dots, possible_text))

    def crime_reduction_sequence(self):
        title = Text("Crime Could Be DRAMATICALLY Lower", font_size=40, color=ACCENT_COLOR).scale(0.2)
        title.shift(UP*0.6)
        
        # Before/After comparison
        before_title = Text("Current System", font_size=28, color=TEXT_COLOR).scale(0.2)
        after_title = Text("Optimal System", font_size=28, color=SUCCESS_COLOR).scale(0.2)
        
        before_title.shift(LEFT*0.6 + UP*0.3)
        after_title.shift(RIGHT*0.6 + UP*0.3)
        
        # Crime rate bars
        before_bar = Rectangle(height=2, width=1, color=WARNING_COLOR, fill_opacity=0.8).scale(0.2)
        after_bar = Rectangle(height=0.6, width=1, color=SUCCESS_COLOR, fill_opacity=0.8).scale(0.2)
        
        before_bar.shift(LEFT*0.6)
        after_bar.shift(RIGHT*0.6 + DOWN*0.14)
        
        before_label = Text("33% Re-arrest", font_size=24, color=WARNING_COLOR).scale(0.2)
        after_label = Text("10% Re-arrest", font_size=24, color=SUCCESS_COLOR).scale(0.2)
        
        before_label.next_to(before_bar, DOWN, buff=0.06)
        after_label.next_to(after_bar, DOWN, buff=0.06)
        
        # Violent crime comparison
        v_before_bar = Rectangle(height=0.8, width=1, color=WARNING_COLOR, fill_opacity=0.8).scale(0.2)
        v_after_bar = Rectangle(height=0.27, width=1, color=SUCCESS_COLOR, fill_opacity=0.8).scale(0.2)
        
        v_before_bar.shift(LEFT*0.6 + DOWN*0.4)
        v_after_bar.shift(RIGHT*0.6 + DOWN*0.45)
        
        v_before_label = Text("6% Violent", font_size=20, color=WARNING_COLOR).scale(0.2)
        v_after_label = Text("2% Violent", font_size=20, color=SUCCESS_COLOR).scale(0.2)
        
        v_before_label.next_to(v_before_bar, DOWN, buff=0.04)
        v_after_label.next_to(v_after_bar, DOWN, buff=0.04)
        
        self.play(Write(title))
        self.play(
            Write(before_title),
            Write(after_title)
        )
        self.play(
            DrawBorderThenFill(before_bar),
            DrawBorderThenFill(v_before_bar),
            Write(before_label),
            Write(v_before_label)
        )
        self.wait(1)
        self.play(
            DrawBorderThenFill(after_bar),
            DrawBorderThenFill(v_after_bar),
            Write(after_label),
            Write(v_after_label)
        )
        
        improvement = Text("70% REDUCTION in crime", font_size=32, color=SUCCESS_COLOR, weight=BOLD).scale(0.2)
        improvement.shift(DOWN*0.6)
        self.play(Write(improvement))
        
        self.wait(2.5)
        self.play(FadeOut(title, before_title, after_title, before_bar, after_bar,
                          v_before_bar, v_after_bar, before_label, after_label,
                          v_before_label, v_after_label, improvement))

    def solution_sequence(self):
        title = Text("The Solution: Evidence-Based Decisions", font_size=40, color=ACCENT_COLOR).scale(0.2)
        title.shift(UP*0.6)
        
        # Key metrics
        metric1 = Text("✓ Double release rates", font_size=32, color=SUCCESS_COLOR)
        metric2 = Text("✓ Eliminate racial disparities", font_size=32, color=SUCCESS_COLOR)
        metric3 = Text("✓ Reduce crime by 70%", font_size=32, color=SUCCESS_COLOR)
        metric4 = Text("✓ Same or better public safety", font_size=32, color=SUCCESS_COLOR)
        
        metrics = VGroup(metric1, metric2, metric3, metric4).scale(0.2)
        metrics.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        metrics.center()
        
        self.play(Write(title))
        for metric in metrics:
            self.play(Write(metric), run_time=0.8)
        
        self.wait(2)
        self.play(FadeOut(title, metrics))

    def call_to_action(self):
        main_text = Text(
            "Data-driven justice\nis possible.",
            font_size=48,
            color=ACCENT_COLOR,
            line_spacing=1.2,
            weight=BOLD
        ).scale(0.2)
        
        source = Text(
            "Source: Journal of Quantitative Criminology (2024)\nLaqueur & Copus - NY State Parole Analysis",
            font_size=20,
            color=TEXT_COLOR,
            line_spacing=1.1
        ).scale(0.2)
        source.shift(DOWN*0.6)
        
        self.play(Write(main_text), run_time=2)
        self.play(Write(source), run_time=1.5)
        self.wait(3)

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
            font_size=46,
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

    def citation(self, text1, text2):
        # Study citation with better formatting
        citation = VGroup(
            Text(text1,
                 font="Arial", font_size=24, color=BLUE_A, weight=BOLD),
            Text(text2,
                 font="Arial", font_size=20, color=GRAY_A)
        ).arrange(DOWN, buff=0.3).move_to(ORIGIN)

        # Citation background
        citation_bg = RoundedRectangle(
            width=citation.width + 1,
            height=citation.height + 0.5,
            corner_radius=0.2,
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
# To render: manim -pqh parole_viz.py ParoleVisualization
