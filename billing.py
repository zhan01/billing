balance = {
    'Alice': 100,
    'Bob': 100,
    'Charlie': 5000,
    'Eric': 50,
    'Fiona': 300
}

plans = {
    'cheap': 1,
    'average': 2,
    'expensive': 10
}

users = {
    'Alice': 'cheap',
    'Bob': 'average',
    'Charlie': 'expensive',
    'Fiona': 'cheap'
}

history = [
    {'Charlie': 50},
    {'Alice': 10},
    {'Alice': 20},
    {'Bob': 2},
    {'Eric': 15}
]

def calculate_balance(balance, history, users, plans):
    for conversion in history:
        user = list(conversion.keys())[0]
        user_tariff = users.get(user, 'cheap')
        balance[user] = balance[user] - (plans[user_tariff] * conversion[user])

    print(balance)

calculate_balance(balance, history, users, plans)