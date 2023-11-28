import pytest
KOSTROVOK_FEE = 0.12
BOOKKING_CONVERT_RATE = 75
from copy import deepcopy

def find_all_matching(data, values = {}):
    data = deepcopy(data)
    min_cost = values.get('min', float('-inf'))
    max_cost = values.get('max', float('inf'))
    kost_rate = lambda x: int(x + KOSTROVOK_FEE * x)
    book_rate  = lambda x: int(x * BOOKKING_CONVERT_RATE)
    result_list = []
    for x in data:
        for y in x['hotels']:
            if x['service'] == 'kostrovok':
                y['cost'] = kost_rate(y['cost'])
            elif x['service'] == 'book-king':
                y['cost'] = book_rate(y['cost'])
                
    for x in data:
        for y in x['hotels']:
            if min_cost < y['cost'] < max_cost:    
                result_list.append({
                    'service': x['service'], 
                    'hotel': {
                    'name': y['name'], 
                    'cost': y['cost']}})
    result = sorted(result_list, key=lambda x: x['hotel']['cost'])

    return result[0]
                
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
def find_the_cheapest_service(data, predicates=None):
    return find_all_matching(data, predicates)

def test_with_min_max(data):
    expected2 = {
        'hotel': {'cost': 672, 'name': '$phpInn'},
        'service': 'kostrovok'
        }
    predicates2 = {'min': 650, 'max': 700}
    predicates2 = {'min': 650, 'max': 700}
    result2 = find_all_matching(data, predicates2)
    assert result2 == expected2

def test_with_only_min(data):
    expected = {
        'hotel': {'cost': 802.5, 'name': 'JavaInn'},
        'service': 'book-king'
        }
    predicates = {'min': 800}
    result = find_the_cheapest_service(data, predicates)
    assert result == expected


def test_with_only_max(data):
    expected = {
        'hotel': {'cost': 500, 'name': 'python_inn'},
        'service': 'airdnb'
        }
    predicates = {'max': 570}
    result = find_the_cheapest_service(data, predicates)
    assert result == expected


def test_with_nothing(data):
    expected = {
        'hotel': {'cost': 500, 'name': 'python_inn'},
        'service': 'airdnb'
        }
    predicates = {}
    result = find_the_cheapest_service(data, predicates)
    assert result == expected
