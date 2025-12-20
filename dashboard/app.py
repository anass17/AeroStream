import streamlit as st
import pandas as pd
import components.bar_chart as ch
from components.pie_chart import pie_chart
from components.line_chart import line_chart
from components.stat_box import html_stat_box

HEIGHT = 350



##### Header

st.set_page_config(page_title="AeroStream", page_icon="✈️", layout="wide")

st.title("AeroStream")
st.markdown("##### Analyse des tweets des compagnies aériennes")

st.divider()



##### Statistiques Generales

st.subheader("Statistiques Generales")

col1, col2, col3 = st.columns(3, gap="medium")

col1.html(html_stat_box("Nombre total de tweets", 100))
col2.html(html_stat_box("Nombre de compagnies aériennes", 4))
col3.html(html_stat_box("Pourcentage de tweets négatifs", "60.5%"))

st.divider()



##### Diagrammes

col1, col2 = st.columns(2, gap="large")



### 1 - Percentage de chaque sentiment

df_sentiments_counts = pd.DataFrame([
    ["Postive", 20],
    ["Neutral", 15],
    ["Negative", 23],
], columns=["sentiment", "count"])

col1.html("<h2 style='margin-bottom:20px'>Percentage de chaque sentiment</h2>")

chart = pie_chart(df_sentiments_counts, "sentiment", "Sentiment", HEIGHT)
col1.altair_chart(chart, use_container_width=True)



### 2 - Nombre de tweet par jour

df = pd.DataFrame({
    "tweet_created": pd.to_datetime([
        "2025-11-01", "2025-11-01", "2025-11-03",
        "2025-11-05", "2025-11-05", "2025-11-07", "2025-11-09",
        "2025-11-05", "2025-11-03", "2025-11-09",
        "2025-11-09", "2025-11-09", "2025-11-07", "2025-11-09",
        "2025-11-05", "2025-11-09", "2025-11-01",
        "2025-11-05", "2025-11-05", "2025-11-01", "2025-11-09",
        "2025-11-03"
    ])
})

col2.html("<h2 style='margin-bottom:20px'>Nombre de tweet par jour</h2>")

chart = line_chart(df, "tweet_created", "Date")
col2.altair_chart(chart, use_container_width=True)



### 3 - Volume de tweets par compagnie

df_volume = pd.DataFrame([
    ["United", 5],
    ["USAirline", 10],
    ["FlyLight", 32],
    ["AirWays", 22],
], columns=["airline", "count"])

col1.html("<h2 style='margin-bottom:20px'>Volume de tweets par compagnie</h2>")

chart = ch.horizental_bar_chart(df_volume, "airline", "count", "Airline", "Number of tweets", HEIGHT)
col1.altair_chart(chart, use_container_width=True)



### 4 - Répartition des sentiments par compagnie

df_sentiments = pd.DataFrame([
    ["United", "negative", 5],
    ["United", "neutral", 5],
    ["United", "positive", 5],
    ["USAirline", "negative", 10],
    ["USAirline", "neutral", 10],
    ["USAirline", "positive", 10],
    ["FlyLight", "negative", 32],
    ["FlyLight", "neutral", 32],
    ["FlyLight", "positive", 32],
    ["AirWays", "negative", 22],
    ["AirWays", "neutral", 22],
    ["AirWays", "positive", 22],
], columns=["airline", "label", "count"])

col2.html("<h2 style='margin-bottom:20px'>Répartition des sentiments par compagnie</h2>")

chart = ch.split_horizental_bar_chart(df_sentiments, "airline", "label", "count", "Compagnie", "sentiment", "Nombre de tweets", HEIGHT)
col2.altair_chart(chart, use_container_width=True)



### 5 - Taux de satisfaction par compagnie (%)

df_satisfaction = pd.DataFrame([
    ["United", 52.3],
    ["USAirline", 16.7],
    ["FlyLight", 22.4],
    ["AirWays", 20.8],
], columns=["airline", "satisfaction_rate"])


col1.html("<h2 style='margin-bottom:20px'>Taux de satisfaction par compagnie (%)</h2>")

chart = ch.horizental_bar_chart(df_satisfaction, "airline", "satisfaction_rate", "Airline", "Satisfaction Rate", HEIGHT)
col1.altair_chart(chart, use_container_width=True)



### 6 - Principales causes de tweets négatifs

df_negative_reasons = pd.DataFrame([
    ["Long Delay", 20],
    ["Bad Flight", 15],
    ["Aweful Service", 23],
    ["Disrespectful", 44],
], columns=["negativereason", "count"])


col2.html("<h2 style='margin-bottom:20px'>Principales causes de tweets négatifs</h2>")

chart = ch.horizental_bar_chart(df_negative_reasons, "negativereason", "count", "Negative Reason", "Number of tweets", HEIGHT)
col2.altair_chart(chart, use_container_width=True)



### 7 - Données agrégées détaillées

df_full_aggregation = pd.DataFrame({
    "airline": ["United", "Delta", "American", "Virgin America", "US Airways"],
    "total_tweets": [1200, 950, 870, 430, 300],
    "negative_tweets": [200, 180, 150, 60, 50],
    "positive_tweets": [900, 700, 650, 350, 230],
    "neutral_tweets": [100, 70, 70, 20, 20],
})

st.html("<h2 style='margin-bottom:20px'>Données agrégées détaillées</h2>")
st.dataframe(df_full_aggregation)