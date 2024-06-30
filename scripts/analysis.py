import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

dataf = pd.read_csv('data/election_results.csv')
    
    
dataf.dropna(inplace=True)

    

total_seats = dataf['Seats'].astype(int).sum()
party_seat_count = df.groupby('Party')['Seats'].sum()

    

plt.figure(figsize=(10, 6))
    
plt.ylabel('Seats')
    
plt.savefig('data/party_seat_distribution.png')
plt.show()



