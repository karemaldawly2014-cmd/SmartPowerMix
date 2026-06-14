import streamlit as st
import sqlite3

conn = sqlite3.connect(
    "smartpower.db",
    check_same_thread=False
)

st.header("الخامات")

with st.form("mat"):

    project = st.text_input(
        "المشروع"
    )

    item = st.text_input(
        "الصنف"
    )

    qty = st.number_input(
        "الكمية"
    )

    price = st.number_input(
        "سعر الوحدة"
    )

    if st.form_submit_button(
        "حفظ"
    ):

        conn.execute(
            """
            INSERT INTO materials
            (
            project,
            item,
            qty,
            price
            )
            VALUES(?,?,?,?)
            """,
            (
                project,
                item,
                qty,
                price
            )
        )

        conn.commit()