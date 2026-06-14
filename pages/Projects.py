import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "smartpower.db",
    check_same_thread=False
)

st.header("المشاريع")

with st.form("project"):

    name = st.text_input("اسم المشروع")

    client = st.text_input("العميل")

    contract = st.number_input(
        "قيمة التعاقد"
    )

    received = st.number_input(
        "المحصل"
    )

    progress = st.slider(
        "نسبة التنفيذ",
        0,
        100
    )

    if st.form_submit_button("حفظ"):

        conn.execute(
            """
            INSERT INTO projects
            (
            name,
            client,
            contract_value,
            received,
            progress
            )
            VALUES(?,?,?,?,?)
            """,
            (
                name,
                client,
                contract,
                received,
                progress
            )
        )

        conn.commit()

st.dataframe(
    pd.read_sql(
        "SELECT * FROM projects",
        conn
    )
)