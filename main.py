from question import GetTest, RunTest


if __name__ == "__main__":

    test = GetTest('questions.json')
    
    for question in test.make_test_list():

        qurrent_test = RunTest(question)
        qurrent_test.run_test()
        qurrent_test.show_result()
    
