from unittest import TestCase, main
from runner import Runner
class RunnerTest(TestCase):
    def test_walk(self):
        runner = Runner("John Doe")  # создаём объект Runner с произвольным именем
        for _ in range(10):  # вызываем метод walk 10 раз
            runner.walk()
        self.assertEqual(runner.distance, 50)  # проверяем, что distance равен 50

    def test_run(self):
        runner = Runner("John Doe")  # создаём объект Runner с произвольным именем
        for _ in range(10):  # вызываем метод run 10 раз
            runner.run()
        self.assertEqual(runner.distance, 100)  # проверяем, что distance равен 100
    def test_challenge(self):
        runner1 = Runner("Alice")  # создаём первого объекта Runner
        runner2 = Runner("Bob")    # создаём второго объекта Runner

        for _ in range(10):  # вызываем метод run для первого объекта
            runner1.run()

        for _ in range(10):  # вызываем метод walk для второго объекта
            runner2.walk()

        # Проверяем, что дистанции не равны
        self.assertNotEqual(runner1.distance, runner2.distance)
if __name__ == '__main__':
    main()


