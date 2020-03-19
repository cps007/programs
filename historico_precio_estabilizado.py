# -*- coding: utf-8 -*-
"""
Gráfico precio stabilizado vs costo marginal
Christian Perigault
(c) Febrero 14 2020
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Inicialización
pd.plotting.register_matplotlib_converters()

# Parámetros
archivo_datos_cmg  = "/home/cps007/PMG/cmg 2015 - 2019.csv"
archivo_datos_nudo = "/home/cps007/PMG/precios de nudo 2015 - 2019.csv"
directorio_salida  = "/home/cps007/PMG/"

separador     = ";"

# Datos
df_cmg  = pd.read_csv(archivo_datos_cmg,sep=separador)
fechas  = pd.to_datetime(dict(year=df_cmg.año, month=df_cmg.mes, day=df_cmg.día, hour=df_cmg.hora))
barras  = df_cmg.keys()[5:]

df_nudo            = pd.read_csv(archivo_datos_nudo,sep=separador)
fechas_nudo        = pd.to_datetime(df_nudo['fecha'])
fechas_nudo_inicio = pd.to_datetime(df_nudo['inicio'])
fechas_nudo_fin    = pd.to_datetime(df_nudo['fin'])



# Inicialización gráficos
for barra in barras:
    print("Graficando barra: "+barra)
    fig = plt.figure(figsize=(15, 8.5))
    ax  = fig.add_subplot(111)
    ax.set(title='Hourly CMg ' + barra + ' (2015-2019)', ylabel='US$/MWh', xlabel='hour')
    ax.set_ylim(top=200)
    ax.set_xlim(left=pd.Timestamp('2015-01-01 00:00:00'), right=pd.Timestamp('2019-12-31 23:00:00'))

    # Grafica
    ax.scatter(fechas, df_cmg[barra],color = 'deepskyblue', s= 5, alpha = 0.05)
    p_nudo = df_nudo[barra]
    for i in range(len(df_nudo)):
        ax.plot([fechas_nudo_inicio[i], fechas_nudo_fin[i]],[p_nudo[i],p_nudo[i]], color = 'red' )

    # Eje x
    ax.set_xlabel("Year")
    fig.savefig(directorio_salida + barra + ".png", dpi=600)