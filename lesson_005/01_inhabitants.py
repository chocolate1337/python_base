# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...
# TODO сделай импорты в разных строках, так легче читается
# TODO: как сделать импорт без lesson_005:
#  https://docs.google.com/document/d/1r4uqIEtQFG6JAGAX5YYOj8DCA55aI4b3iXtJNrENweU/edit#heading=h.cnqzbxwlfznx
from lesson_005 import room_1 as r1, room_2 as r2

print(f'В комнате room_1 живут: {r1.folks}')
print(f'В комнате room_2 живут: {r2.folks}')
