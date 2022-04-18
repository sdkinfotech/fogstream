from run_test import run_test

# ------- указать задержку при обновлении экрана ------ |
DELAY = 1
# ------- указать путь к файлу с тестами -------------- |
json_file = 'questions.json'
#-------------------------------------------------------|


if __name__ == "__main__":
    run_test(json_file, DELAY)

