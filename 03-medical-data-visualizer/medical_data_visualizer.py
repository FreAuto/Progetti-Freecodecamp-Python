import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Importa i dati
df = pd.read_csv('medical_examination.csv')

# 2. Aggiungi la colonna 'overweight' (BMI > 25)
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3. Normalizza i dati: 0 se buono, 1 se cattivo (per cholesterol e gluc)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Funzione per il Categorical Plot
def draw_cat_plot():
    # 5. Crea il DataFrame in formato long con pd.melt
    df_cat = pd.melt(
        df, 
        id_vars=['cardio'], 
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    # 6. Raggruppa e ridenomina i dati per contare le occorrenze
    df_cat = pd.DataFrame(
        df_cat.groupby(['cardio', 'variable', 'value'])['value'].count()
    ).rename(columns={'value': 'total'}).reset_index()

    # 7. Disegna il grafico con catplot
    graph = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar',
        order=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
    )

    # 8. Ottieni la figura
    fig = graph.fig

    # 9. Non modificare queste righe (salvataggio automatico per i test)
    fig.savefig('catplot.png')
    return fig


# 10. Funzione per la Heat Map
def draw_heat_map():
    # 11. Pulisci i dati rimuovendo i valori anomali
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12. Calcola la matrice di correlazione
    corr = df_heat.corr()

    # 13. Genera la maschera per il triangolo superiore
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14. Imposta la figura di matplotlib
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15. Disegna la heatmap con seaborn
    sns.heatmap(
        corr, 
        mask=mask, 
        annot=True, 
        fmt='.1f', 
        square=True, 
        linewidths=.5, 
        cbar_kws={'shrink': 0.5}, 
        ax=ax
    )

    # 16. Non modificare queste righe (salvataggio automatico per i test)
    fig.savefig('heatmap.png')
    return fig
