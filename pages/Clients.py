import streamlit as st
import sqlite3

conn = sqlite3.connect(
    "smartpower.db",
    check_same_thread=False
)

st.header("العملاء")

with st.form("client"):

    name = st.text_input(
        "الاسم"
    )

    phone = st.text_input(
        "الموبايل"
    )

    address = st.text_area(
        "العنوان"
    )

    if st.form_submit_button(
        "حفظ"
    ):

        conn.execute(
            """
            INSERT INTO clients
            (
            name,
            phone,
            address
            )
            VALUES(?,?,?)
            """,
            (
                name,
                phone,
                address
            )
        )

        conn.commit()