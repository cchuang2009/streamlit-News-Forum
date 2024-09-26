import pandas as pd
from datetime import datetime
import streamlit as st

st.set_page_config(page_title="News Archive", page_icon=":newspaper:", layout="wide")

# Read CSV file
df = pd.read_csv("news.csv")

# Convert date column to datetime
df["Published_date"] = pd.to_datetime(df["Published_date"])

# Sort by date
df = df.sort_values("Published_date", ascending=False)

# Set default selection to current year and month
now = datetime.now()
default_year_month = now.strftime("%Y-%b")

# Get unique year-month combinations from dataframe
year_months = df["Published_date"].dt.strftime("%Y-%b").unique()

# Sort months by year and then by month
months = sorted(year_months, key=lambda x: (int(x[:4]), ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"].index(x[-3:])), reverse=True)

# Extract the year and month of the last news article
last_news_date = pd.to_datetime(df.iloc[-1]["Published_date"])
last_news_year_month = last_news_date.strftime("%Y-%b")

# Add the last year-month to the months list if it's not already there
if default_year_month not in months:
    months.append(default_year_month)

# Sidebar menu for selecting month
if default_year_month not in months:
    st.write("No news")
else:
    selected_month = st.sidebar.selectbox("Select Month", months, index=months.index(default_year_month))

# Keyword search box
search_term = st.sidebar.text_input("Search News", "")

# Filter dataframe by selected month and search term
filtered_df = df[(df["Published_date"].dt.strftime("%Y-%b") == selected_month) & (df["Title"].str.contains(search_term, case=False))]

# Display selected news
st.write(f"## News for :blue[{selected_month}]")

for title, source, date in filtered_df[["Title", "Source", "Published_date"]].itertuples(index=False):
    if len(filtered_df) > 0:
        with st.expander(f'**{title}**'):
            st.write(f"{source}", unsafe_allow_html=True)
            st.write(f"*Published on :orange[{date.date()}]*")
    else:
        st.write("No news updated this month!")

# Show last 5 news articles in sidebar
st.sidebar.markdown("## Last 5 News Articles")
last_5_articles = df.head()[["Title", "Source", "Published_date"]].values.tolist()[::-1]
for article in last_5_articles:
    title, source, date = article
    st.sidebar.markdown(f"[{title}] - *Published on :orange[{date.date()}]*")

# If no selection made, show the most recent news article in main area
if not selected_month:
    st.write(f"# Latest News: [{df.iloc[0]['Title']}]({df.iloc[0]['Source']})")
