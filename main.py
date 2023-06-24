import turtle
import pandas
import csv

screen = turtle.Screen()
screen.title("Name the States")

# Make image a new turtle shape to turn screen to image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Import csv data into variable using pandas
data = pandas.read_csv("50_states.csv")
list_of_states = data["state"].tolist()

score = 0
game_is_on = True
guessed_states = []

answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?").title()

while len(guessed_states) < 50:

    if answer_state == "Exit":
        states_to_learn = [state for state in list_of_states if state not in guessed_states]
        # for state in list_of_states:
        #     if state not in guessed_states:
        #         states_to_learn.append(state)

        df = pandas.DataFrame(states_to_learn)
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in list_of_states:
        score += 1
        guessed_states.append(answer_state)
        state_data = data[data.state == f"{answer_state}"]
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)
        state_turtle = turtle.Turtle()
        state_turtle.penup()
        state_turtle.hideturtle()
        state_turtle.goto(x_cor, y_cor)
        state_turtle.write(arg=f"{answer_state}", align="center", font=("Courier", 10, "normal"))


    # states_to_learn.csv






    answer_state = screen.textinput(title=f"{score}/50 correct", prompt="What's another state name?").title()












