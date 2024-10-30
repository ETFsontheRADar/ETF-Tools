pip install requests beautifulsoup4


import requests
from bs4 import BeautifulSoup

url = "https://bmogam.com/ca-en/products/exchange-traded-funds/find-an-etf/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the ETF data
table = soup.find('table', {'id': 'etf-table'})

# Extract ETF information
etfs = []
for row in table.find_all('tr')[1:]:  # Skip the header row
    columns = row.find_all('td')
    if len(columns) >= 2:
        etf_name = columns[0].text.strip()
        etf_ticker = columns[1].text.strip()
        etfs.append((etf_name, etf_ticker))

# Print the list of ETFs
for etf in etfs:
    print(f"Name: {etf[0]}, Ticker: {etf[1]}")