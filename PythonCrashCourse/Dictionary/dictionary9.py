cities = {
    'itapetininga': {
        'country': 'Brasil',
        'population': '200000',
        'fact': 'really shitty',
    },
    'london':{
        'country': 'England',
        'population': '1.000.000',
        'fact': 'even shittier',
    },
    'california':{
        'country': 'USA',
        'population': '10.000.000',
        'fact': 'somehow the worst of the 3',
    },
}

for city, fact in cities.items():
    print(f"\n City:{'itapetininga'}")
    country = f"{'itapetininga'['country']}"
    print(country)