#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:03:45 2024

@author: lbalieiro@lince.lab
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Dados
x = np.array([0.1, 0.2, 0.3, 0.4, 0.5])  # Deslocamento (m)
t = np.array([0.176, 0.356, 0.534, 0.714, 0.895])  # Intervalo de tempo (s)

# Plot dos pontos
plt.scatter(t, x, color='blue', label='Dados do experimento')

# Regressão linear
slope, intercept, _, _, _ = linregress(t, x)
t_range = np.linspace(min(t), max(t), 100)
x_fit = slope * t_range + intercept

# Plot da reta de melhor ajuste
plt.plot(t_range, x_fit, color='red', label='Reta de melhor ajuste')

# Configurações do gráfico
plt.xlabel('Tempo (s)')
plt.ylabel('Deslocamento (m)')
plt.title('Gráfico x=f(t)')
plt.legend()

# Mostrar o gráfico
plt.grid(True)
plt.show()

# Coeficientes angular e linear
print(f"Coeficiente angular (inclinação da reta): {slope}")
print(f"Coeficiente linear (intercepto da reta): {intercept}")
