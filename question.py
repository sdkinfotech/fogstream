from random import shuffle


class Test:

    def __init__(self, test) -> None:
        
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
        
        # -- сформируем ответы таким образом, чтобы связать их с индексами ---
        # -- контейнер для строк ответов с индексами
        self.results = {}
        # -- добавляем перемешанные строки ответов с индексами
        number = 1
        for answer in self.answers:
            self.results[number] = answer
            number += 1
        # ------------------------------------------------------------------- #
        
        # -- отобразим в консоли вопрос и варианты ответов с индексами ------ #
        print("")
        print(self.test['question'], "\n") 

        for key, value in self.results.items():
            print(f"{key} : {value}")
       
        print("")
        # -- запросим ответ от пользователя ------#
        self.user_answer = int(input("Введите номер правильного ответа: "))
        

    def show_result(self):

        if self.results[self.user_answer] == self.test['right']:
            print("True")
        else:
            print("False")
        
    

       


    
        