import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "smartpower.db",
    check_same_thread=False
)

st.header("العمالة")

with st.form("worker"):

    name = st.text_input("اسم العامل")

    phone = st.text_input("التليفون")

    daily = st.number_input("اليومية")

    if st.form_submit_button("حفظ"):

        conn.execute(
            """
            INSERT INTO workers
            (
            name,
            phone,
            daily_rate
            )
            VALUES(?,?,?)
            """,
            (
                name,
                phone,
                daily
            )
        )

        conn.commit()

st.dataframe(
    pd.read_sql(
        "SELECT * FROM workers",
        conn
    )
)