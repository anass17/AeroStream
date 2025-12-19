from tasks.queries import tweets_count_per_airline, sentiments_distribution, satisfaction_rate, identify_main_causes


#####

data = tweets_count_per_airline()

for airline, count in data:
    print(f"{airline :20s} - {count}")


#####

data_2 = sentiments_distribution()

for sentiment, count in data_2:
    print(f"{sentiment :10s} - {count}")


#####

data_3 = satisfaction_rate()

rate = (data_3['positive'] / data_3['total']) * 100

print(f"{rate}%")

##### 

data_4 = identify_main_causes()

for reason, count in data_4:
    print(f"{reason :40s} - {count}")