import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape
url = "https://www.scrapethissite.com/pages/forms"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the data
table = soup.find("table")

# Extract data from the table and store it in a list of dictionaries
data = []
headers = []
for index, row in enumerate(table.find_all("tr")):
    columns = row.find_all(["th", "td"])
    if index == 0:  # Extract headers from the first row
        headers = [header.text.strip() for header in columns]
    else:
        data.append([column.text.strip() for column in columns])

# Create a pandas DataFrame from the extracted data
df = pd.DataFrame(data, columns=headers)

# Save the DataFrame to a CSV file
df.to_csv("result.csv", index=False)

print("Data has been scraped and saved to 'result.csv'.")
