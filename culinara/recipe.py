class Recipe:

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def missing_ingredients(self, pantry):
        """
        Method that return a dictionary for the missing ingredients.
        """
        missing = {}
        for item, required in self.ingredients.items():
            available = pantry.inventory.get(item, 0)
            if available < required:
                missing[item] = required - available
        return missing

    def cookable(self, pantry):
        """
        If there are no missing ingredients, return True.
        """
        return len(self.missing_ingredients(pantry)) == 0

    def view(self):
        """
        Information of the recipe.
        """
        lines = [f"Recipe: {self.name}", "Ingredients:"]
        for name, quantity in self.ingredients.items():
            lines.append(f"  - {name}: {quantity}")
        return "\n".join(lines)