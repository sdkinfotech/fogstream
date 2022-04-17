from question import Test

question_1 = {
    'question' : 'Как присвоить значение 10 переменной a?',
    'wrong': ['a == 10', 'a : 10', 'a ** 10'],
    'right': 'a = 10'
    }

def run(question):
    test = Test(question)
    test.run_test()
    test.show_result()

if __name__ == "__main__":
    
    run(question_1)
