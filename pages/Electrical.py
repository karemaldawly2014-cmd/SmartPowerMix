import streamlit as st

st.header("Electrical Calculator")

rooms = st.number_input(
    "عدد الغرف"
)

acs = st.number_input(
    "عدد التكييفات"
)

heaters = st.number_input(
    "عدد السخانات"
)

load = (
    acs*2.5
    +
    heaters*1.5
    +
    rooms*0.7
)

st.metric(
    "Connected Load kW",
    round(load,2)
)