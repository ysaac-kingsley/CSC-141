
cities = {'Dubai':{
    'country' : 'UAE', 'population' : '11,000,000', 'fact': 'The Burj Khalifa is the tallest tower in the world located in the UAE'
},
'Doha':{
    'country': 'Qatar', 'population' : '3,000,000', 'fact': 'The 2022 World Cup was held in Qatar'
},
'Muscat':{
    'country':'Oman', 'population': '5,300,000', 'fact':'Oman has very beautiful natural caves during the monsoon season.'
}
}

for k,v in cities.items():
    country = f"{v['country']}"
    population =f"{v['population']}"
    fact = f"{v['fact']}"

    print(f"{k}:")
    print('In: '+ country + '\nPopulation: '+ population + '\nFact: '+ fact)
    print('\n')