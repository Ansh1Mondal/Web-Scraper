import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the web page you want to scrape
url = 'https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2022-23-14450'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the request with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

     # Find the table header (if any)
    table_header = soup.find('thead')

    # Extract the header row
    headers = [span.text.strip() for span in table_header.find_all('span')]

    # headers = ["Column1","Column2","Column3","Column4","Column5","Column6","Column7"]

    # Find elements on the page (example: all paragraph tags)
    tablerow = soup.find_all('tr')

    data=[]

    # Loop through the elements and print the text
    for row in tablerow:
        # Find all columns in the row
        columns = row.find_all('td')

        # Only process rows with the expected number of columns
        if len(columns) > 1:
            # Extract text from each column and strip whitespace
            row_data = [col.text.strip() for col in columns]
            # Append the row data to the list
            data.append(row_data)

    # Convert the data list to a Pandas DataFrame
    df = pd.DataFrame(data,columns=headers)

    # convert the DataFrame into excel
    
    df.loc[1:].to_excel("t20_data.xlsx",index=False)

    print("Excel created")

    # Print the DataFrame

    # print(df.loc[1:])
    # print(df)


        # Print the text of each column, separated by a comma
        # print(", ".join([col.text.strip() for col in columns])) # strip us used to remove any white spaces or tabs etc.
else: 
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
