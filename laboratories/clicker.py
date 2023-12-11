from laboratories.libraries import click

key = 10
start_position = [0] * key
a = [0] * key

click.show_window("Дифференциальный криптоанализ")  # Дифференциальный/Линейный

for j in range(key):
    click.click_1(click.find_coords_x() + 39 + (28 * j),
                  click.find_coords_y() + 454)  # find_coords_y() + 388 (Линейный) + 454 (Дифф)

for k in range(2 ** (len(a))):
    j = len(a) - 1
    while j >= 0 and a[j] == 1:
        a[j] = 0
        click.double_click(click.find_coords_x() + 39 + (28 * j),
                           click.find_coords_y() + 454)  # find_coords_y() + 388 (Линейный) + 454 (Дифф)
        j -= 1
    if j >= 0 and a[j] == 0:
        a[j] = 1
        click.click_1(click.find_coords_x() + 39 + (28 * j),
                      click.find_coords_y() + 454)  # find_coords_y() + 388 (Линейный) + 454 (Дифф)
    click.window_checker("ошибка", "информация", click.find_coords_x() + 80,
                         click.find_coords_y() + 619)
    # window_checker find_coords_y() + 571 (Линейный) + 619 (Дифф)
