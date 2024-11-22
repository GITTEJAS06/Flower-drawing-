import turtle

def draw_petal(turtle_obj, radius, angle):
    for _ in range(2):
        turtle_obj.circle(radius, angle)
        turtle_obj.left(180 - angle)

def draw_flower(turtle_obj, num_petals, radius, angle):
    for _ in range(num_petals):
        draw_petal(turtle_obj, radius, angle)
        turtle_obj.left(360 / num_petals)

def main():
    window = turtle.Screen()
    window.bgcolor("white")
    flower_turtle = turtle.Turtle()
    flower_turtle.shape("turtle")
    flower_turtle.color("red")
    flower_turtle.speed(10)
    draw_flower(flower_turtle, 10, 100, 60)
    flower_turtle.hideturtle()
    window.exitonclick()

if __name__ == "__main__":
    main()
