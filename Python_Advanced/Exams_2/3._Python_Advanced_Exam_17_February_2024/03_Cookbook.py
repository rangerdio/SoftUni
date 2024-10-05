def cookbook(*ingredients):
    recipes = {}
    result = ''
    for recipe_name, cuisine, ingredients_list in ingredients:
        if cuisine not in recipes:
            recipes[cuisine] = []
        recipes[cuisine].append([recipe_name, ingredients_list])
    recipes_sorted = sorted(recipes.items(), key=lambda x: -len(x[1]))

    for cuisine, recipes_in_cuisine in recipes_sorted:
        recipes_in_cuisine_sorted = sorted(recipes_in_cuisine, key=lambda x: x[0])
        result += f'{cuisine} cuisine contains {len(recipes_in_cuisine)} recipes:\n'
        for recipe, ingredients_list in recipes_in_cuisine_sorted:
            result += f'* {recipe} -> Ingredients: {", ".join(ingredients_list)}\n'

    return result


# print(cookbook(
#     ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#     ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
#     ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
#     ("Croissant", "French", ["flour", "butter", "yeast"]),
#     ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
# ))

# print(cookbook(
#     ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
#     ))


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))
