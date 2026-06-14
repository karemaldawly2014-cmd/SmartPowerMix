import streamlit as st
import sqlite3

conn = sqlite3.connect(
    "smartpower.db",
    check_same_thread=False
)

st.header("المصاريف")

with st.form("expense"):

    project = st.text_input(
        "المشروع"
    )

    expense_type = st.selectbox(
        "نوع المصروف",
        [
            "بنزين",
            "عدة",
            "فطار",
            "نثريات"
        ]
    )

    amount = st.number_input(
        "القيمة"
    )

    if st.form_submit_button(
        "حفظ"
    ):

        conn.execute(
            """
            INSERT INTO expenses
            (
            project,
            expense_type,
            amount
            )
            VALUES(?,?,?)
            """,
            (
                project,
                expense_type,
                amount
            )
        )

        conn.commit()