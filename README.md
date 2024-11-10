# Курс по машинному обучению
Здесь собрана основная информация по курсу.

### Правила игры

Итоговая оценка за курс (по 10-бальной шкале) будет сформирована следующим образом:
$$Итог = mathround \left[ 5 \times \left(\frac{Баллы \ за \ ДЗ}{Макс. баллов \ за \ ДЗ} \times 0.3 + Kaggle \times 0.3 + \frac{Баллы \ за \ Лабы}{Макс. баллов \ за \ Лабы} \times 0.4\right) + BonusPoints \right] + Exam $$

#### Блокирующие условия

Если $\frac{Баллы \ за \ ДЗ}{Макс. баллов \ за \ ДЗ} < 0.3$ или $\frac{Баллы \ за \ Лабы}{Макс. баллов \ за \ Лабы} < 0.3$ или $Exam < 2$ то студент получает неуд. за курс.

### Контесты Kaggle и Лабораторные работы

| Название | Дедлайн     | Ссылка на Kaggle       | Ссылка для сдачи лабы | 
| :-------- | :------- | :------------------------- | :------ |
| Линейная регрессия | 6 октября 23:59 | [Kaggle](https://www.kaggle.com/t/66116668b7d04793854036005a0809bb)  | [Ссылка для сдачи](https://forms.gle/VenxQ1mNfUS7WgoK6) |
| Классификация | 10 ноября 23:59 | [Kaggle](https://www.kaggle.com/t/89b6443ba8c4852711f82130ef11ac27)  | [Ссылка для сдачи](https://forms.gle/WM2cMvgEwEM9jeRFA) |
| Нейросети | 22 декабря 23:59 |  | |

Оценка за каждый контест Kaggle формируется по критериям
- Преодоление бейзлайна на public - 1 балл
- Попадание в топ-50% на private - 1.5 балла
- Попадание в топ-30% на private - 2 балла
- Попадание в топ-15%  на private- 2.5 балла
- Попадание в топ-5% на private - 3 балла

следующим образом: $Kaggle_i = \frac{Лучший \ из \ выполненных \ критериев}{3}$

Итоговая оценка по всем контестам: $Kaggle = \frac{1}{3}(Kaggle_1 + Kaggle_2 + Kaggle_3)$

#### Оформление Лабораторной работы

Вы оформляете решение контеста в соответствии с шаблоном (доступен в корне репозитория). Форма для отправки .ipynb решений появится ближе к дедлайну.

Оценка за лабораторную работу ставится независимо от вашего положения в лидерборде Kaggle и выставляется ориентируясь на следующие критерии:

| Оценка | Критерий     | 
| :-------- | :------- | 
| 0 | Лабораторная работа не сдана или списана. | 
| 1 | В лабораторной работе присутствуют грубые ошибки. Приведенные выводы несодержательны. |
| 2 | Проведены простейшие эксперименты. Проведен простейший EDA. Выбор модели и ее параметров корректно обоснованы. Выводы содержат ошибки или необоснованы. |
| 3 | Проведен содержательный EDA. Данные корректно подготовлены для обучения. Проведены содержательные эксперименты. Выводы из экспериментов корректны и обоснованы. |
| 4 | Все, что в п.3, + проведены эксперименты с автоматическим подбором гиперпараметров. Для получения метрик используется кросс-валидация. Проведен feature-engineering, корректно используются техники аугментации данных. |
| 5 | Все, что в п.4, + соблюдены best-practices с семинаров, codestyle и рекомендуемая структура работы. Исследованы неочевидные приемы и техники. |

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
| Линейная регрессия | 29 сентября 23:59 | [Контест](https://contest.yandex.ru/contest/67582/enter/) |
| Метрики классификации | 13 октября 23:59 | [Контест](https://contest.yandex.ru/contest/68885/enter/)  |
| SVM | 27 октября 23:59 | [Контест](https://contest.yandex.ru/contest/68886/enter/) |
| Нейросети | 22 декабря 23:59 | |


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
| Записи лекций и семинаров | [Ссылка](https://drive.google.com/drive/folders/1J9TK_GWVvCVOA3C7SVtuCyDU0CDERXcs?usp=sharing) |
