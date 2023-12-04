import numpy as np
import matplotlib.pyplot as plt
def rect_wave(t, period):
    return np.where(np.logical_and(t >= -period/4, t <= period/4), 1, e)
def compute_inner_product(period1, period2, duration, shift):
    t = np.linspace(-duration/2, duration/2, 1000)
    wave1 = rect_wave(t - shift, period1)
    wave2 = rect_wave(t, period2)
    inner_product = np.sum(wave1 * wave2)
    return inner_product
def orthogonal_rect_waves(period1, period2, duration, shift):
    inner_product = compute_inner_product(period1, period2, duration, shift)
    if np.isclose(inner_product, 0):
        print("Волны ортогональны")
        linestyle = '--'
    else:
        print("Волны не ортогональны")
        linestyle = '--'
    t = np.linspace(-duration / 2, duration / 2, 1000)
    wave1 = rect_wave(t - shift, period1)
    wave2 = rect_wave(t, period2)
    plt.figure(figsize=(10, 6))
    plt.subplot(211)
    plt.plot(t, wave1, color='blue', linestyle=linestyle, label=f'Wave 1 (period = {period1})
    plt.plot(t, wave2, color='red', linestyle=linestyle, label=f'Wave 2 (period = {period2})
    plt.xlabel('t')
    plt.ylabel('Amplitude')
    plt.title('Orthogonal Rectangular Waves with Time Shift')
    plt.legend()
    plt.grid(True)
    plt.subplot(212)
    product_wave = wave1 * wave2
    plt.plot(t, product_wave, color='green', linestyle='-', label='Product of Waves')
    plt.xlabel('t')
    plt.ylabel('Amplitude')
    plt.title('Orthogonal Rectangular Waves with Time Shift')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

