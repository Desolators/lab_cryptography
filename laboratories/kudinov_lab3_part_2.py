import numpy 
import matplotlib.pyplot as pyplot
count_subcarriers = 13
subcarrier_spacing = 2
f_min = -20
f_max = 20
f = numpy.linspace(f_min, f_max, 1000)
ofdm_spectre = numpy.zeros_like(f)
for i in range(count_subcarriers):
    subcarrier_freq = i * subcarrier_spacing
    ofdm_spectre += numpy.sinc(f - subcarrier_freq)
pyplot.figure(figsize=(12, 8))
pyplot.subplot(211)
pyplot.plot(f, ofdm_spectre, color='blue')
pyplot.xlabel('Частота (Hz)')
pyplot.ylabel('Величина')
pyplot.title('OFDM спектр (Линейный масштаб)')
pyplot.grid(True)
pyplot.subplot(212)
pyplot.plot(f, 20 * numpy.log10(numpy.clip(ofdm_spectre, a_min=1e-10, a_max=None)), color='blue')
pyplot.xlabel('Частота (Hz)')
pyplot.ylabel('Величина (dB)')
pyplot.title('OFDM Spectrum (Логарифмический масштаб)')
pyplot.grid(True)
pyplot.tight_layout()
pyplot.show()
