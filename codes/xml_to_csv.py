# Import libraries
# pip install pandas
import xml.etree.ElementTree as Xet
import pandas as pd

cols = []
rows = []

# Parsing the XML file
xmlparse = Xet.parse("path/to/file.xml")         #Replace the file.xml with the path to the relevant '.xml' file
root = xmlparse.getroot()

for i in root:
    data = {}
    for col in cols:
        data[col] = i.find(col).text
    rows.append(data)

df = pd.DataFrame(rows, columns=cols)

# Writing dataframe to csv
df.to_csv("path/to/save/output.csv")    # Enter your path directory and give your CSV filename with .csv
