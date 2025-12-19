from tasks.queries import tweets_count_per_airline, sentiments_distribution

data = tweets_count_per_airline()

for airline, count in data:
    print(f"{airline :20s} - {count}")

data_2 = sentiments_distribution()

for sentiment, count in data_2:
    print(f"{sentiment :10s} - {count}")