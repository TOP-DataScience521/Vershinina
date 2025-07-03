Запросы к таблице country:

1. Вывести названия всех стран Евразии
select name 
from country 
where continent in ('Europe', 'Asia');

2. Вывести названия регионов и стран, в которых ожидаемая продолжительность жизни меньше пятидесяти лет
select name, region 
from country 
where lifeexpectancy < 50;

3. Вывести название самой крупной по площади страны Африки
select name, surfacearea 
from country 
where continent = 'Africa' 
order by surfacearea desc 
limit 1;
 
4. Вывести названия пяти азиатских стран с самой низкой плотностью населения
select name 
from country 
where continent = 'Asia' 
order by population 
limit 5;

Запросы к таблице city:

5. Вывести в порядке возрастания населения коды стран и названия городов, 
численность населения которых превышает пять миллионов человек
select name, countrycode 
from city 
where population > 5000000 
order by population;

6. Вывести название города в Индии с самым длинным названием
select name
from city
where countrycode = 'IND'
order by char_length(Name) desc
limit 1;