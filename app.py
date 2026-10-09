import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Air Tracker",
    layout="wide"
)

st.title("✈️ Air Tracker Flight Analytics")

airport_df = pd.read_csv("airport.csv")
flight_df = pd.read_csv("flights.csv")
delay_df = pd.read_csv("airport_delays.csv")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Airports", len(airport_df))

with col2:
    st.metric("Total Flights", len(flight_df))

with col3:
    st.metric(
        "Average Delay Index",
        round(delay_df["delay_index"].mean(), 2)
    )

st.subheader("Airport Data")
st.dataframe(airport_df)

st.subheader("Flight Status")
st.bar_chart(
    flight_df["status"].value_counts()
)

st.subheader("Airport Delays")
st.bar_chart(
    delay_df.set_index("airport_iata")["delay_index"]
)
