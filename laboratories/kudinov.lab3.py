import numpy 
import matplotlib.pyplot as pyplot


def rect_wave(t, period):
    return numpy.where(numpy.logical_and(t >= -period / 4, t <= period / 4), 1, 0)


def model(period_1, period_2, duration, shift):
    t = numpy.linspace(-duration / 2, duration / 3, 2000)
    wave1 = rect_wave(t - shift, period_1)
    wave2 = rect_wave(t, period_2)
    inner_product = numpy.sum(wave1 * wave2)
    return inner_product


def orthogonal_rect_waves(period_1, period_2, duration, shift):
    result = model(period_1, period_2, duration, shift)
    if numpy.isclose(result, 0):
        print("Волны ортогональны")
    else:
        print("Волны не ортогональны")
    t = numpy.linspace(-duration / 4, duration / 6, 2000)
    wave1 = rect_wave(t - shift, period_1)
    wave2 = rect_wave(t, period_2)
    pyplot.figure(figsize=(10, 6))
    pyplot.subplot(211)
    pyplot.plot(t, wave1, color='black', linestyle='--', label=f'Волна 1 (период = {period_1})')
    pyplot.plot(t, wave2, color='blue', linestyle='-', label=f'Волна 2 (период = {period_2})')
    pyplot.xlabel('t')
    pyplot.ylabel('Амплитуда')
    pyplot.title('Ортогональные прямоугольные волны со сдвигом во времени')
    pyplot.legend()
    pyplot.grid(True)
    pyplot.subplot(212)
    product_wave = wave1 * wave2
    pyplot.plot(t, product_wave, color='red', linestyle='-', label='Результат')
    pyplot.xlabel('t')
    pyplot.ylabel('Амплитуда')
    pyplot.title('Ортогональные прямоугольные волны со сдвигом во времени')
    pyplot.legend()
    pyplot.grid(True)
    pyplot.tight_layout()
    pyplot.show()


period1 = 1
period2 = 2
duration_1 = 8
shift_1 = 0.5
result_1 = model(period1, period2, duration_1, shift_1)
print (f'Значение интеграла произведения волн: {result_1}')
orthogonal_rect_waves(period1, period2, duration_1, shift_1)
