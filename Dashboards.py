import pandas as pd
import dash
from dash import dcc, html
from dash import dash_table
from dash.dependencies import Input, Output

# Пример данных (увеличиваем количество данных и добавляем категорию покупок)
data = {
    'clients': [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900],  # Общее количество клиентов
    'new_clients': [100, 150, 200, 250, 300, 350, 400, 450, 500, 600],  # Новые клиенты за период (возрастают)
    'repeat_clients': [20, 40, 60, 80, 100, 120, 140, 160, 180, 200],  # Повторные клиенты
    'total_orders': [1000, 1200, 1300, 1500, 1700, 1800, 1900, 2100, 2200, 2400],  # Общее количество заказов
    'visits': [5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500],  # Число посещений сайта
    'total_revenue': [20000, 22000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000],  # Общий доход
    # Добавление новых категорий покупок
    'sports_nutrition': [300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],  # Спортивное питание
    'healthy_nutrition': [200, 250, 300, 350, 400, 450, 500, 550, 600, 650],  # Правильное питание
    'weight_loss_nutrition': [100, 150, 200, 250, 300, 350, 400, 450, 500, 550],  # Питание для похудения
    'sugar_free_nutrition': [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],  # Питание без сахара
}

# Создаем DataFrame
df = pd.DataFrame(data)

# Расчет показателей
df['growth_rate'] = df['new_clients'].pct_change() * 100  # Процентный рост
df['repeat_order_rate'] = df['repeat_clients'] / df['clients'] * 100  # Частота повторных заказов
df['average_check'] = df['total_revenue'] / df['total_orders']  # Средний чек
df['conversion_rate'] = df['total_orders'] / df['visits'] * 100  # Конверсия

# Инициализация приложения Dash
app = dash.Dash(__name__)

# Макет для дашборда
app.layout = html.Div([
    html.H1("Дашборд по показателям бизнеса", style={'textAlign': 'center', 'marginTop': '30px'}),

    # Контейнер для показателей
    html.Div([
        # 1-й показатель: Темп роста клиентской базы
        html.Div([
            html.H3("Темп роста клиентской базы", style={'textAlign': 'center', 'marginTop': '20px'}),
            html.Div([
                html.Div([
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
                ], style={'flex': 1, 'padding': '10px', 'width': '50%'}),  # График слева
                html.Div([
                    dash_table.DataTable(
                        id='growth-rate-table',
                        columns=[{'name': col, 'id': col} for col in df[['new_clients', 'growth_rate']].columns],
                        data=df[['new_clients', 'growth_rate']].to_dict('records'),
                        style_table={'height': '300px', 'overflowY': 'auto'},
                        style_cell={'height': '60px'},  # Настроим высоту ячеек
                    ),
                ], style={'flex': 1, 'padding': '10px', 'width': '50%'}),  # Таблица справа
            ], style={'display': 'flex', 'justifyContent': 'space-between', 'alignItems': 'flex-start'}),
        ], style={'marginBottom': '50px'}),  # Отступ снизу

        # 2-й показатель: Частота повторных заказов
        html.Div([
            html.H3("Частота повторных заказов", style={'textAlign': 'center', 'marginTop': '20px'}),
            html.Div([
                html.Div([
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
                ], style={'flex': 1, 'padding': '10px', 'width': '50%'}),  # График слева
                html.Div([
                    dash_table.DataTable(
                        id='repeat-order-rate-table',
                        columns=[{'name': col, 'id': col} for col in df[['repeat_clients', 'repeat_order_rate']].columns],
                        data=df[['repeat_clients', 'repeat_order_rate']].to_dict('records'),
                        style_table={'height': '300px', 'overflowY': 'auto'},
                        style_cell={'height': '60px'},  # Настроим высоту ячеек
                    ),
                ], style={'flex': 1, 'padding': '10px', 'width': '50%'}),  # Таблица справа
            ], style={'display': 'flex', 'justifyContent': 'space-between', 'alignItems': 'flex-start'}),
        ], style={'marginBottom': '50px'}),  # Отступ снизу

        # 3-й показатель: Средний чек
        html.Div([
            html.H3("Средний чек", style={'textAlign': 'center', 'marginTop': '20px'}),
            html.Div([
                html.Div([
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
                ], style={'flex': 1, 'padding': '10px', 'width': '50%'}),  # График слева
                html.Div([
                    dash_table.DataTable(
                        id='average-check-table',
                        columns=[{'name': col, 'id': col} for col in df[['total_revenue', 'average_check']].columns],
                        data=df[['total_revenue', 'average_check']].to_dict('records'),
                        style_table={'height': '300px', 'overflowY': 'auto'},
                        style_cell={'height': '60px'},  # Настроим высоту ячеек
                    ),
                ], style={'flex': 1, 'padding': '10px', 'width': '50%'}),  # Таблица справа
            ], style={'display': 'flex', 'justifyContent': 'space-between', 'alignItems': 'flex-start'}),
        ], style={'marginBottom': '50px'}),  # Отступ снизу

        # 4-й показатель: Конверсия посетителей в покупателей
        html.Div([
            html.H3("Конверсия посетителей в покупателей", style={'textAlign': 'center', 'marginTop': '20px'}),
            html.Div([
                html.Div([
                    dcc.Graph(
                        id='conversion-rate-graph',
                        figure={
                            'data': [
                                {'x': df.index, 'y': df['conversion_rate'], 'type': 'line', 'name': 'Конверсия посетителей в покупателей'},
                            ],
                            'layout': {
                                'title': 'Конверсия посетителей в покупателей'
                            }
                        }
                    ),
                ], style={'flex': 1, 'padding': '10px', 'width': '50%'}),  # График слева
                html.Div([
                    dash_table.DataTable(
                        id='conversion-rate-table',
                        columns=[{'name': col, 'id': col} for col in df[['visits', 'conversion_rate']].columns],
                        data=df[['visits', 'conversion_rate']].to_dict('records'),
                        style_table={'height': '300px', 'overflowY': 'auto'},
                        style_cell={'height': '60px'},  # Настроим высоту ячеек
                    ),
                ], style={'flex': 1, 'padding': '10px', 'width': '50%'}),  # Таблица справа
            ], style={'display': 'flex', 'justifyContent': 'space-between', 'alignItems': 'flex-start'}),
        ], style={'marginBottom': '50px'}),  # Отступ снизу

        # 5-й показатель: Процентное соотношение покупок по категориям
        html.Div([
            html.H3("Процентное соотношение покупок по категориям", style={'textAlign': 'center', 'marginTop': '20px'}),
            html.Div([
                # Круговая диаграмма
                html.Div([
                    dcc.Graph(
                        id='category-purchase-pie-chart',
                        figure={
                            'data': [
                                {
                                    'labels': ['Спортивное питание', 'Правильное питание', 'Питание для похудения', 'Питание без сахара'],
                                    'values': [
                                        df['sports_nutrition'].sum(),
                                        df['healthy_nutrition'].sum(),
                                        df['weight_loss_nutrition'].sum(),
                                        df['sugar_free_nutrition'].sum(),
                                    ],
                                    'type': 'pie',
                                    'name': 'Категории покупок',
                                },
                            ],
                            'layout': {
                                'title': 'Процентное соотношение покупок по категориям'
                            }
                        }
                    ),
                ], style={'flex': 1, 'padding': '10px', 'width': '50%'}),  # Круговая диаграмма слева

                # Таблица с данными
                html.Div([
                    dash_table.DataTable(
                        id='category-purchase-table',
                        columns=[
                            {'name': 'Категория', 'id': 'category'},
                            {'name': 'Количество покупок', 'id': 'purchases'},
                        ],
                        data=[
                            {'category': 'Спортивное питание', 'purchases': df['sports_nutrition'].sum()},
                            {'category': 'Правильное питание', 'purchases': df['healthy_nutrition'].sum()},
                            {'category': 'Питание для похудения', 'purchases': df['weight_loss_nutrition'].sum()},
                            {'category': 'Питание без сахара', 'purchases': df['sugar_free_nutrition'].sum()},
                        ],
                        style_table={'height': '300px', 'overflowY': 'auto'},
                        style_cell={'height': '60px'},  # Настроим высоту ячеек
                    ),
                ], style={'flex': 1, 'padding': '10px', 'width': '50%'}),  # Таблица справа
            ], style={'display': 'flex', 'justifyContent': 'space-between', 'alignItems': 'flex-start'}),
        ], style={'marginBottom': '50px'}),  # Отступ снизу

    ])
])

# Запуск сервера
if __name__ == '__main__':
    app.run_server(debug=True)
