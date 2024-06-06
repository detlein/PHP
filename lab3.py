import pandas as pd
import matplotlib.pyplot as plt

# URLs for the datasets
urls = {
    'Confirmed': 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv',
    'Deaths': 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_deaths_global.csv&filename=time_series_covid19_deaths_global.csv',
    'Recovered': 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_recovered_global.csv&filename=time_series_covid19_recovered_global.csv'
}

# Load the confirmed cases dataset
confirmed_df = pd.read_csv(urls['Confirmed'])

# Get the list of unique countries
countries = confirmed_df['Country/Region'].unique().tolist()

print("Список доступных стран:")
for country in countries:
    print(country)

# User input for country and category
selected_country = input("Введите страну: ")
selected_category = input("Введите категорию (Confirmed/Recovered/Deaths): ")

# Load the appropriate dataset based on the selected category
df_country = pd.read_csv(urls[selected_category])
df_country = df_country[df_country['Country/Region'] == selected_country]

# Sum up the cases by date
df_category = df_country.drop(columns=['Province/State', 'Country/Region', 'Lat', 'Long']).sum()

# Calculate the daily increase
df_daily_increase = df_category.diff().fillna(df_category.iloc[0]).astype(int)

# Plotting
plt.figure(figsize=(12, 8))
plt.plot(df_category.index, df_category.values, label=selected_category)
plt.plot(df_daily_increase.index, df_daily_increase.values, label='Ежедневное увеличение')
plt.title(f"{selected_country} - {selected_category}")
plt.xlabel("Дата")
plt.ylabel("# случаев")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()