import plotly.graph_objects as go

colors = ['#5b3e80', '#9b6ba9', '#9977b6', '#b4a6bf', '#d1aebf', '#ea96b9', '#ef9997',
          '#faa67b', '#efb99e', '#fa915c', '#bb7497', '#549fa3', '#547ca3', '#3776dc']

# Gráfico de barras
def graficas_barras(df, column_1, column_2, colors, title, xlabel, ylabel, orientation):
    fig = go.Figure(data=[
        go.Bar(
            x=df[column_1],  # Cambiar a valores del DataFrame
            y=df[column_2],  # Cambiar a valores del DataFrame
            orientation=orientation,
            marker=dict(color=colors, line=dict(color='black', width=0.5)),
        )
    ])
    
    fig.update_layout(
        title={
            'text': title,
            'font': {'family': 'Roboto', 'size': 24, 'color': 'black'},
            'x': 0.5, 'xanchor': 'center', 'yanchor': 'top', 'pad': {'b': 90}
        },
        xaxis_title={'text': xlabel, 'font': {'family': 'Roboto', 'size': 18, 'color': 'black'}},
        yaxis_title={'text': ylabel, 'font': {'family': 'Roboto', 'size': 18, 'color': 'black'}, 'standoff': 10},
        yaxis=dict(automargin=True),
        template='plotly_white',
        hoverlabel=dict(bgcolor="white", font_size=16, font_family="Roboto", font_color='black'),
        margin=dict(l=70, r=30, t=75, b=30),
        width=850,
        height=450
    )
    
    return fig

# Gráfico de barras apiladas
def graficas_barras_apiladas(df, name_legend_x, name_legend_y, column_1, column_2, column_3, title, xlabel, ylabel):
    fig = go.Figure(data=[
        go.Bar(name=name_legend_x, x=df[column_1], y=df[column_2], marker_color='#5b3e80'),
        go.Bar(name=name_legend_y, x=df[column_1], y=df[column_3], marker_color='#9b6ba9')
    ])
    
    fig.update_layout(
        title={
            'text': title,
            'font': {'family': 'Roboto', 'size': 24, 'color': 'black'},
            'x': 0.5, 'xanchor': 'center', 'yanchor': 'top', 'pad': {'b': 90}
        },
        xaxis_title={'text': xlabel, 'font': {'family': 'Roboto', 'size': 18, 'color': 'black'}},
        yaxis_title={'text': ylabel, 'font': {'family': 'Roboto', 'size': 18, 'color': 'black'}, 'standoff': 10},
        yaxis=dict(automargin=True),
        template='plotly_white',
        hoverlabel=dict(bgcolor="white", font_size=16, font_family="Roboto", font_color='black'),
        margin=dict(l=70, r=30, t=75, b=30),
        width=900,
        height=450
    )
    
    return fig

# Gráfico de barras agrupadas
def graficas_barras_agrupadas(df, legend_1, legend_2, legend_3, legend_4, legend_5, column_1, column_2, column_3, column_4, column_5, column_6, title, xlabel, ylabel):
    fig = go.Figure(data=[
        go.Bar(name=legend_1, x=df[column_1], y=df[column_2], marker_color='#fa915c'),
        go.Bar(name=legend_2, x=df[column_1], y=df[column_3], marker_color='#bb7497'),
        go.Bar(name=legend_3, x=df[column_1], y=df[column_4], marker_color='#549fa3'),
        go.Bar(name=legend_4, x=df[column_1], y=df[column_5], marker_color='#547ca3'),
        go.Bar(name=legend_5, x=df[column_1], y=df[column_6], marker_color='#3776dc')
    ])

    fig.update_layout(
        title={
            'text': title,
            'font': {'family': 'Roboto', 'size': 24, 'color': 'black'},
            'x': 0.5, 'xanchor': 'center', 'yanchor': 'top', 'pad': {'b': 90}
        },
        xaxis_title={'text': xlabel, 'font': {'family': 'Roboto', 'size': 18, 'color': 'black'}},
        yaxis_title={'text': ylabel, 'font': {'family': 'Roboto', 'size': 18, 'color': 'black'}, 'standoff': 10},
        yaxis=dict(automargin=True),
        template='plotly_white',
        hoverlabel=dict(bgcolor="white", font_size=16, font_family="Roboto", font_color='black'),
        margin=dict(l=70, r=30, t=75, b=30),
        width=900,
        height=450
    )
    
    return fig




