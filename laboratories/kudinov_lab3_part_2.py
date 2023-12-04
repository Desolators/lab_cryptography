import numpy 
import matplotlib.pyplot as pyplot


def create_ofdm():
    count_subcarriers, subcarrier_spacing, f_max, f_min = 13, 2, 20, -20
    f = numpy.linspace(f_min, f_max, 1000)
    return subcarrier_spacing, count_subcarriers, f


def create_spectre_odfm():
    subcarrier_spacing, count_subcarriers, f = create_ofdm()
    ofdm_spectre = numpy.zeros_like(f)
    for i in range(count_subcarriers):
        subcarrier_freq = i * subcarrier_spacing
        ofdm_spectre += numpy.sinc(f - subcarrier_freq)
        return ofdm_spectre, f


def create_plots():
    ofdm_spectre, f = create_spectre_odfm()
    pyplot.figure(figsize=(10, 5))
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


create_ofdm()
create_plots()
