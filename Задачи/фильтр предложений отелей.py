KOSTROVOK_FEE = 0.12
BOOKKING_CONVERT_RATE = 75


def find_all_matches(data, **kwargs):
    if not kwargs:
        min_cost = - float('inf')
        max_cost = float('inf')
    else:
        min_cost, max_cost = kwargs
    kost = lambda x: x + 0.12*x
    bok  =lambda x: x * 75 
    servises = [kost for x['cost'] in data]



data = [
  {
    "service": "kostrovok",
    "hotels": [
      { "name": "$phpInn", "cost": 600 },
      { "name": "JSInn", "cost": 620 },
      { "name": "python_inn", "cost": 550 },
      { "name": "JavaInn", "cost": 810 }
    ]
  },
  {
    "service": "book-king",
    "hotels": [
      { "name": "$phpInn", "cost": 15 },
      { "name": "JSInn", "cost": 11 },
      { "name": "python_inn", "cost": 9 },
      { "name": "JavaInn", "cost": 10.7 }
    ]
  },
  {
    "service": "airdnb",
    "hotels": [
      { "name": "$phpInn", "cost": 680 },
      { "name": "JSInn", "cost": 750 },
      { "name": "python_inn", "cost": 500 },
      { "name": "JavaInn", "cost": 810 }
    ]
  }
]
print(find_all_matches(data))