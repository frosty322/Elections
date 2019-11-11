import sqlite3
import folium as fol
import pandas as pd

def color_change(turnout):
        if(turnout < 30):
            return('green')
        elif(30 <= turnout < 60):
            return('orange')
        else:
            return('red')

def popup_html(i, df, data):
        html = '<h5> УИК № {}</h5>'.format(df.iloc[i,0])
        html += '<br><b> Амосов Михаил Иванович </b>: {} %'.format(data.iloc[i,15])
        html += '<br><b> Беглов Александр Дмитриевич </b>: {} %'.format(data.iloc[i,16])
        html += '<br><b> Тихонова Надежда Геннадьевна </b>: {} %'.format(data.iloc[i,17])
        html += '<br><b> Явка </b>: {} %'.format(data.iloc[i,19])
        return html

def showMaps(data):
    conn = sqlite3.connect("mydatabase_2.db")
    df = pd.read_sql("SELECT * FROM coordinates", conn) 
       
    map = fol.Map(location=[59.976040,30.45], 
                 tiles= 'cartodbpositron',
                 zoom_start = 11.5)

    tooltip = 'Click me!'

    for i in range(data.shape[0]):
        fol.Marker(location=[df.iloc[i+65,1],df.iloc[i+65,2]],
                  popup = fol.Popup(popup_html(i, df, data), max_width=700, height=250),
                  icon=fol.Icon(color = color_change(data.iloc[i,19]), icon='cloud')).add_to(map)
    
    map.save("Результаты_выборов.html")
