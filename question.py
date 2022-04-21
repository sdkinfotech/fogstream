from random import shuffle
import json


class GetTest:

    def __init__(self, json_file) -> None:
        """получает тесты из json"""

        self.json_file = json_file
        with open(self.json_file, 'r', encoding='utf-8') as file:
            self.questions = json.load(file)

    def make_test_list(self):
        """
        формирует список тестов и перемешивает их
        Возвращает уже перемешанный список в вызов
        """

        test_list = []
        for item in self.questions:
            test_list.append(item)
        shuffle(test_list)
        return test_list


class RunTest:

    def __init__(self, test) -> None:

        """
        формирует список вариантов ответов 
        перемешивает список ответов
        test: объект с тестом(вопрос - ответы).
        """

        self.test = test

        # --генерируем ответы на вопрос -------------- #

        # -- создаем пустой список контейнер
        self.answers = []
        # -- добавляем все неправильные ответы
        for answer in self.test['wrong']:
            self.answers.append(answer)
            # -- добавляем правильный ответ
        self.answers.append(self.test['right'])
        # -- перемешиваем список
        shuffle(self.answers)
        # -------------------------------------------- #

    def run_test(self):

        """
        Отображает на экране вопрос и варианты ответов.
        Вариантам ответов присваиваются порядковые индексы
        Ожидает ответа от пользователя
        """

        # -- сформируем ответы таким образом, чтобы связать их с индексами ---
        # -- контейнер для строк ответов с индексами
        self.results = {}
        # -- добавляем перемешанные строки ответов с индексами
        number = 1
        for answer in self.answers:
            self.results[str(number)] = answer
            number += 1
        # ------------------------------------------------------------------- #

        # -- отобразим в консоли вопрос и варианты ответов с индексами ------ #
        print("")
        print(self.test['question'], "\n")

        for key, value in self.results.items():
            print(f"{key} : {value}")

        print("")
        # -- запросим ответ от пользователя ------#
        self.user_answer = input("Введите номер правильного ответа: ")

    def show_result(self):

        """
        сравнивает ответ пользователя с правильным ответом
        Для этого используется полученное значение из json 
        ответ пользователя привязан к индексу в словаре.
        Возвращает True или False
        """

        # -- находим правильный ответ -------------------------- #
        if self.results[self.user_answer] == self.test['right']:

            return True

        else:

            return False
