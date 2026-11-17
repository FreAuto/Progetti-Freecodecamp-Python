import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Importa i dati (imposta 'date' come indice)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Pulisci i dati filtrando i giorni nel top 2.5% e nel bottom 2.5%
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

def draw_line_plot():
    # Crea una copia del dataframe per il grafico a linee
    df_line = df.copy()

    # Disegna il grafico a linee
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df_line.index, df_line['value'], color='r', linewidth=1)
    
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Salva e restituisci la figura
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Prepara i dati per il grafico a barre raggruppate per anno e mese
    df_bar = df.copy()
    df_bar['Year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.month_name()

    # Raggruppa per anno e mese calcolando la media
    df_bar = df_bar.groupby(['Year', 'Month'])['value'].mean().unstack()

    # Ordina i mesi correttamente
    month_order = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    df_bar = df_bar[month_order]

    # Disegna il grafico a barre
    fig = df_bar.plot(kind='bar', figsize=(15, 10), legend=True).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=month_order)
    plt.xticks(rotation=90)

    # Salva e restituisci la figura
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepara i dati per i box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['Year'] = df_box['date'].dt.year
    df_box['Month'] = df_box['date'].dt.strftime('%b')
    
    # Ordine dei mesi per la stagionalità
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Disegna i box plots affiancati
    fig, axes = plt.subplots(1, 2, figsize=(20, 7))

    # Year-wise Box Plot (Trend)
    sns.boxplot(x='Year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Month-wise Box Plot (Seasonality)
    sns.boxplot(x='Month', y='value', data=df_box, order=month_order, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Salva e restituisci la figura
    fig.savefig('box_plot.png')
    return fig
