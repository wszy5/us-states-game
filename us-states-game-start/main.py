import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')

image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

game_is_on = True
while game_is_on:

    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    answer_state = answer_state.title()


    data = pandas.read_csv(open("50_states.csv"))

    if answer_state in data["state"].to_list():
        data = data.where(data["state"] == answer_state)
        data = data.dropna()
        new_x = float(data["x"])
        new_y = float(data["y"])
        added_state = turtle.Turtle()
        added_state.hideturtle()
        added_state.penup()
        added_state.goto(x=new_x, y=new_y)
        added_state.write(answer_state)


screen.exitonclick()
