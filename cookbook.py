from pprint import pprint
from unittest import result
cook_book = {}
with open('recipes.txt', 'rt', encoding='utf-8') as file:
    for x in file:
        x = x.strip()
        if x.isdigit():
            continue
        elif x and '|' not in x:
            cook_book[x] = []
            food = x
        elif x and '|' in x:
            a, b, c = x.split(" | ")
            cook_book.get(food).append(dict(ingredient_name=a, quantity=int(b), measure=c))

pprint(cook_book)

def get_shop_list_by_foods(food_list, person_count):
    shop_list = {}
    for food in food_list:
        if food in cook_book:
            for ingredient in cook_book[food]:
                if ingredient['ingredient_name'] in shop_list:
                    shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                else:
                    shop_list[ingredient['ingredient_name']] = ({'measure': ingredient['measure'], 'quantity':
                                                                (ingredient['quantity'] * person_count)})
        else:
            print('Такого блюда нет в книге')
    return shop_list


pprint(get_shop_list_by_foods(['Фахитос', 'Омлет'], 2))


with open('1.txt', 'r', encoding='utf-8') as file_1:
    line_1 = {}
    count_1 = 0
    for line in file_1.readlines():
        count_1 += 1
        line_1['1.txt'] = count_1
with open('1.txt', 'r', encoding='utf-8') as file_1:
    text_1 = file_1.read()

with open('2.txt', 'r', encoding='utf-8') as file_2:
    line_2 = {}
    count_2 = 0
    for line in file_2.readlines():
        count_2 += 1
        line_2['2.txt'] = count_2
with open('2.txt', 'r', encoding='utf-8') as file_2:
    text_2 = file_2.read()

with open('3.txt', 'r', encoding='utf-8') as file_3:
    line_3 = {}
    count_3 = 0
    for line in file_3.readlines():
        count_3 += 1
        line_3['3.txt'] = count_3
with open('3.txt', 'r', encoding='utf-8') as file_3:
    text_3 = file_3.read()

join = sorted(list(line_1.items()) + list(line_2.items()) + list(line_3.items()), key=lambda x: x[1])

with open('result.txt', 'w', encoding='utf-8') as f_result:
    for line in join:
        f_result.write(f'{join[0][0]}\n {join[0][1]}\n {text_2}\n {join[1][0]}\n {join[1][1]}\n {text_1}\n'
                          f'{join[2][0]}\n {join[2][1]}\n {text_3}\n')

print(f_result)