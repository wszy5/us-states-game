import turtle
from tkinter import messagebox
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
guessed_states = []
print(states)
while game_is_on:

    answer_state = screen.textinput(title=f"Guess the State {score}/50", prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state in states:
        guessed_states.append(answer_state)
        score += 1
        # e_data = data.where(data["state"] == answer_state).dropna()
        e_data = data[data.state == answer_state]
        new_x = float(e_data["x"])
        new_y = float(e_data["y"])
        added_state = turtle.Turtle()
        added_state.hideturtle()
        added_state.penup()
        added_state.goto(x=new_x, y=new_y)
        added_state.write(answer_state)
        states.remove(answer_state)

    if states == []:
        messagebox.showinfo(title="Koniec gry", message="Gratulacje! :D")
        time.sleep(3)
        screen.exit()

    if answer_state == "Exit":
        a_states = set(states)
        c_states = set(guessed_states)
        unguessed_states = a_states - c_states
        messagebox.showinfo(title="Koniec gry", message=unguessed_states)
        time.sleep(4)
        screen.exitonclick()
