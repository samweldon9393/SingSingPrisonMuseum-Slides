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
        
        
        '''
        '''
        # Title sequence
        self.title_sequence()
        
        # Hook
        self.hook_sequence()
        
        # Racial disparities
        self.racial_disparity_sequence()

        # Call to action
        self.call_to_action()

        # Citation 
        self.do_citation()

        # Scale of the problem
        self.scale_sequence()
        
        # 10,000 years
        self.prison_days_sequence()
        
        # The solution
        self.show_conclusion()

    def title_sequence(self):
        title = Text("Forgiveness & Who Gets It", font_size=60, color=ACCENT_COLOR, weight=BOLD).scale(0.2)
        subtitle = Text("A Closer Look At Prison and Parole", font_size=36, color=TEXT_COLOR).scale(0.2)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        self.play(FadeIn(title), run_time=1.5)
        self.play(FadeIn(subtitle), run_time=1.5)
        self.wait(3)
        self.play(FadeOut(title, subtitle))

    def do_citation(self):
        t1 = "Study: An Algorithmic Assessment of Parole Decisions"
        t2 = "by  Hannah S. Laqueur & Ryan W. Copus"
        self.citation(t1, t2)

    def hook_sequence(self):
        hook_text = Text(
            "According to NYU\nBased on figures from 2023\nRace plays a large role in parole decisions",
            font_size=48,
            color=TEXT_COLOR,
            line_spacing=1.2
        ).scale(0.2)
        
        # Emphasize "HALF"
        hook_text[21:25].set_color(WARNING_COLOR)  # "HALF"
        
        self.play(FadeIn(hook_text), run_time=2.5)
        self.wait(3)
        self.play(FadeOut(hook_text))

    def racial_disparity_sequence(self):
        title = Text("Chance of being granted parole", font_size=44, color=ACCENT_COLOR).scale(0.2)
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
        white_bar = Rectangle(height=45*4/30, width=1.5, color=WHITE, fill_opacity=0.8).scale(0.2)
        black_bar = Rectangle(height=32*4/30, width=1.5, color="#ff6b35", fill_opacity=0.8).scale(0.2)
        
        # Position bars
        white_bar.move_to(axes.c2p(1, 14.5))
        black_bar.move_to(axes.c2p(2, 8.35))
        
        # Labels
        white_label = Text("White People\n45%", font_size=24, color=WHITE).scale(0.2)
        black_label = Text("People of Color\n32%", font_size=24, color="#ff6b35").scale(0.2)
        
        white_label.next_to(white_bar, DOWN*0.3, buff=0.6)
        black_label.next_to(black_bar, DOWN*0.3, buff=0.6)
        
        
        self.play(FadeIn(title))
        subtitle = self.create_subtitle("Racial Disparities")
        self.play(
            DrawBorderThenFill(white_bar),
            DrawBorderThenFill(black_bar),
            run_time=2
        )
        self.play(
            FadeIn(white_label),
            FadeIn(black_label),
            run_time=1.5
        )
        self.wait(2)
        self.play(FadeOut(title, white_bar, black_bar, 
                          white_label, black_label, subtitle))

    def scale_sequence(self):
        title = Text("The Scale of the Problem", font_size=44, color=ACCENT_COLOR).scale(0.2)
        title.shift(UP*0.6)
        
        # Create dots representing hearings
        total_text = Text("Out of 19,713 Parole Hearings in NYS", font_size=36, color=TEXT_COLOR).scale(0.2)
        total_text.next_to(title, DOWN*1.5, buff=1)
        
        # Create grid of dots
        dots = VGroup()
        for i in range(20):
            for j in range(20):
                dot = Dot(radius=0.08, color=WHITE, fill_opacity=0.6)
                dot.move_to([i*0.3 - 3, j*0.2 - 2, 0])
                dots.add(dot)
        dots.scale(0.2)
        dots.move_to(ORIGIN)
        
        # Highlight released dots (about 20%)
        released_dots = dots[:80]  # Roughly 20% of 400 dots
        
        self.play(FadeIn(title))
        self.play(FadeIn(total_text))
        self.play(Create(dots), run_time=4)
        self.wait(3)
        
        released_text = Text("Only 4,168 Were Released (21%)", font_size=32, color=WARNING_COLOR).scale(0.2)
        released_text.shift(DOWN*0.6)
        
        self.play(
            released_dots.animate.set_color(SUCCESS_COLOR).set_fill(opacity=1),
            FadeIn(released_text),
            run_time=2
        )
        self.wait(3)
        self.play(FadeOut(released_text))

        possible_dots = dots[80:196]  # Roughly 20% of 400 dots

        possible_text = Text("We could have released another 5491 without increasing crime", font_size=32, color=WARNING_COLOR).scale(0.2)
        possible_text.shift(DOWN*0.6)
        
        self.play(
            possible_dots.animate.set_color(WARNING_COLOR).set_fill(opacity=1),
            FadeIn(possible_text),
            run_time=2
        )
        self.wait(5)
        self.play(FadeOut(title, total_text, dots, possible_text))

    def prison_days_sequence(self):
        title = Text("What does it really mean to have your parole denied?", font_size=40, color=ACCENT_COLOR).scale(0.2)
        title.shift(UP*0.6)

        # Start with one day
        single_day = Square(side_length=0.04, color=WARNING_COLOR, fill_opacity=0.6).scale(0.2)
        single_day.shift(UP*0.2)
        
        day_label = Text("1 Day in Prison", font_size=28, color=TEXT_COLOR).scale(0.2)
        day_label.next_to(single_day, DOWN, buff=0.1)

        self.play(FadeIn(title))
        self.wait(3)

        self.play(
            DrawBorderThenFill(single_day),
            FadeIn(day_label)
        )
        self.wait(3)

        # Show 2 years worth of days
        wait_text = Text("The average wait for another parole hearing is 2 years", font_size=32, color=WARNING_COLOR).scale(0.2)
        wait_text.shift(DOWN*0.4)
        
        self.play(FadeIn(wait_text))
        self.wait(4)
        
        # Create grid representing 730 days (2 years)
        days_grid = VGroup()
        for i in range(26):  # 26 rows
            for j in range(28):  # 28 columns = 728, close to 730
                if len(days_grid) < 730:
                    day_square = Square(side_length=0.04, color=WARNING_COLOR, fill_opacity=0.6).scale(0.2)
                    day_square.move_to([j*0.06 - 0.8, -i*0.04 + 0.5, 0])
                    days_grid.add(day_square)
        
        days_count = Text("730 Days", font_size=24, color=WARNING_COLOR).scale(0.2)
        days_count.next_to(days_grid, DOWN, buff=0.08)

        self.play(FadeOut(day_label, wait_text))
        self.play(ReplacementTransform(single_day, days_grid), FadeIn(days_count), run_time=2)
        self.wait(5)

        # Turn 730 days into 1 square
        shrink_text = Text("Now lets pack all those days back into 1 square", font_size=24, color=WARNING_COLOR).scale(0.2)
        shrink_text.shift(DOWN*0.5)
        single_day = Square(side_length=0.04, color=RED, fill_opacity=0.6).scale(0.2)
        self.play(ReplacementTransform(days_grid, single_day), FadeIn(shrink_text), run_time=2)
        scale_note = Text("Each square is ~2 years", font_size=20, color=TEXT_COLOR).scale(0.2)
        scale_note.shift(DOWN*0.7)

        # Now show the massive scale
        massive_text = Text("In a 2 year sample, 5,490 people were denied parole unnecessarily", font_size=32, color=TEXT_COLOR).scale(0.2)
        massive_text.shift(UP*0.4)
        
        total_days = self.bg_text("That's 4,007,700 unnecessary days in prison\nOver 10,000 YEARS of human life wasted")
        total_days.shift(DOWN*0.2)

        self.wait(3)
        self.play(
            FadeOut(days_count, shrink_text),
            FadeIn(massive_text)
        )
        self.wait(6)
        
        # Create visual representation of the massive number
        # Use dots to represent chunks of days (each dot = 1000 days)
        massive_dots = VGroup()
        for i in range(50):
            for j in range(100):
                if len(massive_dots) < 5008:  # Roughly 4,007,700 / 1000
                    dot = Dot(radius=0.008, color=RED, fill_opacity=0.8)
                    dot.move_to([j*0.016 - 0.8, -i*0.016 + 0.3, 0])
                    massive_dots.add(dot)


        self.play(
            FadeIn(total_days),
            ReplacementTransform(single_day, massive_dots),
            FadeIn(scale_note),
            run_time=3
        )
        
        self.wait(5)
        
        self.play(FadeOut(title, massive_text, total_days, massive_dots, scale_note))

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
        
        self.play(FadeIn(title))
        self.play(
            FadeIn(before_title),
            FadeIn(after_title)
        )
        self.play(
            DrawBorderThenFill(before_bar),
            DrawBorderThenFill(v_before_bar),
            FadeIn(before_label),
            FadeIn(v_before_label)
        )
        self.wait(1)
        self.play(
            DrawBorderThenFill(after_bar),
            DrawBorderThenFill(v_after_bar),
            FadeIn(after_label),
            FadeIn(v_after_label)
        )
        
        improvement = Text("70% REDUCTION in crime", font_size=32, color=SUCCESS_COLOR, weight=BOLD).scale(0.2)
        improvement.shift(DOWN*0.6)
        self.play(FadeIn(improvement))
        
        self.wait(2.5)
        self.play(FadeOut(title, before_title, after_title, before_bar, after_bar,
                          v_before_bar, v_after_bar, before_label, after_label,
                          v_before_label, v_after_label, improvement))

    def solution_sequence(self):
        title = Text("", font_size=40, color=ACCENT_COLOR).scale(0.2)
        title.shift(UP*0.6)
        
        # Key metrics
        metric1 = Text("✓ Double release rates", font_size=32, color=SUCCESS_COLOR)
        metric2 = Text("✓ Eliminate racial disparities", font_size=32, color=SUCCESS_COLOR)
        metric3 = Text("✓ Reduce crime by 70%", font_size=32, color=SUCCESS_COLOR)
        metric4 = Text("✓ Same or better public safety", font_size=32, color=SUCCESS_COLOR)
        
        metrics = VGroup(metric1, metric2, metric3, metric4).scale(0.2)
        metrics.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        metrics.center()
        
        self.play(FadeIn(title))
        for metric in metrics:
            self.play(FadeIn(metric), run_time=0.8)
        
        self.wait(2)
        self.play(FadeOut(title, metrics))

    def call_to_action(self):
        main_text = Text(
            "With a focus on risk assessment",
            font_size=48,
            color=ACCENT_COLOR,
            line_spacing=1.2,
            weight=BOLD
        ).scale(0.2)
        
        source = Text(
            "These decision don't have to be arbitrary",
            font_size=30,
            color=TEXT_COLOR,
            line_spacing=1.1
        ).scale(0.2)
        source.shift(DOWN*0.3)
        
        self.play(FadeIn(main_text), run_time=2)
        self.play(FadeIn(source), run_time=1.5)
        self.wait(3)
        self.play(FadeOut(main_text, source))

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
            corner_radius=0,
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

    def bg_text(self, text):
        citation = VGroup(
            Text(text,
                 font="Arial", font_size=24, color=BLUE_A, weight=BOLD),
        ).arrange(DOWN, buff=0.3).move_to(ORIGIN)

        # Citation background
        citation_bg = RoundedRectangle(
            width=citation.width + 1,
            height=citation.height + 0.5,
            corner_radius=0.0,
            fill_opacity=0.7,
            fill_color=BLUE_D,
            stroke_color=BLUE_C,
            stroke_width=1
        )

        citation_group = VGroup(citation_bg, citation).scale(0.2)
        return citation_group

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
            Text("• Parole denials should not be punitive",
                 font="Arial", font_size=28, color=GREEN_C, weight=MEDIUM),
            Text("• Algorithms can effectively calculate risk of reoffending",
                 font="Arial", font_size=28, color=GREEN_C, weight=MEDIUM),
            Text("• We can practice forgiveness without increasing crime",
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


# To render: manim -pqh parole_viz.py ParoleVisualization

