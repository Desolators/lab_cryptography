import matplotlib.pyplot as plt
import numpy as np

# Параметры OFDM
num_subcarriers = 13
subcarrier_spacing = 2  # Гц
# Частотный диапазон
f_min = -20  # Гц
f_max = 20  # Гц
# Создание частотной оси
f = np.linspace(f_min, f_max, 1000)
# Создание спектра OFDM
ofdm_spectrum = np.zeros_like(f)
for i in range(num_subcarriers):
    subcarrier_freq = i * subcarrier_spacing
    ofdm_spectrum += np.sinc(f - subcarrier_freq)
# Линейный масштаб
plt.figure(figsize=(10, 5))
plt.subplot(211)
plt.plot(f, ofdm_spectrum)
plt.xlabel('Частота (Hz)')
plt.ylabel('Величина')
plt.title('OFDM спектр (Линейный масштаб)')
plt.grid(True)
# Логарифмический масштаб
plt.subplot(212)
plt.plot(f, 20 * np.log10(np.clip(ofdm_spectrum, a_min=1e-10, a_max=None)))
plt.xlabel('Частота (Hz)')
plt.ylabel('Величина (dB)')
plt.title('OFDM Spectrum (Логарифмический масштаб)')
plt.grid(True)
plt.tight_layout()
plt.show()
