import os

path = os.path.join(os.getcwd(), 'recipes.txt')
with open(path) as cook_file:
    cook_book = {}
    for string in cook_file:
        dish = string.strip()
        ingredients_count = int(cook_file.readline().strip())
        dish_dict = []
        for item in range(ingredients_count):
            ingredient_name, quantity, measure = cook_file.readline().strip().split('|')
            dish_dict.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[dish] = dish_dict
        cook_file.readline()

def get_shop_list_by_dishes(dishes, person_count):
    product_dict = {}
    for _dish in dishes:
        for ingredient in cook_book[_dish]:
            ingredient_list = dict([(ingredient['ingredient_name'],
                                     {'quantity': int(ingredient['quantity']) * person_count,
                                      'measure': ingredient['measure']})])
            if product_dict.get(ingredient['ingredient_name']) == 'None':
                _merger = (int(product_dict[ingredient['ingredient_name']]['quantity']) +
                           int(ingredient_list[ingredient['ingredient_name']]['quantity']))
                product_dict[ingredient['ingredient_name']]['quantity'] = _merger
            else:
                product_dict.update(ingredient_list)
    return product_dict


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))