import pandas as pd
import numpy as np
from numpy import mean
from numpy import std
import plotly.offline as offline
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

def regression(pos1, pos2, data):
    x = [] 
    y = []
    for i in data.iloc[:,pos1]:
        x.append(i)
    for j in data.iloc[:,pos2]:
        y.append(j)
    
    x = np.array(x)
    y = np.array(y)

    denominator = x.dot(x) - x.mean()*x.sum()
    a = (x.dot(y) - y.mean()*x.sum()) / denominator
    с = (y.mean()*x.dot(x) - x.mean()*x.dot(y)) / denominator

    yath = a*x + с
    return yath

def anomal(n,data):
    data_mean, data_std = mean(data[n]), std(data[n])
    cut_off = data_std * 3
    lower, upper = data_mean - cut_off, data_mean + cut_off
    outliers = [x for x in data[n] if x < lower or x > upper]
    print('аномальные числа "',n, '" : %d' % len(outliers))
    outliers_removed = [x for x in data[n] if x > lower and x < upper]
    print('нормальные числа "',n,'" : %d' % len(outliers_removed))
    return(len(outliers))

def graphics(data):
    fig1 = go.Figure()

    fig1.add_trace(go.Scatter(
            x = data['Амосов Михаил Иванович'], 
            y = data['Явка'],
            name = 'Амосов Михаил Иванович',
            mode = 'markers',
            marker_color='#18F018'))
    fig1.add_trace(go.Scatter(
            x = data['Амосов Михаил Иванович'],
            y = regression(12,18,data),
            marker_color='#18F018',
            name = 'Количество аномальных чисел распределения "Амосов Михаил Иванович" : %d' % anomal('Амосов Михаил Иванович',data)))

    fig1.add_trace(go.Scatter(
            x = data['Беглов Александр Дмитриевич'], 
            y = data['Явка'],
            name = 'Беглов Александр Дмитриевич',
            mode = 'markers',
            marker_color='#F01818',
            legendgroup="group2"))
    fig1.add_trace(go.Scatter(
            x = data['Беглов Александр Дмитриевич'], 
            y = regression(13,18,data),
            name = 'Количество аномальных чисел распределения "Беглов Александр Дмитриевич" : %d' % anomal('Беглов Александр Дмитриевич',data),
            marker_color='#F01818',
            legendgroup="group2"))

    fig1.add_trace(go.Scatter(
            x = data['Тихонова Надежда Геннадьевна'], 
            y = data['Явка'],
            name = 'Тихонова Надежда Геннадьевна',
            mode = 'markers',
            marker_color='#F018F0',
            legendgroup="group3"))
    fig1.add_trace(go.Scatter(
            x = data['Тихонова Надежда Геннадьевна'], 
            y = regression(14,18,data),
            name = 'Количество аномальных чисел распределения "Тихонова Надежда Геннадьевна" : %d' % anomal('Тихонова Надежда Геннадьевна',data),
            marker_color='#F018F0',
        legendgroup="group3"))
            
    fig1.update_layout(title='Зависимость количества голосов за кандидата от явки')
    fig1.write_html('Зависимость_количества_голосов_за_кандидата_от_явки.html', auto_open=True)



    fig2 = go.Figure()

    fig2.add_trace(go.Scatter(
            x = data['Явка'], 
            y = data['Число избирателей, внесенных в список избирателей на момент окончания голосования'], 
            name = 'Явка',
            mode = 'markers',
            marker_color='#18F018',
            legendgroup="group4"))
    fig2.add_trace(go.Scatter(
            x = data['Явка'],
            y = regression(18,1,data),
            marker_color='#18F018',
            name = 'Количество аномальных чисел распределения "Явка" : %d' % anomal('Явка',data),
            legendgroup="group4"))

    fig2.update_layout(title='Зависимость явки от количества избирателей на участке')
    fig2.write_html('Зависимость_явки_от_количества_избирателей_на_участке.html', auto_open=True)


    group_labels = ['Явка'] 
    x = [data['Явка']]
    fig = ff.create_distplot(x, group_labels, show_hist=False)
    fig.update_layout(title='Зависимость явки и количества избирательных участков')
    fig.write_html('Зависимость_явки_и_количества_избирательных_участков.html', auto_open=True)