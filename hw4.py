easy = {"cat": "кот", "dog": "собака", "owl": "сова", "car": "машина", "pan": "ручка"}

medium = {"river": "речка", "mirror": "зеркало", "divide": "разделять", "map": " карта", "god": "бог"}

hard = {"usual": "обычный", "library": "библиотека", "execute": "выполнять", "code": "код", "accept": "принимать"}

words = {}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    4: "Хорошо",
    5: "Отлично",

}
answers = {}

print('Введите уровень сложности ')
print('Лёгкий, средний, сложный: ')

user_answer = input().lower()

if user_answer == 'средний':
    words = medium
if user_answer == 'сложный':
    words = hard
else:
    words = easy

words_count = len(words)

print(f'Выбран уровень сложности, мы предложим {words_count} слов, подберите перевод')

for words_en, words_ru in words.items():
    print("Нажмите 'Enter'")
    input()

    letter_count = len(words_ru)
    first_letter = words_ru[0]

    print(f'{words_en}, {letter_count} букв, начинается на {first_letter}...')

    user_answer = input().lower()

    if user_answer == words_ru:
        print(f'Верно, {words_en.title()} это {words_ru}')
        answers[words_en] = True
    else:
        print(f'Неверно, {words_en.title()} это {words_ru}')
        answers[words_en] = False

for words_en, is_correct in answers.items():
    if is_correct:
        print(words_en)

correct_words = []
incorrect_words = []

for words_en, is_correct in answers.items():
    if is_correct:
        correct_words.append(words_en)
    else:
        incorrect_words.append(words_en)

print('Правильно отвечены слова: ')
print("\n".join(correct_words))
print('Неправильно отвечены слова: ')
print("\n".join(incorrect_words))

correct_count = len(correct_words)
user_level = levels[correct_count]

print()
print('Ваш ранг: ')
print(f'{user_level}')
