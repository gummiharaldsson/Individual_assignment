import json

# Loading the json data
with open('conflict_data_full_lined.json', encoding='utf8') as file:
    data = json.load(file)

total_deaths = 0
with open('yugoslavia_death_data.csv', 'w', encoding='utf8') as file:
    for datum in data:
        if 'Yugoslavia' in datum['country'] and datum['year'] == 1991:
            country = datum['country']
            deaths = datum['best']
            #print(deaths)
            total_deaths = total_deaths + datum['best']
            #print(f'Number of deaths {datum["best"]}')

            # Converting json data to csv
            file.write(f'{country},{deaths}\n')
    


