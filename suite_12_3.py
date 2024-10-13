import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создаем TestSuite
suite = unittest.TestSuite()

# Добавляем тесты в TestSuite
suite.addTest(unittest.makeSuite(RunnerTest))
suite.addTest(unittest.makeSuite(TournamentTest))

# Создаем объект класса TextTestRunner с аргументом verbosity=2
runner = unittest.TextTestRunner(verbosity=2)

# Запускаем TestSuite
runner.run(suite)
