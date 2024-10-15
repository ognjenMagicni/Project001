import plotly.express as px
import plotly.graph_objects as go

def drawGraph(propertyInfo):
    x = [0,1]
    y = [0,1000]
    fig_1000 = px.line(x = x, y = y)

    x = [0,1]
    y = [0,1500]
    fig_1500 = px.line(x = x, y = y)

    x = [0,1]
    y = [0,2000]
    fig_2000 = px.line(x = x, y = y)

    x = []
    y = []
    link = []
    color = []

    for property in propertyInfo:
        x.append(property[0][1])
        y.append(property[0][2])
        link.append(property[2])
        color.append(property[1][0])

    fig = px.scatter(x = x, y = y, color = color,text = [f"<a href='{link[i]}' target='_blank'>.</a>" for i in range(len(link))])
    
    fig_final = go.Figure()

    for trace in fig_1000:
        fig_final.add_trace(trace)
    for trace in fig_1500:
        fig_final.add_trace(trace)
    for trace in fig_2000:
        fig_final.add_trace(trace)
    for trace in fig:
        fig_final.add_trace(trace)

    fig_final.show()