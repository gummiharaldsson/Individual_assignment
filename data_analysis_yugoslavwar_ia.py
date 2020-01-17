import json

# Loading the json data
with open('conflict_data_full_lined.json', encoding='utf8') as file:
    data = json.load(file)

total_deaths = 0
total_deaths_1992 = 0
with open('yugoslavia_death_data.csv', 'w', encoding='utf8') as file:
    file.write('deaths,date,\n')
    for datum in data:
        if 'Yugoslavia' in datum['country'] and (datum['year'] == 1991 or datum['year'] == 1992):
            country = datum['country']
            deaths = datum['best']
            #print(deaths)
            #total_deaths_1991 = total_deaths_1991 + datum['best']
            # total_deaths_1992 = total_deaths_1992 + datum['best']
            # print(total_deaths_1992)

            # Converting json data to csv
            file.write(f"{deaths},{datum['date_start']}\n")
    


