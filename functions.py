# Finding the nearest weather station for a city and giving its ID
closest = min(df_stations.iterrows(), key = lambda df: (df[1][0]-city_lat)**2 + (df[1][1]-city_long)**2)
stationID = closest[0]
#print(closestID)
