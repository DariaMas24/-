

import logging
from runner import Runner

# Настраиваем логгер
logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',  # перезапись файла при каждом запуске
    encoding='utf-8',
    format='%(levelname)s: %(message)s'
)


class RunnerTest:

    def test_walk(self):
        logger = logging.getLogger(__name__)  # Исправлено на __name__

        try:
            # Передаем отрицательную скорость
            runner = Runner(name="John Doe", speed=-10)

            logger.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logger.warning("Неверная скорость для Runner")
            raise e

    def test_run(self):
        logger = logging.getLogger(__name__)  # Исправлено на __name__

        try:
            # Передаем неверный тип данных для имени
            runner = Runner(name=123, speed=20)

            logger.info('"test_run" выполнен успешно')
        except TypeError as e:
            logger.warning("Неверный тип данных для объекта Runner")
if __name__ == "__main__":
    runner_test = RunnerTest()
    runner_test.test_walk()  # Вызов метода test_walk
    runner_test.test_run()  # Вызов метода test_run