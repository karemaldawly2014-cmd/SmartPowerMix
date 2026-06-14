import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect(
    "smartpower.db",
    check_same_thread=False
)

projects = pd.read_sql(
    "SELECT * FROM projects",
    conn
)

expenses = pd.read_sql(
    "SELECT * FROM expenses",
    conn
)

materials = pd.read_sql(
    "SELECT * FROM materials",
    conn
)

contracts = projects["contract_value"].sum()

received = projects["received"].sum()

expense_total = expenses["amount"].sum()

material_total = (
    materials["qty"] *
    materials["price"]
).sum()

profit = (
    received
    - expense_total
    - material_total
)

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "التعاقدات",
    f"{contracts:,.0f}"
)

c2.metric(
    "المحصل",
    f"{received:,.0f}"
)

c3.metric(
    "المصاريف",
    f"{expense_total:,.0f}"
)

c4.metric(
    "صافي الربح",
    f"{profit:,.0f}"
)