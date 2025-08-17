from manim import *

class PrisonCellVisualization(ThreeDScene):
    def construct(self):
        # Title sequence
        title = Text("Understanding Prison Confinement", font_size=48, color=WHITE).scale(0.2)
        subtitle = Text("A visualization of space and time", font_size=24, color=GRAY).scale(0.2)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        self.play(FadeIn(title), run_time=2)
        self.play(FadeIn(subtitle), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle), run_time=1.5)
        
        # Explanatory text
        intro_text = Text("Let's compare living spaces to understand scale", 
                         font_size=32, color=LIGHT_GRAY).scale(0.2)
        self.play(Write(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))
        
        # Define areas in square feet
        home_area = 2500
        apartment_area = 900
        cell_area = 70
        
        # Scale factor for visual sizes
        scale_factor = 0.02
        
        # Side lengths proportional to sqrt(area)
        home_side = (home_area * scale_factor) ** 0.5
        apt_side = (apartment_area * scale_factor) ** 0.5
        cell_side = (cell_area * scale_factor) ** 0.5
        
        # Enhanced 3D cubes with subtle gradients and better materials
        home = Cube(side_length=home_side, fill_opacity=0.3, color=BLUE, stroke_width=1, stroke_color=BLUE)
        home.set_fill(color=[BLUE, BLUE_E], opacity=0.3)
        
        apartment = Cube(side_length=apt_side, fill_opacity=0.3, color=GREEN, stroke_width=1, stroke_color=GREEN)
        apartment.set_fill(color=[GREEN, GREEN_D], opacity=0.3)
        
        cell = Cube(side_length=cell_side, fill_opacity=0.4, color=RED, stroke_width=1, stroke_color=RED)
        cell.set_fill(color=[RED, RED_E], opacity=0.4)
        
        # Enhanced labels with better typography and backgrounds
        home_label = VGroup(
            RoundedRectangle(width=3, height=1.2, corner_radius=0.0, stroke_width=0.5,
                           fill_color=BLUE, fill_opacity=0.2, stroke_color=BLUE),
            Text("Average Home\n2,500 sq ft", font_size=28, color=WHITE, weight=BOLD)
        )
        
        apartment_label = VGroup(
            RoundedRectangle(width=4, height=1.2, corner_radius=0.0, stroke_width=0.5,
                           fill_color=GREEN, fill_opacity=0.2, stroke_color=GREEN),
            Text("Average Apartment\n900 sq ft", font_size=28, color=WHITE, weight=BOLD)
        )
        
        cell_label = VGroup(
            RoundedRectangle(width=3, height=1.2, corner_radius=0.0, stroke_width=0.5,
                           fill_color=RED, fill_opacity=0.2, stroke_color=RED),
            Text("Prison Cell\n70 sq ft", font_size=28, color=WHITE, weight=BOLD)
        )
        
        # Position labels below cubes
        home_label.next_to(home, DOWN, buff=1)
        apartment_label.next_to(apartment, DOWN, buff=0.8)
        cell_label.next_to(cell, DOWN, buff=0.6)
        
        # Create groups
        cell_group = VGroup(cell, cell_label)
        apt_group = VGroup(apartment, apartment_label)
        home_group = VGroup(home, home_label)
        
        # Position them
        group = VGroup(cell_group, apt_group, home_group).scale(0.2)
        group.arrange(LEFT, buff=0.7)
        
        # Camera setup for 3D with more dramatic angle
        self.set_camera_orientation(phi=15 * DEGREES)
        
        # Context text
        context_text = Text("Most people live in spaces like these:", 
                           font_size=32, color=LIGHT_GRAY).scale(0.2)
        context_text.shift(UP*1.2)
        self.play(FadeIn(context_text))
        
        # Show progression with enhanced animations
        self.play(
            FadeIn(home, shift=UP), 
            Write(home_label[1]), 
            DrawBorderThenFill(home_label[0]),
            run_time=2
        )
        self.wait(1.5)
        
        self.play(
            FadeIn(apartment, shift=UP), 
            Write(apartment_label[1]), 
            DrawBorderThenFill(apartment_label[0]),
            run_time=2
        )
        self.wait(1.5)
        
        # Dramatic pause before showing cell
        contrast_text = Text("But some live in spaces like this:", 
                            font_size=32, color=YELLOW).scale(0.2)
        contrast_text.shift(UP).shift(LEFT)
        self.play(ReplacementTransform(context_text, contrast_text))
        self.wait(1)
        
        self.play(
            FadeIn(cell, shift=UP), 
            Write(cell_label[1]), 
            DrawBorderThenFill(cell_label[0]),
            run_time=2
        )
        self.wait(3)
        
        
        # Fade out larger contexts, keep cell
        self.play(
            FadeOut(home), FadeOut(home_label),
            FadeOut(apartment), FadeOut(apartment_label),
            FadeOut(contrast_text),
            run_time=2
        )
        self.wait(1)
        
        # Focus text
        focus_text = Text("Now let's focus on the prison experience", 
                         font_size=32, color=WHITE).scale(0.2)
        focus_text.shift(UP)
        self.play(FadeIn(focus_text))
        
        # Keep only the prison cell centered
        self.play(cell_group.animate.move_to(ORIGIN), run_time=2)
        self.wait(1)
        self.play(FadeOut(focus_text))
        
        '''
        # Enhanced prison time section with visual elements
        daily_routine_text = Text("Daily Reality:", font_size=40, color=YELLOW, weight=BOLD).scale(0.2)
        daily_routine_text.shift(UP*0.4)
        self.play(FadeIn(daily_routine_text))
        '''
        
        # Prison time: 23 hours in, 1 hour out simulated with flashes
        hours_in_cell = Text("23 hours a day in cell", font_size=36, color=RED).shift(UP).scale(0.2)
        hours_out_cell = Text("1 hour outside", font_size=24, color=GREEN).shift(DOWN*0.8).scale(0.2)
        
        # Clock visualization
        clock_circle = Circle(radius=0.8, color=WHITE, stroke_width=3).scale(0.2)
        clock_center = Dot(radius=0.02, color=WHITE).scale(0.2)
        hour_marks = VGroup(*[
            Line(ORIGIN, 0.15*UP).rotate(i*PI/6).shift(0.7*UP).rotate(i*PI/6, about_point=ORIGIN)
            for i in range(12)
        ]).scale(0.2)
        hour_marks.set_color(WHITE)
        
        clock = VGroup(clock_circle, hour_marks, clock_center)
        clock.shift(DOWN*1.5)
        
        self.play(
            Write(hours_in_cell),
            Write(hours_out_cell),
            DrawBorderThenFill(clock),
            run_time=2
        )
        
        # Time visualization with enhanced effects
        time_explanation = Text("Let's compress 24 hours into 24 seconds to feel the proportion\nThe cell disappears for as long as you're outside of it", 
                               font_size=24, color=LIGHT_GRAY).scale(0.2)
        time_explanation.shift(DOWN*0.5)
        self.play(FadeIn(time_explanation))
        
        for cycle in range(3):  # repeat twice for effect
            # Dim the cell for 23 seconds (representing 23 hours)
            self.play(
                cell.animate.set_fill(opacity=0.1),
                cell_label.animate.set_fill(opacity=0.3),
                hours_in_cell.animate.set_color(WHITE),
                run_time=0.5
            )
            self.wait(11)  # represent 23 hours compressed to 11 seconds
            
            # Brief moment outside (1 second for 1 hour)
            self.play(
                FadeOut(cell_group),
                hours_out_cell.animate.set_color(WHITE),
                run_time=0.5
            )
            self.play(
                FadeIn(cell_group),
                cell.animate.set_fill(opacity=0.4),
                hours_in_cell.animate.set_color(RED),
                hours_out_cell.animate.set_color(GREEN),
                run_time=0.5
            )
        
        self.wait(1)
        self.play(FadeOut(clock), FadeOut(hours_out_cell))
        
        # Solitary confinement section with enhanced drama
        transition_text = Text("But it can get worse...", font_size=32, color=ORANGE).scale(0.2)
        transition_text.shift(UP*0.7)
        self.play(
                #ReplacementTransform(daily_routine_text, transition_text),
            Write(transition_text),
            run_time=2
        )
        self.wait(2)
        
        # Solitary confinement section
        solitary_title = Text("Solitary Confinement:", font_size=40, color=RED, weight=BOLD).scale(0.2)
        solitary_title.shift(UP*0.4)
        
        solitary_text = Text("24 hours a day in cell", font_size=36, color=RED_E).shift(UP).scale(0.2)
        
        isolation_text = Text("Complete isolation • Almost no human contact", 
                             font_size=24, color=GRAY).scale(0.2)
        isolation_text.shift(DOWN*0.8)
        
        self.play(
            ReplacementTransform(transition_text, solitary_title),
            ReplacementTransform(hours_in_cell, solitary_text),
            FadeIn(isolation_text),
            cell.animate.set_color(RED_E),
            run_time=2
        )
        
        # Visual representation of complete confinement
        bars = VGroup(*[
            Rectangle(width=0.1, height=3, fill_color=GRAY, fill_opacity=0.8, stroke_width=0)
            for i in range(8)
        ]).scale(0.2)
        bars.arrange(RIGHT, buff=0.15)
        #bars.move_to(cell.get_center() + 1.2*RIGHT)
        bars.move_to(ORIGIN)
        
        self.play(FadeIn(bars), run_time=1.5)
        
        # Time indicator for solitary
        time_counter = Text("24 hours = 24 seconds", font_size=20, color=LIGHT_GRAY).scale(0.2)
        time_counter.shift(DOWN*0.3)
        self.play(FadeIn(time_counter))
        
        # Cell remains on screen for 24 seconds straight with subtle pulsing
        for i in range(24):
            if i % 4 == 0:  # Subtle pulse every 4 seconds
                self.play(
                    cell.animate.set_fill(opacity=0.2),
                    rate_func=there_and_back,
                    run_time=0.8
                )
            else:
                self.wait(1)
        
        # Final impact message
        self.play(FadeOut(time_counter))
        final_message = Text("This is the reality for hundreds of thousands", 
                            font_size=32, color=WHITE).scale(0.2)
        final_message.shift(DOWN*0.5)
        self.play(FadeIn(final_message), run_time=2)
        self.wait(3)
        
        # Fade out at end
        self.play(
            FadeOut(cell_group), 
            FadeOut(solitary_text), 
            FadeOut(solitary_title),
            FadeOut(isolation_text),
            FadeOut(bars),
            FadeOut(final_message),
            run_time=3
        )
        
        # Credits
        credits = Text("Data sources: Bureau of Justice Statistics, Prison Policy Initiative", 
                      font_size=18, color=GRAY).scale(0.2)
        self.play(FadeIn(credits))
        self.wait(2)
        self.play(FadeOut(credits))
