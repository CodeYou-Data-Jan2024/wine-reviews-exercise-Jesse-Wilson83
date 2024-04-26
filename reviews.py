import pandas as pd
reviews = pd.read_csv("C:\\Users\\stayp\\github-classroom\\CodeYou-Data-Jan2024\\wine-reviews-exercise-Jesse-Wilson83\\data\\winemag-data-130k-v2.csv.zip")

#get the median
median_points = reviews.groupby('country').points.mean().round(1)

#get the countries
countries = reviews.country.unique()

# get the number of reviews
reviews_per_country = reviews.country.value_counts()

#create new data file
review_df = pd.DataFrame({'country':countries,'count':reviews_per_country.reindex(countries),'points':median_points.reindex(countries)})
review_df.fillna(0, inplace=True)
review_df['count']=review_df['count'].astype(int)
review_df_sorted = review_df.sort_values(by='count', ascending=False)
review_df_sorted.to_csv('C:\\Users\\stayp\\github-classroom\\CodeYou-Data-Jan2024\\wine-reviews-exercise-Jesse-Wilson83\\data\\reviews-per-country.csv', index=False, sep=',')
