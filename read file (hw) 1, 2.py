from pprint import pprint

with open("recipes.txt", "r", encoding='utf8') as file:
    cook_book = {}
    for line in file:
        dishes = line.strip()
        dish_count = int(file.readline())
        dish_structure = []
        for i in range(dish_count):
            food = file.readline()
            ingredient_name, quantity, measure = food.strip().split(' | ')
            dish = {
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure,
            }
            dish_structure.append(dish)
        file.readline()
        cook_book[dishes] = dish_structure
    pprint(cook_book, sort_dicts=False)

print("----------------------------")

def get_shop_list_by_dishes(dishes, person_count):
    shoping_list = {}
    for dish in dishes:
        if dish in cook_book:
            dish_list = {}
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in dish_list:
                    dish_list = {ingredient['ingredient_name']: {'measure': ingredient['measure'], 'quantity': ingredient['quantity']}}
                else:
                    dish_list = {ingredient['ingredient_name']:{'measure':ingredient['measure'], 'quantity': int(ingredient['quantity']) * person_count}}
                    shoping_list.update(dish_list)
    pprint(shoping_list, sort_dicts=False)


#dishes = input()
#person_count = int(input())
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)


