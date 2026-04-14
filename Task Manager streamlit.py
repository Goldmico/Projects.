# MADE BY D1PREZZ
# DO NOT STEAL
# TASK MANAGER STREAMLIT V1

import streamlit as st

col1,col2,col3 = st.columns(3)
with col1:
    pass
with col2:
    st.title("Task Saver")
with col3:
    pass


task_input = ()

# V2 | adding .append means we can do INFINITE TASKS!

if "task" not in st.session_state: # This is saying: If there is no task saved, create a new one.
    st.session_state.task = []

choice = st.selectbox("Pick an option", ["View Tasks", "Add Tasks", "Delete Tasks"])

if choice == "Add Tasks":
    task_input = st.text_input("Enter a task")
    if task_input:
        st.write("Task saved")
        st.session_state.task.append(task_input) # Created saved task veriable

elif choice == "View Tasks":
    st.write(st.session_state.task) # This prints the saved task
    if st.session_state.task.append == "":
        st.write("No task at the moment")

elif choice == "Delete Tasks":
    delete_confirmation = st.button("Delete all tasks?")
    delete_separate = st.button("Delete separate tasks?")

    if delete_confirmation:
        st.session_state.task = []
        st.write("Tasks removed.")
