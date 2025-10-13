from pandas import read_csv
from numpy import array, corrcoef, linspace, intersect1d
from matplotlib import pyplot as plt
from datetime import datetime as dt, timedelta as td
from pathlib import Path 
from sys import path 
from locale import LC_ALL, setlocale

setlocale(LC_ALL, 'ru_RU')

oil_data_path = Path(path[0])/'urals_oil_rus_export_prices.csv'
oil_data = read_csv(oil_data_path, header=None, sep=' ')
dates1 = array([dt.strptime(d, '%d.%b.%y' ).date() for d in oil_data[0]])

dizel_data_path = Path(path[0])/'dizel_fuel_rus_prices.csv'
dizel_data = read_csv(dizel_data_path, header=None, sep=' ')
dates2 = array([dt.strptime(d, '%d.%b.%y' ).date() for d in dizel_data[0]])

# Берём второй столбец/строку с числовыми значениями напрямую
vals1 = array(oil_data[1], dtype=float)
vals2 = array(dizel_data[1], dtype=float)

def month_code(d):
    return d.year * 12 + d.month

mc1 = array([month_code(d) for d in dates1], dtype=int)
mc2 = array([month_code(d) for d in dates2], dtype=int)

# Диапазон сдвигов
shifts = range(-3, 5)  

results = []  

#в данном цикле использовала метод intersect1d. Честно признаюсь, спросила у ИИ про возможности numpy для поиска совп. пар
for k in shifts:
    shifted_mc2 = mc2 + k
    common, i1, i2 = intersect1d(mc1, shifted_mc2, return_indices=True)

    x = vals1[i1]
    y = vals2[i2]

    corr = float(corrcoef(x, y)[0, 1])

    results.append((k, x, y, corr))

    x_str = "  ".join(f"{v:.2f}" for v in x)
    y_str = "  ".join(f"{v:.2f}" for v in y)
    print(f"Сдвиг (мес) = {k}")
    print(f"  x : {x_str}")
    print(f"  y : {y_str}")
    print(f"  corr = {corr:.4f}\n")

# Выбор лучшего сдвига
best = max(results, key=lambda t: t[3])
best_k, best_x, best_y, best_corr = best
print(f"Выбранный сдвиг: {best_k} мес, пар: {best_x.size}, corr = {best_corr:.4f}")

# Регрессия y = a + b*x 
x = best_x.astype(float)
y = best_y.astype(float)

xm = x.mean() 
ym = y.mean()
# Оценка наклона (коэффициент при x) в модели y = a + b*x по методу наименьших квадратов
b = ((x - xm) * (y - ym)).sum() / ((x - xm) ** 2).sum()
a = ym - b * xm

print(f"Регрессия: y = {a:.4f} + {b:.4f} * x")


#  Построение и сохранение графика 
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', label='Данные')
x_line = linspace(x.min(), x.max(), 200)
plt.plot(x_line, a + b * x_line, color='red', label=f'y={a:.2f}+{b:.4f}x')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Сдвиг = {best_k} мес, corr = {best_corr:.4f}')
plt.legend()
plt.grid(True)

out_path = Path(path[0]) / 'regression_match_plot.png'
plt.savefig(str(out_path), dpi=300)
print(f"График сохранён: {out_path}")