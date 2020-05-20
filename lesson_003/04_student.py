# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

money = educational_grant - expenses  #за первый безпроцентный месяц посчитали уже и будем считать за 9 месяцев
month= 1
while month <= 9:
    expenses_procent = expenses * 0.03
    expenses += expenses_procent
    money = money + educational_grant - expenses
    month += 1

money = -round(money,2)
print(f'Студенту надо попросить {money} рублей')
