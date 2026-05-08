import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Global Average Temperature Anomaly Analysis')

@st.cache_data
def load_data():
    temp_data_url = 'https://storage.googleapis.com/berkeley-earth-temperature-hr/global/Global_TAVG_monthly.txt'
    temp_df = pd.read_csv(temp_data_url, comment='%', sep=r'\s+', header=None)

    temp_df.columns = [
        'year', 'month',
        'monthly_anomaly_c', 'monthly_anomaly_uncertainty_c',
        'annual_anomaly_c', 'annual_anomaly_uncertainty_c',
        'five_year_anomaly_c', 'five_year_anomaly_uncertainty_c',
        'ten_year_anomaly_c', 'ten_year_anomaly_uncertainty_c',
        'twenty_year_anomaly_c', 'twenty_year_anomaly_uncertainty_c'
    ]

    temp_df['year'] = temp_df['year'].astype(int)
    temp_df['month'] = temp_df['month'].astype(int)

    for col in temp_df.columns[2:]:
        temp_df[col] = pd.to_numeric(temp_df[col], errors='coerce')

    temp_df['date'] = pd.to_datetime(temp_df['year'].astype(str) + '-' + temp_df['month'].astype(str) + '-01')
    return temp_df


# Load the data
with st.spinner('Loading and processing data...'):
    temp_df = load_data()

st.subheader('Raw Data Preview')
st.dataframe(temp_df.head())

st.subheader('Data Information')
st.text(temp_df.info())

st.subheader('Global Monthly Average Temperature Anomaly (Celsius)')

fig, ax = plt.subplots(figsize=(14, 7))
sns.lineplot(data=temp_df, x='date', y='monthly_anomaly_c', ax=ax)
ax.set_title('Global Monthly Average Temperature Anomaly (Celsius)')
ax.set_xlabel('Date')
ax.set_ylabel('Monthly Anomaly (°C)')
ax.grid(True)
plt.tight_layout()
st.pyplot(fig)
