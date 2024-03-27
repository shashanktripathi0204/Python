import turtle
import pandas as pd

states_data = pd.read_csv("States_India.csv")
states_name = states_data.State.to_list() # without this the "in" will not work

screen = turtle.Screen()
screen.title("India States Game")

# path to image
image = "India_States.gif"
# load in a new image as a new shape
screen.addshape(image)
turtle.shape(image)

# storing the user input, in upper case
guessed_state = []

score = 0
tries = 0
while(len(guessed_state) <= len(states_name)):
    answer_state = screen.textinput(title=f"{len(guessed_state)}/{56} Guess the states",
                                    prompt="Whats the name of the next one ?").title()
    # print(answer_state)
    if answer_state == "Exit":
        missing_state = {"State": []}
        for state in states_name:
            if state not in guessed_state:
                missing_state["State"].append(state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_state in states_name and answer_state not in guessed_state:
        score += 1
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row = states_data[states_data["State"] == answer_state]
        t.goto(float(state_row.x), float(state_row.y))
        t.write(state_row.State.item()) # t.write(answer_state)
    tries = tries + 1
