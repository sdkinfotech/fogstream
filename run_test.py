
from question import GetTest, RunTest
import os
import time

def clscr():
    """Очистка экрана терминала"""
    os.system('cls' if os.name=='nt' else 'clear')


    
def run_test(json_file, delay):
    """
    Запускает программу тестирования. 

    json_file: получает путь к файлу с тестами 
    delay: получает значение задержки очистки экрана
    """
    # -- получаем список тестов из json ---------------#
    test = GetTest(json_file)
    # -- создадим список с тестами --------------------#    
    for question in test.make_test_list():
        clscr()
        # -- и для каждого элемента в списке 
        current_test = RunTest(question)
        try:
            # -- запускаем тест
            current_test.run_test()

            # -- если ответ совпал с правильным 
            if current_test.show_result():
                print("\nПравильно!")
                time.sleep(delay)
            else:
                # -- иначе пишем 
                print("\nНеправильно!")
                time.sleep(delay)
        # -- если есть исключение то
        except KeyError:

            print("\nНекорректный ввод, повторите")
            time.sleep(delay)
            clscr()
            key_error = True

            # -- повторяем предыдущий тест до тех пор пока key_error
            while key_error:
                try:
                    current_test.run_test()

                    if current_test.show_result():
                        print("\nПравильно!")
                        time.sleep(delay)
                        clscr()
                        key_error = False
                    else:
                        print("\nНеправильно!")
                        time.sleep(delay)
                        key_error = False
                except KeyError:
                    print("\nНекорректный ввод, повторите")
                    time.sleep(delay)
                    clscr()