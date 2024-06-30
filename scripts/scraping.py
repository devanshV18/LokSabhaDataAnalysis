import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://results.eci.gov.in/ResultAcGenMar2022/partywiseresult-S24.htm'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
    
    
relation = soup.find('table')

    
datarows = []

for row in relation.find_all('tr'):
    columns = row.find_all('td')
    if len(columns) > 1:
        row_data = [cell.text.strip() for cell in cells]
        
    
    
    df = pd.DataFrame(rows, columns=headers)
    df.to_csv('data/election_results.csv', index=False)
    print("Data scraped and saved to data/election_results.csv")


