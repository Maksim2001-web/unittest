import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        # Ваш код для подготовки тестов
        pass

    def test_challenge(self):
        # Ваш код для теста challenge
        pass

    def test_run(self):
        # Ваш код для теста run
        pass

    def test_walk(self):
        # Ваш код для теста walk
        pass

class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        # Ваш код для подготовки тестов
        pass

    def test_first_tournament(self):
        # Ваш код для теста first_tournament
        pass

    def test_second_tournament(self):
        # Ваш код для теста second_tournament
        pass

    def test_third_tournament(self):
        # Ваш код для теста third_tournament
        pass

def skip_if_frozen(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return func(self, *args, **kwargs)
    return wrapper

for cls in (RunnerTest, TournamentTest):
    for method_name in dir(cls):
        if method_name.startswith('test_'):
            method = getattr(cls, method_name)
            if not method.__name__.startswith('_') and not isinstance(method, classmethod):
                setattr(cls, method_name, skip_if_frozen(method))
