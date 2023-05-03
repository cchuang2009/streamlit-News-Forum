# load required modules, 載入必要模組
import pandas as pd
from datetime import datetime
import streamlit as st

st.set_page_config(page_title="News Archive", page_icon=":newspaper:", layout="wide")

# Read CSV file, 讀取資料
df = pd.read_csv("news.csv")

# Convert date column to datetime 轉換時間資料格式
df["Published_date"] = pd.to_datetime(df["Published_date"])

# Sort by date, 依照時間排序
df = df.sort_values("Published_date", ascending=False)

# Set default selection to current year and month, 預定使用登錄的年月
now = datetime.now()
default_year_month = now.strftime("%Y-%b")

# Get unique year-month combinations from dataframe, 利用年月設定資料現選項
year_months = df["Published_date"].dt.strftime("%Y-%b").unique()
months = sorted(year_months, reverse=True)

# Add the last year-month to the months list if it's not already there
if default_year_month not in months:
    months.append(default_year_month)


# Sidebar menu for selecting month, 設定左邊選項
selected_month = st.sidebar.selectbox("Select Month", months, index=months.index(default_year_month))

# Keyword search box, 關鍵詞查詢
search_term = st.sidebar.text_input("Search News", "")

# Filter dataframe by selected month and search term, 關鍵詞查詢結果
filtered_df = df[(df["Published_date"].dt.strftime("%Y-%b") == selected_month) & (df["Title"].str.contains(search_term, case=False))]

# Display selected news, 顯示選取的項目
st.write(f"## News for :blue[{selected_month}]")

for title, source, date in filtered_df[["Title", "Source", "Published_date"]].itertuples(index=False):
    with st.expander(f'**{title}**'):
        st.write(f"{source}", unsafe_allow_html=True)
        st.write(f"*Published on :orange[{date.date()}]*")

# Show last 5 news articles in sidebar, 列出最新的五個訊息
st.sidebar.markdown("## Last 5 News Articles")
last_5_articles = df.head()[["Title", "Source", "Published_date"]].values.tolist()[::-1]
for article in last_5_articles:
    title, source, date = article
    st.sidebar.markdown(f"[{title}] - *Published on :orange[{date.date()}]*")
    
# If no selection made, show the most recent news article in main area, 如果如果沒有選項, 使用最後的日期內訊息
if not selected_month:
    st.write(f"# Latest News: [{df.iloc[0]['Title']}]({df.iloc[0]['Source']})")
