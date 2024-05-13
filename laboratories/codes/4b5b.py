import turtle


def b4_to_b5(input_code, dictionary):
    temporary_code = []
    output_code = []
    count = 0
    result = ''
    while count < len(input_code):
        temporary_code.append(input_code[count:count + 4])
        count += 4
    for letter in range(len(temporary_code)):
        output_code.append(dictionary[temporary_code[letter]])
    for per in range(len(output_code)):
        result += output_code[per]
    return result


def start_pos(x, y):
    turtle.penup()
    turtle.goto(x, y)
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


def usual_code(code_input):
    previous_digit = '-1'
    for i in range(len(code_input)):
        if code_input[i] == '0' and previous_digit == '1':
            turtle.right(90)
            turtle.forward(25)
            turtle.left(90)
            turtle.forward(25)
            previous_digit = '0'
        elif code_input[i] == '0':
            turtle.forward(25)
            previous_digit = '0'
        elif code_input[i] == '1' and previous_digit == '0':
            turtle.left(90)
            turtle.forward(25)
            turtle.right(90)
            turtle.forward(25)
            previous_digit = '1'
        elif code_input[i] == '1' and previous_digit == '1':
            turtle.forward(25)
            previous_digit = '1'
        elif code_input[i] == '1':
            turtle.left(90)
            turtle.forward(25)
            turtle.right(90)
            turtle.forward(25)
            previous_digit = '1'


dict_code = {'0000': '11110', '0001': '01001', '0010': '10100', '0011': '10101', '0100': '01010', '0101': '01011',
             '0110': '01110', '0111': '01111', '1000': '10010', '1001': '10011', '1010': '10110', '1011': '10111',
             '1100': '11010', '1101': '11011', '1110': '11100', '1111': '11101', }
bit_code_input = '11001010001110111011111101101111'
while (len(bit_code_input) % 4) != 0:
    bit_code_input += '0'
bit_code_output = b4_to_b5(bit_code_input, dict_code)
print(f'Исходная двоичная последовательность : {bit_code_input}')
print(f'Двоичная последовательность после 4b/5b : {bit_code_output}')


window = turtle.Screen()

start_pos(-450, 200)
usual_code(bit_code_input)

start_pos(-450, 0)
usual_code(bit_code_output)

coord_y_now = -200
start_pos(-450, coord_y_now)
first_1 = 0
bit_code_output_MLT_3 = ''
for let in range(len(bit_code_output)):
    if bit_code_output[let] == '0':
        turtle.forward(25)
        if coord_y_now == -175:
            bit_code_output_MLT_3 += '+1'
        elif coord_y_now == -200:
            bit_code_output_MLT_3 += '0'
        elif coord_y_now == -225:
            bit_code_output_MLT_3 += '-1'
    elif bit_code_output[let] == '1':
        if coord_y_now == -175:
            turtle.right(90)
            turtle.forward(25)
            coord_y_now += -25
            turtle.left(90)
            turtle.forward(25)
            bit_code_output_MLT_3 += '0'
        elif coord_y_now == -200:
            if first_1 == 0:
                first_1 = 1
                turtle.left(90)
                turtle.forward(25)
                coord_y_now += 25
                turtle.right(90)
                turtle.forward(25)
                bit_code_output_MLT_3 += '+1'
            elif first_1 == 1:
                first_1 = 0
                turtle.right(90)
                turtle.forward(25)
                coord_y_now += -25
                turtle.left(90)
                turtle.forward(25)
                bit_code_output_MLT_3 += '-1'
        elif coord_y_now == -225:
            turtle.left(90)
            turtle.forward(25)
            coord_y_now += +25
            turtle.right(90)
            turtle.forward(25)
            bit_code_output_MLT_3 += '0'
print(f'Двоичная последовательность после MLT - 3 : {bit_code_output_MLT_3}')
window.exitonclick()
