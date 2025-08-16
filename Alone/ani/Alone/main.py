from manim import *

class PrisonCellVisualization(ThreeDScene):
    def construct(self):
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

        # 3D cubes
        home = Cube(side_length=home_side, fill_opacity=0.2, color=BLUE)
        apartment = Cube(side_length=apt_side, fill_opacity=0.2, color=GREEN)
        cell = Cube(side_length=cell_side, fill_opacity=0.2, color=RED)

        # Labels
        home_label = Text("Average Home\n2500 sq ft", font_size=32).next_to(home, DOWN)
        apartment_label = Text("Average Apartment\n900 sq ft", font_size=32).next_to(apartment, DOWN)
        cell_label = Text("Prison Cell\n70 sq ft", font_size=32).next_to(cell, DOWN)

        cell_group = VGroup(cell, cell_label)
        apt_group = VGroup(apartment, apartment_label)
        home_group = VGroup(home, home_label)

        # Position them
        group = VGroup(cell_group, apt_group, home_group).scale(0.2)
        group.arrange(RIGHT, buff=0.7)

        # Camera setup for 3D
        self.set_camera_orientation(phi=7 * DEGREES)

        # Show progression
        self.play(FadeIn(home), Write(home_label))
        self.wait(1)
        self.play(FadeIn(apartment), Write(apartment_label))
        self.wait(1)
        self.play(FadeIn(cell), Write(cell_label))
        self.wait(2)

        # Fade out larger contexts, keep cell
        self.play(FadeOut(home), FadeOut(home_label),
                  FadeOut(apartment), FadeOut(apartment_label))
        self.wait(1)

        # Keep only the prison cell centered
        self.play(cell_group.animate.move_to(ORIGIN))
        self.wait(1)

        # Prison time: 23 hours in, 1 hour out simulated with flashes
        hours_in_cell = Text("23 hours a day in cell", font_size=36).shift(UP*0.5).scale(0.2)
        self.play(Write(hours_in_cell))

        for _ in range(2):  # repeat twice for effect
            self.wait(11)  # represent 23 hours compressed to 11 seconds
            self.play(FadeOut(cell_group), run_time=0.5)
            self.play(FadeIn(cell_group), run_time=0.5)

        self.wait(1)

        # Solitary confinement section
        solitary_text = Text("Solitary Confinement:\n24 hours a day in cell",
                             font_size=36).shift(UP*0.5).scale(0.2)
        self.play(ReplacementTransform(hours_in_cell, solitary_text))

        # Cell remains on screen for 24 seconds straight
        self.wait(24)

        # Fade out at end
        self.play(FadeOut(cell_group), FadeOut(solitary_text))

