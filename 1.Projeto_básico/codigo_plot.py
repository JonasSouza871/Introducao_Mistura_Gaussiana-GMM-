import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# DADOS DE ALTURA
alturas = np.array([165, 182, 168, 178, 171])

# PARÂMETROS INICIAIS
pesos_misturas = [0.5, 0.5]          # Pesos das misturas
medias = [167, 180]                  # Médias iniciais
desvios_padrao = [np.sqrt(25), np.sqrt(25)]  # Desvios padrão

# FUNÇÃO PARA CALCULAR AS RESPONSABILIDADES EM UM INTERVALO DE ALTURAS
def calcular_responsabilidades_intervalo(intervalo_alturas, pesos, medias, desvios):
    probabilidades = np.zeros((len(intervalo_alturas), 2))
    for i in range(2):
        probabilidades[:,i] = pesos[i] * norm.pdf(intervalo_alturas, medias[i], desvios[i])
    responsabilidades = probabilidades / probabilidades.sum(axis=1, keepdims=True)
    return responsabilidades

# GERAR UM INTERVALO DE ALTURAS ENTRE 160 E 200 CM
intervalo_alturas = np.linspace(160, 200, 400)
responsabilidades_intervalo = calcular_responsabilidades_intervalo(intervalo_alturas, pesos_misturas, medias, desvios_padrao)

# CRIAR O GRÁFICO
plt.figure(figsize=(12, 6))
plt.plot(intervalo_alturas, responsabilidades_intervalo[:,0], label='Grupo 1 (Adolescentes)', color='blue', linewidth=2)
plt.plot(intervalo_alturas, responsabilidades_intervalo[:,1], label='Grupo 2 (Adultos)', color='red', linewidth=2)

# ADICIONAR LINHAS VERTICAIS NAS MÉDIAS INICIAIS
plt.axvline(medias[0], color='blue', linestyle='--', alpha=0.5, label=f'Média Adolescentes ({medias[0]} cm)')
plt.axvline(medias[1], color='red', linestyle='--', alpha=0.5, label=f'Média Adultos ({medias[1]} cm)')

# DESTACAR OS DADOS ORIGINAIS
for altura in alturas:
    plt.axvline(altura, color='black', linestyle=':', alpha=0.4)

# CONFIGURAÇÕES DO GRÁFICO
plt.title('Comportamento das Responsabilidades por Altura', fontsize=14)
plt.xlabel('Altura (cm)', fontsize=12)
plt.ylabel('Responsabilidade (γ)', fontsize=12)
plt.xticks(np.arange(160, 201, 5))
plt.ylim(0, 1)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show() 