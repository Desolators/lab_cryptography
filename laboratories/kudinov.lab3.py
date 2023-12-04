import numpy 
import matplotlib.pyplot as pyplot


def orthogonal_rect_waves(period_1, period_2, duration, shift):
    result = model(period_1, period_2, duration, shift)
    if numpy.isclose(result, 0):
        print("Волны ортогональны")
    else:
        print("Волны не ортогональны")
    t = numpy.linspace(-duration / 4, duration / 4, 2000)
    wave1 = rect_wave(t - shift, period_1)
    wave2 = rect_wave(t, period_2)
    pyplot.figure(figsize=(10, 6))
    pyplot.subplot(211)
    pyplot.plot(t, wave1, color='black', linestyle='-', label=f'Волна 1 (период = {period_1})')
    pyplot.plot(t, wave2, color='blue', linestyle='--', label=f'Волна 2 (период = {period_2})')
    pyplot.title('Ортогональные прямоугольные волны со сдвигом во времени')
    pyplot.ylabel('Амплитуда')
    pyplot.xlabel('t')
    pyplot.legend()
    pyplot.grid(True)
    pyplot.subplot(212)
    wave1_wave2 = wave1 * wave2
    pyplot.plot(t, wave1_wave2, color='red', linestyle='-', label='Результат')
    pyplot.title('Ортогональные прямоугольные волны со сдвигом во времени')
    pyplot.ylabel('Амплитуда')
    pyplot.xlabel('t')
    pyplot.legend()
    pyplot.grid(True)
    pyplot.tight_layout()
    pyplot.show()


def model(period_1, period_2, duration, shift):
    t = numpy.linspace(-duration / 4, duration / 4, 2000)
    wave1 = rect_wave(t - shift, period_1)
    wave2 = rect_wave(t, period_2)
    wave1_wave2_ = numpy.sum(wave1 * wave2)
    return wave1_wave2_


def rect_wave(t, T):
    return numpy.where(numpy.logical_and(t >= -T / 4, t <= T / 4), 1, 0)


duration_1 = 8
shift_1 = 0.5
T1 = 1
T2 = 2
result_1 = model(T1, T2, duration_1, shift_1)
print (f'Значение интеграла произведения волн: {result_1}')
orthogonal_rect_waves(T1, T2, duration_1, shift_1)
