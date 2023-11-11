from fastapi import FastAPI


app = FastAPI(
    title='Trading App'
)


users = [
    {'id': 1, 'role': 'admin', 'name': 'Bob'},
    {'id': 2, 'role': 'investor', 'name': 'John'},
    {'id': 3, 'role': 'trader', 'name': 'Matt'},
    {'id': 4, 'role': 'trader', 'name': 'Lucy'},
]


@app.get('/users/{user_id}')
def get_user(user_id: int):
    return [user for user in users if user.get('id') == user_id]


trades = [
    {'id': 1, 'user_id': 1, 'currency': 'BTC', 'side': 'buy', 'price': 123, 'amount': 2.12},
    {'id': 2, 'user_id': 1, 'currency': 'BTC', 'side': 'sell', 'price': 125, 'amount': 2.12}
]


@app.get('/trades')
def get_trades(limit: int = 1, offset: int = 0):
    return trades[offset:][:limit]


users_2 = [
    {'id': 1, 'role': 'admin', 'name': 'Bob'},
    {'id': 2, 'role': 'investor', 'name': 'John'},
    {'id': 3, 'role': 'trader', 'name': 'Matt'},
    {'id': 4, 'role': 'trader', 'name': 'Lucy'},
]


@app.post('/users/{user_id}')
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get('id') == user_id, users_2))[0]
    current_user['name'] = new_name
    return {'status': 200, 'data': current_user}