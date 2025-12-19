from tasks.queries import tweets_count

data = tweets_count()

for airline, total in data:
    print(f"{airline :20s} - {total}")


