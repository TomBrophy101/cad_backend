import csv
import requests

# This points directly to your FastAPI backend endpoint
URL = "http://127.0.0.1:8000/items/"
insertions = 0

print("Reading MOCK_DATA.csv and sending data to backend...")

try:
    # Opens your mock data file safely
    with open("backend/MOCK_DATA.csv",
              mode="r", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            # Pushes the row dictionary straight to FastAPI
            response = requests.post(URL, json=row)

            if response.status_code == 200:
                insertions += 1
            else:
                # Matches your target output format:
                # prints the row data along with the status code
                print(row, response.status_code)

    print(f"\nTotal insertions: {insertions}")

except FileNotFoundError:
    print("\nERROR: Could not find 'MOCK_DATA.csv'.")
    print("Make sure your CSV file is spelled exactly")
    print("'MOCK_DATA.csv' and is in this same folder!")
