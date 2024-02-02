def divide_dishes():
    with open('recipes.txt', encoding='utf-8') as f:
        all_dishes = []
        dish = []
        for line in f:
            if line != "\n":
                dish.append(line[0:-1])
            else:
                all_dishes.append(dish)
                dish = []
        # all_dishes.append(dish) - добавляет последнее блюдо в файле; для задания этого не нужно.
        return all_dishes


def make_dict(dishes):
    cook_book = {}
    for dish in dishes:
        cook_book[dish[0]] = []
        for ing in dish[2:]:
            cook_book[dish[0]].append({'ingredient_name': ing.split(" | ")[0],
                                       'quantity': ing.split(" | ")[1], 'measure': ing.split(" | ")[2]})
    return cook_book


print(make_dict(divide_dishes()))


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in make_dict(divide_dishes()):
            for ing in make_dict(divide_dishes())[dish]:
                result[list(ing.values())[0]] = {list(ing.keys())[2]: list(ing.values())[2],
                                                 list(ing.keys())[1]: int(list(ing.values())[1]) * person_count}

    return result


print(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 3))
