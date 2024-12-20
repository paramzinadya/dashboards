import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Пример данных
data = {
    'clients': [1000, 1100, 1200, 1300, 1400],  # Общее количество клиентов
    'new_clients': [100, 150, 200, 250, 300],  # Новые клиенты за период
    'repeat_clients': [20, 40, 60, 80, 100],  # Повторные клиенты
    'total_orders': [1000, 1200, 1300, 1500, 1700],  # Общее количество заказов
    'visits': [5000, 5500, 6000, 6500, 7000],  # Число посещений сайта
    'total_revenue': [20000, 22000, 25000, 30000, 35000],  # Общий доход
}

# Создаем DataFrame
df = pd.DataFrame(data)

# Расчет показателей

# 1. Темп роста клиентской базы
df['growth_rate'] = df['new_clients'].pct_change() * 100  # Процентный рост

# 2. Частота повторных заказов
df['repeat_order_rate'] = df['repeat_clients'] / df['clients'] * 100  # Частота повторных заказов

# 3. Средний чек
df['average_check'] = df['total_revenue'] / df['total_orders']  # Средний чек

# 4. Конверсия посетителей в покупателей
df['conversion_rate'] = df['total_orders'] / df['visits'] * 100  # Конверсия

# Инициализация приложения Dash
app = dash.Dash(__name__)

# Макет для дашборда
app.layout = html.Div([
    html.H1("Дашборд по показателям бизнеса"),

    dcc.Graph(
        id='growth-rate-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df['growth_rate'], 'type': 'line', 'name': 'Темп роста клиентской базы'},
            ],
            'layout': {
                'title': 'Темп роста клиентской базы'
            }
        }
    ),

    dcc.Graph(
        id='repeat-order-rate-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df['repeat_order_rate'], 'type': 'line', 'name': 'Частота повторных заказов'},
            ],
            'layout': {
                'title': 'Частота повторных заказов'
            }
        }
    ),

    dcc.Graph(
        id='average-check-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df['average_check'], 'type': 'bar', 'name': 'Средний чек'},
            ],
            'layout': {
                'title': 'Средний чек'
            }
        }
    ),

    dcc.Graph(
        id='conversion-rate-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df['conversion_rate'], 'type': 'line',
                 'name': 'Конверсия посетителей в покупателей'},
            ],
            'layout': {
                'title': 'Конверсия посетителей в покупателей'
            }
        }
    ),
])

# Запуск сервера
if __name__ == '__main__':
    app.run_server(debug=True)
