import turtle
import pandas
import turtle as turtle

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# To find the coordinates of each text location by clicking on the image
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
correct_answers = []

while len(correct_answers) < 50:
    answer_state = screen.textinput(title=f"{len(correct_answers)}/50", prompt="Name a state").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in correct_answers]
        # missing_states = []
        # for state in all_states:
        #     if state not in correct_answers:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        correct_answers.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

