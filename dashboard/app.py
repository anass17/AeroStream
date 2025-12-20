import streamlit as st
import pandas as pd
import components.bar_chart as ch
from components.pie_chart import pie_chart
from components.line_chart import line_chart
from components.stat_box import html_stat_box
from streamlit_autorefresh import st_autorefresh
from extraction.data_fetch import (
    intiate_db, 
    tweets_count_per_airline, 
    tweet_count_per_date,
    sentiments_distribution,
    satisfaction_rate_per_airline,
    identify_main_causes,
    generale_statistics,
    detailled_data
)

HEIGHT = 400

st_autorefresh(interval=60000, key="refresh")



##### Header

st.set_page_config(page_title="AeroStream", page_icon="✈️", layout="wide")

st.title("AeroStream")
st.markdown("##### Analyse des tweets des compagnies aériennes")

st.divider()



##### initialiser la base de données

@st.cache_resource
def get_db():
    return intiate_db()

db, Prediction = get_db()



##### Statistiques Generales

st.subheader("Statistiques Generales")

col1, col2, col3 = st.columns(3, gap="medium")

data = generale_statistics(db, Prediction)

col1.html(html_stat_box("Nombre total de tweets", data[0]))
col2.html(html_stat_box("Nombre de compagnies aériennes", data[1]))
col3.html(html_stat_box("Pourcentage de tweets négatifs", f"{data[2]}%"))

st.divider()



##### Diagrammes

col1, col2 = st.columns(2, gap="large")



### 1 - Percentage de chaque sentiment

data = sentiments_distribution(db, Prediction)
df_sentiments_counts = pd.DataFrame(data, columns=["sentiment", "count"])

col1.html("<h2 style='margin-bottom:20px'>Percentage de chaque sentiment</h2>")

chart = pie_chart(df_sentiments_counts, "sentiment", "Sentiment", HEIGHT)
col1.altair_chart(chart, use_container_width=True)



### 2 - Nombre de tweet par jour

data = tweet_count_per_date(db, Prediction)
df_dates = pd.DataFrame(data, columns=["date", "count"])

col2.html("<h2 style='margin-bottom:20px'>Nombre de tweet par jour</h2>")

chart = line_chart(df_dates, "date", "Date", "count", "Number of tweets", HEIGHT)
col2.altair_chart(chart, use_container_width=True)



### 3 - Volume de tweets par compagnie

data = tweets_count_per_airline(db, Prediction)
data_sentiments = pd.DataFrame(data, columns=["airline", "label", "count"])

df_volume = data_sentiments[['airline', 'count']].groupby('airline').sum().reset_index()

col1.html("<h2 style='margin-bottom:20px'>Volume de tweets par compagnie</h2>")

chart = ch.horizental_bar_chart(df_volume, "airline", "count", "Airline", "Number of tweets", HEIGHT)
col1.altair_chart(chart, use_container_width=True)



### 4 - Répartition des sentiments par compagnie

col2.html("<h2 style='margin-bottom:20px'>Répartition des sentiments par compagnie</h2>")

chart = ch.split_horizental_bar_chart(data_sentiments, "airline", "label", "count", "Compagnie", "sentiment", "Nombre de tweets", HEIGHT)
col2.altair_chart(chart, use_container_width=True)



### 5 - Taux de satisfaction par compagnie (%)

data = satisfaction_rate_per_airline(db, Prediction)
df_satisfaction = pd.DataFrame(data, columns=["airline", "satisfaction_rate"])

col1.html("<h2 style='margin-bottom:20px'>Taux de satisfaction par compagnie (%)</h2>")

chart = ch.horizental_bar_chart(df_satisfaction, "airline", "satisfaction_rate", "Airline", "Satisfaction Rate", HEIGHT)
col1.altair_chart(chart, use_container_width=True)



### 6 - Principales causes de tweets négatifs

data = identify_main_causes(db, Prediction)
df_negative_reasons = pd.DataFrame(data, columns=["negativereason", "count"])


col2.html("<h2 style='margin-bottom:20px'>Principales causes de tweets négatifs</h2>")

chart = ch.horizental_bar_chart(df_negative_reasons, "negativereason", "count", "Negative Reason", "Number of tweets", HEIGHT)
col2.altair_chart(chart, use_container_width=True)



### 7 - Données agrégées détaillées

data = detailled_data(db, Prediction)
df_full_aggregation = pd.DataFrame(data, columns=["airline", "total_tweets", "negative_tweets", "positive_tweets", "neutral_tweets"])

st.html("<h2 style='margin-bottom:20px'>Données agrégées détaillées</h2>")
st.dataframe(df_full_aggregation)