import csv
import re
import plotly.express as px

counter = 0
list_of_skolor = []
list_of_kommuner = []
elever_of_skolor = []
sorted_together = []
sorted_elever = []
sorted_elever2 = []
sorted_skolor2 = []
sorted_skolor3 = []

def opening():
    global kommun 
    kommun = input("Vilken kommun vill du göra en graf av? Använd '*' för att grafa alla! ")

opening()

with open('elever.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list_of_skolor.append(row['Skola'])
        elever_of_skolor.append(row['Elever ÅK 1-9'])
        list_of_kommuner.append(row["Skolkommun"])
counter = 0

for i in elever_of_skolor:
    i = i.replace(" ", "")
    counter += 1
    sorted_skolor2.append(int(i[5:]))

counter = 0

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

for i in list_of_skolor:
    if kommun == "*":
        sorted_together.append((str(sorted_skolor2[counter]) + " " + list_of_skolor[counter]+"-"+list_of_kommuner[counter]))
    else:
        if list_of_kommuner[counter] == kommun:
            sorted_together.append((str(sorted_skolor2[counter]) + " " + list_of_skolor[counter]+"-"+list_of_kommuner[counter])) 
    counter += 1
    sorted_together.sort(key=natural_keys)

for i in sorted_together:
    sorted_elever2.append(i.split(" ")[0])
    sorted_skolor3.append(i.split(" ")[1])

if kommun == "*":
    file_name = "alla_kommuner" + ".html"
else:
    file_name = kommun + ".html"

try:
    fig = px.bar(x=sorted_skolor3, y=sorted_elever2)
    fig.write_html(file_name, auto_open=True)
except ValueError:
    print("Har du råkat hett in fel kommun tro? Testa köra om igen!")
    opening()
