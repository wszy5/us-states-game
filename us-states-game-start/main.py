import turtle
import pandas
import time

screen = turtle.Screen()
screen.title('U.S. States Game')

image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

score = 0
game_is_on = True
data = pandas.read_csv(open("50_states.csv"))
states = data["state"].to_list()
print(states)
while game_is_on:

    answer_state = screen.textinput(title=f"Guess the State {score}/50", prompt="What's another state's name?")
    answer_state = answer_state.title()


    if answer_state in states:
        score += 1
        e_data = data.where(data["state"] == answer_state).dropna()
        new_x = float(e_data["x"])
        new_y = float(e_data["y"])
        added_state = turtle.Turtle()
        added_state.hideturtle()
        added_state.penup()
        added_state.goto(x=new_x, y=new_y)
        added_state.write(answer_state)
        states.remove(answer_state)

    if states == []:
        end = turtle.Turtle()
        end.penup()
        end.hideturtle()
        end.goto(0,0)
        end.write("Congratulations!")
        time.sleep(3)
        screen.exit()


