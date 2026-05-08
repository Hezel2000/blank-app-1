import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

temp_data_url = 'https://storage.googleapis.com/berkeley-earth-temperature-hr/global/Global_TAVG_monthly.txt'
temp_df = pd.read_csv(temp_data_url, comment='%', sep=r'\s+', header=None)

fig, ax = plt.subplots(figsize=(14, 7))
sns.lineplot(data=temp_df, x='date', y='monthly_anomaly_c', ax=ax)
ax.set_title('Global Monthly Average Temperature Anomaly (Celsius)')
ax.set_xlabel('Date')
ax.set_ylabel('Monthly Anomaly (°C)')
ax.grid(True)
plt.tight_layout()
st.pyplot(fig)