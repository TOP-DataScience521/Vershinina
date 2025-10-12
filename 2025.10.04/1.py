from numpy import array, corrcoef, isnan

# Данные об исследованиях
years_rd = array([2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022])
rd = array([
    277784757.3,352917701.2,410864983.6,461006216.0,489450798.7,568386749.7,
    655061743.4,699948879.0,795407850.6,854288043.8,873778705.8,950257084.9,
    960689437.2,1060560377.0,1091333468.1,1193578508.5,1322563915.0
])

# Данные доли больных (годы и значения)
years_c = array([2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023])
c = array([50.5,50.8,52.0,53.7,54.7,55.6,56.4,57.4,56.3,57.9,59.3,60.5])

def compute_correlation_for_shift(years1, vals1, years2, vals2, shift):
    """
    Сдвигаем второй ряд по годам на shift (years2 + shift),
    затем находим общие годы и вычисляем корреляцию Пирсона.
    Возвращаем: list_common_years, vals1_aligned_list, vals2_aligned_list, corr_or_nan
    """
    shifted_years2 = years2 + shift

 # Найдём общие годы 
    common_years = []
    for y in years1:
        if y in shifted_years2:
            common_years.append(int(y))

    if len(common_years) < 2:
        return common_years, [], [], float('nan')

    vals1_aligned = []
    vals2_aligned = []
    for y in common_years:
        idx1 = None
        for i in range(len(years1)):
            if int(years1[i]) == y:
                idx1 = i
                break
        original_year_for_second = y - shift
        idx2 = None
        for j in range(len(years2)):
            if int(years2[j]) == original_year_for_second:
                idx2 = j
                break

        if idx1 is not None and idx2 is not None:
            vals1_aligned.append(float(vals1[idx1]))
            vals2_aligned.append(float(vals2[idx2]))

    arr1 = array(vals1_aligned, dtype=float)
    arr2 = array(vals2_aligned, dtype=float)

    if arr1.size < 2:
        return common_years, vals1_aligned, vals2_aligned, float('nan')

    corr_matrix = corrcoef(arr1, arr2)
    corr = float(corr_matrix[0, 1])

    return common_years, vals1_aligned, vals2_aligned, corr

# Выбираем диапазон сдвигов
min_shift = -3
max_shift = 5

results = {}

print("Проверка корреляции для разных сдвигов (положительный сдвиг = сдвиг доли больных в будущее)")
print("*" * 80)

for shift in range(min_shift, max_shift + 1):
    common_years, aligned_rd, aligned_c, corr = compute_correlation_for_shift(
        years_rd, rd, years_c, c, shift
    )

    print("Сдвиг:", shift, "лет")

    if len(common_years) == 0:
        print("Нет совпадающих годов после сдвига.")
        print("*" * 80)
        results[shift] = (common_years, aligned_rd, aligned_c, corr)
        continue

    print("Общие годы:", common_years)

    rd_str = "[" + ", ".join("{:.2f}".format(x) for x in aligned_rd) + "]"
    c_str = "[" + ", ".join("{:.2f}".format(x) for x in aligned_c) + "]"
    print("Затраты на исследования:", rd_str)
    print("Доля больных (сдвинутая):", c_str)

    if isnan(corr):
        print("Коэффициент корреляции: не определён (мало точек или нулевая дисперсия)")
    else:
        print("Коэффициент корреляции:", "{:.4f}".format(corr))

    print("*" * 80)
    results[shift] = (common_years, aligned_rd, aligned_c, corr)

# Найдём лучший сдвиг по максимальному значению корреляции 
best_shift = None
best_corr = -2.0  

for s, data in results.items():
    corr = data[3]
    if not isnan(corr) and corr > best_corr:
        best_corr = corr
        best_shift = s

if best_shift is None:
    print("Не найдено ни одного сдвига с достаточным количеством точек для расчёта корреляции.")
else:
    print("Итоги:")
    print("Сдвиг с максимальной корреляцией:", best_shift, "лет, корреляция =", "{:.4f}".format(results[best_shift][3]))
