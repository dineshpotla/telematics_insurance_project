import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("data/processed_data.csv")

st.title("Telematics Insurance Risk Dashboard")
st.write("Insights from telematics data")

# Show data summary
st.dataframe(data.head())

# Display risk score distribution
st.subheader("Risk Score Distribution")
plt.hist(data['risk_score'], bins=20)
st.pyplot(plt)

# Average speed vs. accident risk
st.subheader("Average Speed vs. Accident Occurrence")
plt.scatter(data['avg_speed'], data['accident_occurred'])
st.pyplot(plt)
