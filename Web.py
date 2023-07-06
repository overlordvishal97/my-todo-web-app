import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo Aoo")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Enter a todo: ", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

st.session_state
# to run this code go to terminal and
# enter (straamlit run filename.py)
#to create a requirement.txt file use this command
# pip freeze > requirements.txt
