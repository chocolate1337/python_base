import logging
from abc import ABC, abstractmethod

STRIKE_SCORE = 20
SPARE_SCORE = 15
SKITTLE_COUNT = 10
FRAME_COUNT = 10


class BowlingError(Exception):
    pass


class InputValueError(BowlingError):
    pass


class MaxFrameError(BowlingError):
    pass


class SpareError(BowlingError):
    pass


class StrikeError(BowlingError):
    pass


class Game:

    def __init__(self, game_result, need_log=False):

        if need_log:
            self.LOG_LEVEL = logging.INFO
        else:
            self.LOG_LEVEL = logging.CRITICAL

        logging.basicConfig(level=self.LOG_LEVEL, filename='bowling.log',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        if not game_result:
            logging.critical('Не указаны результаты игры !')
            raise AttributeError('Не указаны результаты игры !')

        self.frame = 1
        self.total_score = 0
        self.game_result = game_result
    # TODO хорошо справился, единственное этот метод рызбить бы на парочку
    def calculate_result(self):

        first_throw = FirstThrow()
        second_throw = SecondThrow()
        first_hit, second_hit = 0, 0

        logging.info(f' >> NEW GAME')
        logging.info(f' < {self.game_result} >')

        throw = first_throw
        for throw_symbol in self.game_result:

            if self.frame > FRAME_COUNT:
                logging.critical(f' Превышено кол-во фреймов ! (максимально возможно {FRAME_COUNT})')
                raise MaxFrameError(f' Превышено кол-во фреймов ! (максимально возможно {FRAME_COUNT})')

            try:
                throw_score = throw.process(symbol=throw_symbol)
            except BowlingError as exc:
                logging.critical(f' {exc}')
                raise exc

            self.print_frame_results(throw, throw_symbol, throw_score)

            if isinstance(throw, FirstThrow):
                if throw_score == STRIKE_SCORE:
                    throw = first_throw
                    self.total_score += STRIKE_SCORE
                    self.frame += 1
                else:
                    first_hit = throw_score
                    throw = second_throw
            else:
                if throw_score == SPARE_SCORE:
                    self.total_score += SPARE_SCORE
                else:
                    second_hit = throw_score
                    total_skittle_hits = first_hit + second_hit
                    if total_skittle_hits < SKITTLE_COUNT:
                        self.total_score += total_skittle_hits
                    else:
                        logging.critical('введены результаты бросков превышающие кол-во кеглей !')
                        raise AttributeError('введены результаты бросков превышающие кол-во кеглей !')

                self.frame += 1
                throw = first_throw

            logging.info(f' TOTAL SCORE < {self.total_score} >')
            logging.info(f' >> END GAME')

        return self.total_score

    def print_frame_results(self, throw, throw_symbol, throw_score):
        if self.total_score > 0 and isinstance(throw, FirstThrow):
            logging.info(f' Итого: {self.total_score}')
        logging.info(f' FRAME_{self.frame} {throw} - "{throw_symbol}" -> {throw_score}')

# TODO интересное решение, а как тебе вариант, чтобы в качестве состояний использовать Страйк, Спэйр, и Сумму, 
#  и у всех этих состояний будет метод получить_счет. Далее, когда будешь разбирать заданную строку, то если первый элемент Х, 
#  то ты его отрезаешь (или перескакиваешь через 1 элемент) и получаешь очки - 20, если не Х, то отрезаешь 2 элемента и по условиям ставишь нужный статус.
class Throw(ABC):

    def process(self, symbol):
        if symbol == 'X':
            return self.strike()
        elif symbol == '/':
            return self.spare()
        elif symbol == '-':
            return 0
        elif '1' <= symbol <= '9':
            return int(symbol)
        else:
            raise InputValueError(f'Введен неверный символ "{symbol}"')


    @abstractmethod
    def strike(self):
        pass

    @abstractmethod
    def spare(self):
        pass


class FirstThrow(Throw):

    def strike(self):
        return STRIKE_SCORE

    def spare(self):
        raise SpareError('Spare "/" не может быть 1 броском ')

    def __str__(self):
        return self.__class__.__name__


class SecondThrow(Throw):

    def strike(self):
        raise StrikeError('Strike "X" не может быть 2 броском ')

    def spare(self):
        return SPARE_SCORE

    def __str__(self):
        return self.__class__.__name__


if __name__ == '__main__':
    try:
        game = Game(game_result='d12', need_log=False)
        print(game.calculate_result())
    except (BowlingError, BaseException) as exc:
        print(f'ошибка {exc}')
