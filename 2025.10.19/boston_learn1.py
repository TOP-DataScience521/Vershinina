from pandas import read_csv
from sklearn.linear_model import LinearRegression

from pathlib import Path
from sys import path


script_dir = Path(path[0])

data = read_csv(script_dir / 'boston.csv', comment='#')

# >>> data.shape
# (506, 14)

# отобранные зависимые переменные
effect_vars = ['CRIM', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'PTRATIO', 'LSTAT']
# целевая переменная
target_var = ['MEDV']

# маска для фильтрации значений
mask = data['MEDV'] != 50

x = data.loc[mask, effect_vars]
y = data.loc[mask, target_var]

# >>> x.shape
# (490, 9)
# >>> y.shape
# (490, 1)


# формирование обучающей и тестовой подвыборок
#ИЗМЕНИЛА ОБЪЕМ ТЕСТОВОЙ ВЫБОКИ В БОЛЬШУЮ СТОРОНУ
test_rate = 0.40
i = int(x.shape[0]*(1-test_rate))

x_train, x_test = x.iloc[:i, :], x.iloc[i:, :]
y_train, y_test = y.iloc[:i, :], y.iloc[i:, :]

# СООТВЕТСТВЕННОЙ РАЗМЕР ВЫБОРОК ДЛЯ ОБУЧЕНИЯ И ДЛЯ ТЕСТА ТОЖЕ ИЗМЕНИЛИСЬ
# >>> x_train.shape, y_train.shape
# ((294, 9), (294, 1))
# >>>
# >>> x_test.shape, y_test.shape
# (((196, 9), (196, 1))


# уравнение функции нескольких переменных для множественной линейной регрессии
# y(x1, x2, x3, x4, x5, x6, x7, x8, x9) = a1*x1 + a2*x2 + a3*x3 + a4*x4 + a5*x5 + a6*x6 + a7*x7 + a8*x8 + a9*x9 + b

# a1, a2, a3, a4, a5, a6, a7, a8, a9, b — это коэффициенты, которые необходимо подобрать, что и происходит во время обучения модели

model = LinearRegression()

# обучение модели
model.fit(x_train, y_train)

# ИЗМЕНИЛИСЬ ЗНАЧЕНИЯ КОЭФФИЦИЕНТОВ- МНОЖИТЕЛЕЙ (В СРЕДНЕМ В 1,5-2 РАЗА ПО СРАВНЕНИЮ СО ЗНАЧЕНИЯМИ, ПОЛУЧЕННЫМИ ПРИ test_rate=0.2)
# значения коэффициентов-множителей (в примере выше: a1, a2, ..., a9)
# >>> model.coef_
# array([[-0.33128087, -0.10434137,  0.70004857, -4.71317505,  8.48275086,
        # -0.05400363, -0.93649746, -0.6283542 , -0.07235017]])

# А КОЭФФИЦИЕНТ-СЛАГАЕМОГО ИЗМЕНИЛСЯ БОЛЕЕ ЧЕМ В 3 РАЗА
# значение коэффициента-слагаемого (в примере выше: b)
# >>> model.intercept_
# array([-6.64988614])


# тестирование модели
y_pred = model.predict(x_test)

# >>> y_pred.shape
# (196, 1)

# метрики:
# среднеквадратичная ошибка
rmse = (((y_test - y_pred)**2).sum() / len(y_test))**0.5
# коэффициент детерминации
r2 = 1 - ((y_test - y_pred)**2).sum() / (((y_test - y_test.mean())**2).sum())
# скорректированный коэффициент детерминации
r2_adj = 1 - (1 - r2)*(x_test.shape[0] - 1) / (x_test.shape[0] - x_test.shape[1] - 1)

print(f'RMSE = {rmse.iloc[0]:.1f}\nR2 = {r2.iloc[0]:.0%}\nR2 (adjusted) = {r2_adj.iloc[0]:.0%}')

# RMSE = 6.6
# R2 = -25%
# R2 (adjusted) = -31%

# При увеличении тестоой выборки до 40% (и соответственно уменьшение обучающей выбоки) произошло существенное ухудшение показателей технических метрик. Мы наблюдаем существенное ухудшение
# работы модели. 

