import pandas as pd
from datetime import datetime
import streamlit as st

st.set_page_config(page_title="News Archive", page_icon=":newspaper:", layout="wide")

# Read CSV file
df = pd.read_csv("news.csv")

# Convert date column to datetime
df["Publish_date"] = pd.to_datetime(df["Publish_date"])

# Sort by date
df = df.sort_values("Publish_date", ascending=False)

# Set default selection to current year and month
now = datetime.now()
default_year_month = now.strftime("%Y-%b")

# Get unique year-month combinations from dataframe
year_months = df["Publish_date"].dt.strftime("%Y-%b").unique()
months = sorted(year_months, reverse=True)

# Sidebar menu for selecting month
#selected_month = st.sidebar.selectbox("Select Month", months, index=months.tolist().index(default_year_month))
selected_month = st.sidebar.selectbox("Select Month", months, index=months.index(default_year_month))

# Filter dataframe by selected month
filtered_df = df[df["Publish_date"].dt.strftime("%Y-%b") == selected_month]
   
# Display selected news
st.write(f"## News for :blue[{selected_month}]")

for title, source, date in filtered_df[["Title", "Source", "Publish_date"]].itertuples(index=False):
    with st.expander(f'**{title}**'):
        #st.markdown(f"[{source}]({source})") 
        st.write(f"{source}",unsafe_allow_html=True)
        st.write(f"*Published on :orange[{date.date()}]*")  
    
# Show last 5 news articles in sidebar
st.sidebar.markdown("## Last 5 News Articles")
last_5_articles = df.head()["Title"].values.tolist()[::-1]
for article in last_5_articles:
    st.sidebar.write(article)

# If no selection made, show the most recent news article in main area
if not selected_month:
    st.write(f"# Latest News: [{df.iloc[0]['Title']}]({df.iloc[0]['Source']})")
