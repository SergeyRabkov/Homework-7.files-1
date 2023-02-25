def get_cook_book_from_file(fail_name):
    with open(fail_name, 'r', encoding='utf-8') as fail:
        cook_book = {}
        for line in fail:
            ingredients = []
            recipe_name = line.strip()
            ingredient_count = int(fail.readline())
            for _ in range(ingredient_count):
                ingredient = fail.readline().strip()
                ingredient_name, quantity, mesure = ingredient.split(' | ')
                ingredients.append({
                    'ingredient_name' : ingredient_name,
                    'quantity' : quantity,
                    'mesure' : mesure
                    })
            cook_book.setdefault(recipe_name, ingredients)
            fail.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book_from_file('recipes.txt')
    shop_list = {}
    for dishe in dishes:
        if dishe in cook_book.keys():
            for ingredient in cook_book[dishe]:
                quantity = ingredient['quantity']
                ingredient['quantity'] = int(quantity) * person_count
                if ingredient['ingredient_name'] not in shop_list:
                    dict_value = {'mesure' : ingredient['mesure'], 'quantity' : ingredient['quantity']}
                    shop_list.setdefault(ingredient['ingredient_name'], dict_value)
                else:
                    shop_list_value_quantity = shop_list[ingredient['ingredient_name']]['quantity']
                    shop_list[ingredient['ingredient_name']]['quantity'] = shop_list_value_quantity + ingredient['quantity']
    return shop_list


print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 6))
