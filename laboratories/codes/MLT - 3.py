import turtle


def start_pos():
    turtle.penup()
    turtle.goto(-950, -300)
    turtle.pendown()
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(15)
    turtle.right(180)
    turtle.forward(30)
    turtle.left(180)
    turtle.forward(15)
    turtle.right(90)
    return


bit_code_input = '1100111001111001001'
window = turtle.Screen()
start_pos()
coord_y_now = -300
first_1 = 0
for i in range(len(bit_code_input)):
    if bit_code_input[i] == '0':
        turtle.forward(25)
    elif bit_code_input[i] == '1':
        if coord_y_now == -275:
            turtle.right(90)
            turtle.forward(25)
            coord_y_now += -25
            turtle.left(90)
            turtle.forward(25)
        elif coord_y_now == -300:
            if first_1 == 0:
                first_1 = 1
                turtle.left(90)
                turtle.forward(25)
                coord_y_now += 25
                turtle.right(90)
                turtle.forward(25)
            elif first_1 == 1:
                first_1 = 0
                turtle.right(90)
                turtle.forward(25)
                coord_y_now += -25
                turtle.left(90)
                turtle.forward(25)
        elif coord_y_now == -325:
            turtle.left(90)
            turtle.forward(25)
            coord_y_now += +25
            turtle.right(90)
            turtle.forward(25)

window.exitonclick()
