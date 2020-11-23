# -*- coding: utf-8 -*-

# Подземелье было выкопано ящеро-подобными монстрами рядом с аномальной рекой, постоянно выходящей из берегов.
# Из-за этого подземелье регулярно затапливается, монстры выживают, но не герои, рискнувшие спуститься к ним в поисках
# приключений.
# Почуяв безнаказанность, ящеры начали совершать набеги на ближайшие деревни. На защиту всех деревень не хватило
# солдат и вас, как известного в этих краях героя, наняли для их спасения.
#
# Карта подземелья представляет собой json-файл под названием rpg.json. Каждая локация в лабиринте описывается объектом,
# в котором находится единственный ключ с названием, соответствующем формату "Location_<N>_tm<T>",
# где N - это номер локации (целое число), а T (вещественное число) - это время,
# которое необходимо для перехода в эту локацию. Например, если игрок заходит в локацию "Location_8_tm30000",
# то он тратит на это 30000 секунд.
# По данному ключу находится список, который содержит в себе строки с описанием монстров а также другие локации.
# Описание монстра представляет собой строку в формате "Mob_exp<K>_tm<M>", где K (целое число) - это количество опыта,
# которое получает игрок, уничтожив данного монстра, а M (вещественное число) - это время,
# которое потратит игрок для уничтожения данного монстра.
# Например, уничтожив монстра "Boss_exp10_tm20", игрок потратит 20 секунд и получит 10 единиц опыта.
# Гарантируется, что в начале пути будет две локации и один монстр
# (то есть в коренном json-объекте содержится список, содержащий два json-объекта, одного монстра и ничего больше).
#
# На прохождение игры игроку дается 123456.0987654321 секунд.
# Цель игры: за отведенное время найти выход ("Hatch")
#
# По мере прохождения вглубь подземелья, оно начинает затапливаться, поэтому
# в каждую локацию можно попасть только один раз,
# и выйти из нее нельзя (то есть двигаться можно только вперед).
#
# Чтобы открыть люк ("Hatch") и выбраться через него на поверхность, нужно иметь не менее 280 очков опыта.
# Если до открытия люка время заканчивается - герой задыхается и умирает, воскрешаясь перед входом в подземелье,
# готовый к следующей попытке (игра начинается заново).
#
# Гарантируется, что искомый путь только один, и будьте аккуратны в рассчетах!
# При неправильном использовании библиотеки decimal человек, играющий с вашим скриптом рискует никогда не найти путь.
#
# Также, при каждом ходе игрока ваш скрипт должен запоминать следущую информацию:
# - текущую локацию
# - текущее количество опыта
# - текущие дату и время (для этого используйте библиотеку datetime)
# После успешного или неуспешного завершения игры вам необходимо записать
# всю собранную информацию в csv файл dungeon.csv.
# Названия столбцов для csv файла: current_location, current_experience, current_date
#
#
# Пример взаимодействия с игроком:
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло времени: 00:00
#
# Внутри вы видите:
# — Вход в локацию: Location_1_tm1040
# — Вход в локацию: Location_2_tm123456
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали переход в локацию Location_2_tm1234567890
#
# Вы находитесь в Location_2_tm1234567890
# У вас 0 опыта и осталось 0.0987654321 секунд до наводнения
# Прошло времени: 20:00
#
# Внутри вы видите:
# — Монстра Mob_exp10_tm10
# — Вход в локацию: Location_3_tm55500
# — Вход в локацию: Location_4_tm66600
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали сражаться с монстром
#
# Вы находитесь в Location_2_tm0
# У вас 10 опыта и осталось -9.9012345679 секунд до наводнения
#
# Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!
#
# У вас темнеет в глазах... прощай, принцесса...
# Но что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег :)
# Ну, на этот-то раз у вас все получится! Трепещите, монстры!
# Вы осторожно входите в пещеру... (текст умирания/воскрешения можно придумать свой ;)
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло уже 0:00:00
# Внутри вы видите:
#  ...
#  ...
#
# и так далее...
import json
import re
import time
from decimal import Decimal
from datetime import datetime
from collections import OrderedDict
from termcolor import colored
HATCH_EXP = 280

remaining_time = '123456.0987654321'
# если изначально не писать число в виде строки - теряется точность!


field_names = 'current_location,current_experience,current_date\n'


class Location:
    def __init__(self, loc):
        self.name = list(loc.keys())[0]
        self.time = Decimal(re.search(r'(tm)(\d+)', self.name)[2])
        self.content = self._get_content(loc[self.name])
        self.mobs = list([Monster(mob) for mob in self.content['mobs']])
        self.gates = list([Location(gate) for gate in self.content['gates']])
        self.hatch = list([Hatch(hatch) for hatch in self.content['hatch']])
        self.content_ = self.mobs + self.gates

    def _get_content(self, loc_content):
        mobs = []
        gates = []
        hatch = []

        for item in loc_content:
            if isinstance(item, str):
                if item.startswith(('Mob', 'Boss')):
                    mobs.append(item)
            elif isinstance(item, dict):
                if list(item.keys())[0].startswith('Hatch'):
                    hatch.append(item)
                else:
                    gates.append(item)

        return {
            'mobs': mobs,
            'gates': gates,
            'hatch': hatch,
        }

    def __str__(self):
        return f'Location info\n' \
               f'\tLocation_name: {self.name}\n' \
               f'\tLocation time: {self.time}\n' \
               f'\tMonsters: {", ".join([mob.name for mob in self.mobs])}\n' \
               f'\tAvailable gates: {", ".join([gate.name for gate in self.gates])}\n' \
               f'\tHatch: {self.hatch}\n'


class Hatch:
    def __init__(self, loc):
        self.name = list(loc.keys())[0]
        self.time = Decimal(re.search(r'(tm)(\d+)', self.name)[2])

    def __str__(self):
        return f'You Win!'


class Monster:
    def __init__(self, mob_name):
        self.name = mob_name
        self.exp = int(re.search(r'(exp)(\d+)', self.name)[2])
        self.time = Decimal(re.search(r'(tm)(\d+)', self.name)[2])

    def __str__(self):
        return f'Monster info\n' \
               f'\tMonster name: {self.name}\n' \
               f'\tExperience: {self.exp}\n' \
               f'\tTime to kill: {self.time}\n'


class Player:
    def __init__(self, user_name, start_location):
        self.name = user_name
        self.current_location = start_location
        self.current_experience = 0
        self.remaining_time = Decimal(remaining_time)
        self.start_location = start_location

    def __str__(self):
        return f'Exp: {self.current_experience}\n' \
               f'Dead time: {self.remaining_time}\n'


class Game:

    with open('rpg.json') as f:
        dungeon_map = json.load(f)

    def __init__(self):
        self.available_actions = OrderedDict()
        self.player = None
        self.start_loc = Location(self.dungeon_map)
        self.hatch_exp = HATCH_EXP
        self.game_result = None
        self.log = []
        self.__settings = {
            'colors':  {'text': 'red', 'action': 'yellow', 'mob': 'blue', 'loc': 'cyan', 'hatch': 'magenta'},
            'delay': 0.5
        }

    def start(self):
        print(colored(f'Hello, stranger!\n'
                      f'Whats your name?\n',
                      color=self.__settings['colors']["text"]))
        player_name = input(colored(">> ", color=self.__settings['colors']["action"]))

        if player_name == '':
            player_name = 'Player'

        print()

        self.player = Player(player_name, self.start_loc)
        print(colored(f"{player_name}, rdy to dungeon?", color=self.__settings['colors']["text"]))
        print(colored(f'{"":-^50}', color=self.__settings['colors']["action"]))
        print(colored("1 - Lets do it!!", color=self.__settings['colors']["action"]))
        print(colored("2 - Later:)", color=self.__settings['colors']["action"]))
        print(colored(f'{"":-^50}', color=self.__settings['colors']["action"]))

        action = int(input(colored(">> ", color=self.__settings['colors']["action"])))

        if action == 1:
            self.menu_select()
        elif action == 2:
            print(colored('Comeback any time', color=self.__settings['colors']["text"]))
            return

    def menu_print(self):
        loc_name = self.player.current_location.name
        mobs = self.player.current_location.mobs
        gates = self.player.current_location.gates
        hatch = self.player.current_location.hatch

        print()
        print(f'{colored(f"You in {loc_name}", color=self.__settings["colors"]["text"])}')
        print(f'{colored("You see:", color=self.__settings["colors"]["text"])}')

        if mobs:
            print(f'{colored("Monsters:", color=self.__settings["colors"]["text"])}')
            print(colored("\n".join([f"\t - {mob.name}" for mob in mobs]), color=self.__settings["colors"]['mob']))
        if gates:
            print(colored('You walk:', color=self.__settings["colors"]['text']))
            print(colored("\n".join([f"\t - {gate.name}" for gate in gates]), color=self.__settings["colors"]['loc']))
        if hatch:
            print(colored(f'Exit:', color=self.__settings["colors"]['text']))
            print(colored(f'\t - {hatch[0].name}', color=self.__settings["colors"]['hatch']))
        if not mobs and not gates and not hatch:
            print(colored(f'\tDeep dungeon.\n'
                          f' \tYou can..', color=self.__settings["colors"]['text']))

        if mobs:
            self.available_actions['Attack Monster'] = self.attack_monster
        if gates:
            self.available_actions['In another location'] = self.change_loc
        if hatch:
            self.available_actions['Exit'] = self.go_to_hatch
        self.available_actions['End it'] = self.quit

        print(colored(f'\n{"":-^50}', color='yellow'))
        print(colored("\n".join([f"\t{num} - {val}" for num, val in enumerate(self.available_actions.keys(), start=1)]),
              color='yellow'))
        print(colored(f'{"":-^50}', color='yellow'))
        print()

    def menu_select(self):
        """ log """
        self.log.append({
            'current_loc': self.player.current_location.name,
            'current_exp': self.player.current_experience,
            'current_date': datetime.strftime(datetime.now(), '%Y.%m.%d %H:%M:%S')
        })

        time.sleep(self.__settings['delay'])
        self.menu_print()

        action = None
        while not action:
            try:
                player_choice = int(input(colored(">> ", color=self.__settings["colors"]['action'])))
                action = list(self.available_actions.values())[player_choice - 1]
            except:
                print(colored('Try again: ', color=self.__settings["colors"]['text']))
        self.available_actions.clear()
        action()

    def attack_monster(self):
        mobs = self.player.current_location.mobs

        if len(mobs) > 1:
            print(colored("Whom to attack?:", color=self.__settings["colors"]["text"]))
            print(colored(
                '\n'.join([f"\t{num} - {mob.name}" for num, mob in enumerate(mobs, start=1)]),
                color=self.__settings["colors"]["mob"]))
            mob_index = self.__user_input(context=mobs)
        else:
            mob_index = 0

        mob = mobs.pop(mob_index)
        self.player.current_experience += mob.exp
        self.player.remaining_time -= mob.time
        print(colored(f"You fighting.. {mob.name}", color=self.__settings["colors"]["text"]))
        print()
        print(f'{"Win":=^50}')
        print(f'{"Exp: ":<6}+{mob.exp:<3}{"":10}{"Time: ": <6}-{mob.time:<3}\n'
              f'{"":-^50}\n\n'
              f'{self.player}')
        print(f'{"":=^50}')
        self.menu_select()

    def change_loc(self):
        gates = self.player.current_location.gates

        if len(gates) > 1:
            print(colored(f'You see:', color=self.__settings["colors"]['text']))
            print(colored(
                '\n'.join([f"\t{num} - {gate.name}" for num, gate in enumerate(gates, start=1)]),
                color=self.__settings["colors"]['loc']))
            print(colored('Where will you go?', color=self.__settings["colors"]['text']))

            gate_index = self.__user_input(context=gates)
        else:
            gate_index = 0

        gate = self.player.current_location.gates.pop(gate_index)
        self.player.remaining_time -= gate.time

        print(colored(f'Walk in {gate.name}', color=self.__settings["colors"]['text']))
        self.player.current_location = gate

        print()
        print(f'{"New place":=^50}')
        print(f'{"Time: ":<6}-{gate.time:<4}\n'
              f'{"":-^50}\n\n'
              f'{self.player}')
        print(f'{"":=^50}')
        self.menu_select()

    def go_to_hatch(self):
        self.player.remaining_time -= self.player.current_location.hatch[0].time
        self.__check_time()
        if self.player.current_experience >= self.hatch_exp:
            self.game_result = 'WIN'
            self.end_the_game()
        else:
            print(colored(f'Not enought exp!\n'
                          f'Need: {self.hatch_exp}\n'
                          f'Have: {self.player.current_experience}\n', color=self.__settings["colors"]['text']))
            self.menu_select()

    def quit(self):
        self.game_result = 'GAME OVER'
        self.end_the_game()

    def end_the_game(self):
        print(f'{self.game_result:=^50}')
        print(f'Player: {self.player.name}')
        print(f'Exp: {self.player.current_experience}')
        print(f'have time: {self.player.remaining_time}')
        print(f'{"":=^50}')
        self.__write_log()

    def __user_input(self, context):
        while True:
            index = int(input(colored('>> ', color=self.__settings["colors"]['action']))) - 1
            if index in range(len(context)):
                return index
            else:
                print(colored('Try again: ', color=self.__settings["colors"]['text']))

    def __check_time(self):
        if self.player.remaining_time < 0:
            self.quit()

    def __write_log(self):
        with open('dungeon.csv', 'w') as log_file:
            log_file.write(field_names)
            for step in self.log:
                step_info = ','.join([f'{val}' for val in step.values()])
                log_file.write(step_info)
                log_file.write('\n')


if __name__ == '__main__':
    game = Game()
    game.start()

# Учитывая время и опыт, не забывайте о точности вычислений!

# зачет!
