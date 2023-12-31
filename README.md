# Курс по машинному обучению
Здесь собрана основная информация по курсу.

### Правила игры

Итоговая оценка за курс (по 10-бальной шкале) будет сформирована следующим образом:
$$Итог = mathround \left[ 5 \times \left(\frac{Баллы \ за \ ДЗ}{Макс. баллов \ за \ ДЗ} \times 0.3 + Kaggle \times 0.3 + \frac{Баллы \ за \ Лабы}{Макс. баллов \ за \ Лабы} \times 0.4\right) + BonusPoints \right] + Exam $$

#### Блокирующие условия

Если $\frac{Баллы \ за \ ДЗ}{Макс. баллов \ за \ ДЗ} < 0.6$ или $\frac{Баллы \ за \ Лабы}{Макс. баллов \ за \ Лабы} < 0.4$ или $Exam < 2$ то студент получает неуд. за курс.

### Контесты Kaggle и Лабораторные работы

| Название | Дедлайн     | Ссылка на Kaggle       | Ссылка для сдачи лабы | 
| :-------- | :------- | :------------------------- | :------ |
| Линейная регрессия | 29 октября 23:59 | [Kaggle](https://www.kaggle.com/t/2820b6d8199b4bea9626cf57cfa3fd73) | [Фома для сдачи](https://forms.gle/seAJiJX2jnUcbXVt8) |
| Классификация | 3 декабря 23:59 | [Kaggle](https://www.kaggle.com/t/e372af0ac4064750aa12e874bd62a76b) | [Форма для сдачи](https://forms.gle/YUX62WP7F9QfBC6a6) |
| Нейросети | 7 января 23:59 | [Kaggle](https://www.kaggle.com/t/e96012d07a67422c8b017e5a3b6a6d79) | [Форма для сдачи](https://forms.gle/BTM9q47bJmjKTm4RA) | 

Оценка за каждый контест Kaggle формируется по критериям
- Преодоление бейзлайна на паблике - 1 балл
- Попадание в топ-15 - 1.5 балла
- Попадание в топ-10 - 2 балла
- Попадание в топ-5 - 2.5 балла
- Попадание в топ-3 - 3 балла

следующим образом: $Kaggle_i = \frac{Лучший \ из \ выполненных \ критериев}{3}$

Итоговая оценка по всем контестам: $Kaggle = \frac{1}{3}(Kaggle_1 + Kaggle_2 + Kaggle_3)$

#### Оформление Лабораторной работы

Вы оформляете решение контеста в соответствии с шаблоном (доступен в корне репозитория). Форма для отправки .ipynb решений появится ближе к дедлайну.

Оценка за лабораторную работу ставится независимо от вашего положения в лидерборде kaggle и варьируется от 0 до 5, где 0 - лаба не сдана или сделана неудовлетворительно, 5 - лаба сделана идеально с комментариями, графиками, выводами и т.д.

#### Регистрация на Kaggle
Если вы испытываете проблемы с регистрацией (не можете подтвердить номер телефона для отправки решений), [напишите в поддержку Kaggle](https://www.kaggle.com/contact#/account/activate/phone) — вам помогут. И прочитайте [вот этот тред](https://www.kaggle.com/discussions/general/13822).

#### Воспроизводимость решений
В первой ячейке (после импортов) вашего jupyter notebook с решением добавьте следующие строки:
```python
  my_seed = 12345 # любое целое число на ваш выбор
  random.seed(my_seed)
  np.random.seed(my_seed)
```

### Домашние задания (homeworks)
Проверяются автоматически в системе Яндекс.Контест. 
| Название | Дедлайн     | Ссылка                |
| :-------- | :------- | :------------------------- |
| Линейная регрессия | 01 октября 23:59 | [Контест 1](https://contest.yandex.ru/contest/52519/problems/)|
| Метрики классификации | 22 октября 23:59 | [Контест 2](https://contest.yandex.ru/contest/54112/problems/) |
| SVM | 5 ноября 23:59 | [Контест 3](https://contest.yandex.ru/contest/54500/problems/) |
| ~~Деревья~~ | __отменено__ | __отменено__ |
| Нейросети | 24 декабря 23:59 | [Контест 4](https://contest.yandex.ru/contest/54860/problems/) |


Плагиат будет караться аннулированием работы для всех причастных без возможности апелляции.

### Экзамен

Экзамен будет приниматься в устной форме. Экзаменационный билет будет состоять из двух или трех вопросов:

#### Вопрос 1 (2 балла)

Вопрос по теории. Может включать формулировки, выводы формул, доказательства, обоснования утверждений. Все по материалам лекций.

#### Вопрос 2 (3 балла)

Вопрос на рассуждение. Будет предложена задача из реального мира, как-то описаны данные и имеющиеся ресурсы. От студента требуется сформулировать задачу в терминах машинного обучения, предложить наилучшее на его взгляд решение, описать возможные проблемы и способы их устранения.

#### Вопрос по работе в семестре (-1 или 0 баллов)
Если у нас возникнут вопросы касательно авторства ваших ДЗ или Лаб, вы можете получить вопрос на понимание собственного кода / выводов в лабе и т.д. Если не отвечаете, то получаете $-1$ балл к оценке.

Если мы не сомневаемся в вашей добросовестности - вы не получаете этот вопрос. 

### Материалы

| Материал | Ссылка |
| :-------- | :------- |
| Записи лекций | [Ссылка](https://drive.google.com/drive/folders/1tl3O15BVU86Cx_Ql-B_u4ewM-g-obFug?usp=sharing)|
| Записи семинаров (Пермь) | [Ссылка](https://drive.google.com/drive/folders/1IIUTxlsSLnHLpWSU3aJqhFFRyqyazFc7?usp=sharing)|
| Записи семинаров (Рязань) | [Ссылка](https://drive.google.com/drive/folders/14v_lEpfInepXQADu4ZPpXFE5Q0scvH1v?usp=sharing)|
