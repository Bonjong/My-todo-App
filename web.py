import streamlit as st
import functions
todos=functions.get_todos()
def add_todo():
    todo=st.session_state['new_todo']+'\n'
    todos.append(todo)
    functions.write_todo(todos)


st.title('My Todo App')
st.subheader("Welcome to my todo app")
for index, todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input("", placeholder="please enter new Item", on_change=add_todo,key='new_todo')