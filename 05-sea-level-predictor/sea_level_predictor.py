import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Importa i dati
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Crea il grafico a dispersione (scatter plot)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b', label='Data')

    # 3. Crea la prima linea di best fit (usando tutti gli anni dal 1880 al 2050)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series([i for i in range(df['Year'].min(), 2051)])
    y_pred = res.slope * x_pred + res.intercept
    ax.plot(x_pred, y_pred, 'r', label='Best Fit Line (1880-2050)')

    # 4. Crea la seconda linea di best fit (usando solo dal 2000 al 2050)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred_recent = pd.Series([i for i in range(2000, 2051)])
    y_pred_recent = res_recent.slope * x_pred_recent + res_recent.intercept
    ax.plot(x_pred_recent, y_pred_recent, 'g', label='Best Fit Line (2000-2050)')

    # 5. Aggiungi etichette e titolo
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Salva e restituisci la figura (non modificare queste righe)
    fig.savefig('sea_level_plot.png')
    return fig
