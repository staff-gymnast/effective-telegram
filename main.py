from manim import *

class MyFirstAnimation(Scene):
    def construct(self):
        # Create a text object
        text = Text("Hello, Manim!")
        
        # Create a mathematical equation
        equation = MathTex(r"E=mc^2")
        
        # Add the text to the scene
        self.play(Write(text))
        
        # Wait for 2 seconds
        self.wait(2)
        
        # Transform the text into the equation
        self.play(Transform(text, equation))
        
        # Wait for 2 seconds
        self.wait(2)

if __name__ == "__main__":
    config.background_color = WHITE
    MyFirstAnimation().render()
