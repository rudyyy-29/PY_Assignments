import csv #comma separated
import json #dictionary format

with open('data_P01.csv','w') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Hrishi', 19, 'Jalgoan'])
    writer.writerow(['Paresh', 19, 'Satara'])
    writer.writerow(['CharDiwari', 35, 'Mumbai'])
    writer.writerow(['Rudra', 20, 'Pune'])

with open("data_P01.csv", "r") as csvfile:
    csvreader = csv.DictReader(csvfile)

    data = list(csvreader)


with open("data_P01.json", "w") as jsonfile:      # Write data into JSON file
    json.dump(data, jsonfile)

print("CSV data successfully converted to JSON.")
