import turtle
import colorsys


# Setup
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
t.hideturtle()

# Animation parameters
layers = 24  # number of primary layers
petals = 12  # petals per layer
h = 0.0  # initial hue

# Create multiple layers of the mandala
for i in range(layers):
    # Set color with high saturation for neon effect
    color = colorsys.hsv_to_rgb(h, 0.9, 1)
    t.pencolor(color)

    # Draw one complete layer
    for _ in range(petals):
        # Draw petal
        t.pensize(2)
        t.circle(80 + i * 10, 60)  # Outer curve
        t.left(120)
        t.circle(80 + i * 10, 60)  # Inner curve
        t.left(120)

        # Draw connecting lines
        t.pensize(1)
        t.forward(100 + i * 10)
        t.backward(100 + i * 10)
        t.right(360 / petals)  # Rotate for next petal

    h += 0.8 / layers  # Gradually shift hue
    t.right(360 / layers)  # Slight rotation between layers

# Add center detail
h = 0
for i in range(36):
    color = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(color)
    t.circle(40, 90)
    t.left(90)
    t.circle(40, 90)
    t.left(10)
    h += 0.03

turtle.done()

