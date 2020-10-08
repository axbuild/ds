import io, base64, urllib, matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


# на вход поступает словарь с парами "метрика->данные"
def plot_to_png(data):
    plt.clf()                # очищаем то содержимое pyplot
    for key, value in data.items():
        plt.plot(value, label=key)        # добавляем данные
    buf = io.BytesIO()            # создаём буфер для данных
    plt.legend()
    plt.savefig(buf, format='png')    # выводим картинку в буфер
    buf.seek(0)                # позиционируемся на начало буфера
    return buf.read()            # возвращаем результат в виде строки