# -*- coding: utf-8 -*-
import my_burger as food

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

print('Рецепт двойного чизбургера! Раскладываем все ингридиенты...')
food.bun()
food.beef()
food.pickle()
food.tomato()
food.cheese()
food.mayo()

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger
print('А вот рецепт моего личного бургера...')
food.bun()
food.chick()
food.tomato()
food.pickle()
food.mayo()
food.ketchup()


# зачет!
