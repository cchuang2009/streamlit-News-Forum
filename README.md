# streamlit-News-Forum

This is a simple news board artifact created by chatgpt. To provide the data inthis artifact, only create the file `news.csv` as follows, 這是使用 chatgpt產生的新聞發佈榜，讀取並發佈 `news.csv` 裡面的資料格式如下:
```
Title,Source,Publish_date
"title1","news content1",YYYY-MM-DD
"title2","news content2",YYYY-MM-DD
```
where `YYYY-MM-DD` is the datetime format, such as `2023-02-01`, 使用 datetime 的時間模式, `YYYY-MM-DD`. If `"` symobl required in content, :red[double this symbol], 如果消息本文中含有 `"`，則將符號重複.
To prepare the "news.csv", and run the following on shell to startup, 準備好檔案之後，執行下列程式啟動應用程式:
```
streamlit run app.py
```
[Streamlit App](https://cchuang2009-streamlit-news-forum-app-9ayjmo.streamlit.app/)

TODO
---
1. Key-words searching function, (done under testing),  關鍵詞的查詢功能，測試中.
2. Helper app to add new news, 輸入新消息的輔助程式.
