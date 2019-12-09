
# testTask112019

python  command line utility ... test task for this year

## libraries

* [Click](https://click.palletsprojects.com/en/7.x/)
* [sqlalchemy](https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91)
* [alembic](https://alembic.sqlalchemy.org/)
* [jsonlines](https://jsonlines.readthedocs.io/en/latest/)

## Task description

* [Task 1](https://docs.google.com/document/d/1FwndaKyc3Ua8z0tJTnv34nf3Ass4VigaemGeGNDXkGA/edit?usp=sharing) unfinished

Task 2

*  кирпич весит 1 кг плюс половина от веса кирича -- сколько весит кирпич?
        [лучшее объяснение я нашел тут и на английском мне кажется текст задачи более понятным](http://jwilson.coe.uga.edu/EMT668/EMT668.Student.Folders/SeitzBrian/EMT669/brick.problem/halfbrick.html)
*  В массиве любого размера с целыми числами от 1 до 500,000 одно число повторяется дважды, все остальные числа уникальны. Предложите наиболее быстрый алгоритм поиска повторяющегося числа.
        [также линк на наиболее полное как по мне объяснение](https://habr.com/ru/post/167177/)
*  Смотря в небо три минуты вероятность заметить самолет составляет 60%. Определите вероятность заметить самолет за одну минуту и объясните решение.
        наиболее очевидный вариант с вероятностью меньше в 3 раза x=60*(1/3)  ... еще можно вспомнить [вероятность события](https://ru.wikipedia.org/wiki/%D0%92%D0%B5%D1%80%D0%BE%D1%8F%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C) но я не уверен что нужно именно это :)
* [напишите консольную программу которая будет обходить матрицу улиткой начиная с левого верхнего угла. На входе, параметрами 2 числа, размерность матрицы IxJ, на выходе список текущих координат для каждой посещенной точки. Например:  visit.py 3x3  0,0  0,1  0,2  1,2  2,2  2,1  2,0  1,0  1,1](./testtask112019/task2.py)
* [напишите консольную программу которая по заданному числу находит обратное ему бинарное число (13 => 1101, обратное ему (читаем справа налево) 1011 => 11). На входе параметром число N 1<= N <= 1000000000, на выходе обратное число    reverse_bin.py 13    11]((./testtask112019/task2.py))

## How to run

* install local libs `pipenv install`
* activate virtualenv|shell `pipenv shell`
* you need to run `docker-compose -f docker/postgresql.yaml`
* run db migrations `alembic upgrade head`
* then install in development mode `pip install -e .`
* and run `testtask112019 importdata --help` and `testtask112019 importdata --path <path to the folder with dada>`


### credits

This package was created with Cookiecutter_ and the `elgertam/cookiecutter-pipenv`_ project template, based on `audreyr/cookiecutter-pypackage`_.
