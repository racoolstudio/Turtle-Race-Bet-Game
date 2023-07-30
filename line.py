from turtle import Turtle


class Line(Turtle):
    def __init__(self, x, y, color1, color2):
        super().__init__()
        self.x = x
        self.y = y
        self.color1 = color1
        self.color2 = color2
        self.hideturtle()

    def draw(self):
        # Prepare the turtle to draw the line
        self.penup()
        self.goto(self.x, self.y)
        self.right(90)
        self.width(10)

        # Draw the Line.
        for i in range(10):
            self.pendown()
            # Alternate the colors of the line segments
            if i % 2 == 0:
                self.color(self.color1)
            else:
                self.color(self.color2)
            self.fd(30)
