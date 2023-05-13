import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# Define the date range for the historical prices
start_date = datetime(2018, 1, 1)
end_date = datetime(2023, 5, 12)

# Define the base URL for the Yahoo Finance historical prices page
url = 'https://finance.yahoo.com/quote/AAPL/history'

# Define the headers for the HTTP GET requests to prevent 404 errors and look like a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
}

# Define a list to store the data rows
rows = []

# Loop over each date in the range and retrieve the historical prices data for that date
while start_date <= end_date:
    # Convert the date to UNIX timestamp format
    start_timestamp = int(start_date.timestamp())
    end_timestamp = int((start_date + timedelta(days=7)).timestamp())

    # Send an HTTP GET request for the historical prices page with the desired date range
    params = {
        'period1': start_timestamp,
        'period2': end_timestamp,
        'interval': '1d',
        'filter': 'history',
        'frequency': '1d',
        'includeAdjustedClose': 'true'
    }
    response = requests.get(url, headers=headers, params=params)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the historical prices table and extract the data rows
    table = soup.find('table', {'data-test': 'historical-prices'})
    for tr in table.find_all('tr')[1:]:
        row = [td.text.strip() for td in tr.find_all('td')]
        if len(row) == 7:
            rows.append(row)

    # Increment the date by a week
    start_date += timedelta(days=7)

# Create a Pandas DataFrame from the data rows
df = pd.DataFrame(rows, columns=['Date', 'Open', 'High', 'Low', 'Close*', 'Adj. close**', 'Volume'])
#print(df)

# save the data in csv file
df.to_csv('AAPL.csv', index=False)

