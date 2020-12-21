from collections import defaultdict

candidates = defaultdict(list)
recipies = []

with open('input21.txt') as f:
    for line in f.read().replace(')', '').splitlines():
        ingredients, allergens = line.split(' (contains ')
        ingredients = ingredients.split(' ')
        recipies.append(ingredients)
        allergens = allergens.split(', ')
        for allergen in allergens:
            candidates[allergen].append(set(ingredients))

for allergen in candidates:
    candidates[allergen] = set.intersection(*candidates[allergen])
ingredients_with_allergenes = set.union(*candidates.values())
print(sum(map(len, [[ingredient for ingredient in recipie if ingredient not in ingredients_with_allergenes] for recipie in recipies])))

ingredient_to_allergene = {}
while len(candidates) > 0:
    allergene = min(candidates, key=lambda a: len(candidates.get(a)))
    ingredients = candidates.pop(allergene)
    assert len(ingredients) == 1
    ingredient = tuple(ingredients)[0]
    ingredient_to_allergene[ingredient] = allergene
    for ingredients in candidates.values():
        if ingredient in ingredients:
            ingredients.remove(ingredient)
            
canonical_list = sorted(list(ingredient_to_allergene), key=ingredient_to_allergene.get)
print(','.join(canonical_list))

