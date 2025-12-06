from .recipe import Recipe
from .pantry import Pantry
from .utils import load_json_data, save_json_data

class CulinaraManager:
    def __init__(self, config_file='config.json'):
        config = load_json_data(config_file)
        self.recipe_file = config.get("recipe_file", "data/recipes.json")
        self.pantry_file = config.get("pantry_file", "data/pantry.json")
        self.report_file = config.get("report_file", "reports/report.txt")

        self.pantry = Pantry(self.pantry_file)
        self.recipes = self.load_recipes()

    def load_recipes(self):
        """
        Load and return a list of recipes.
        """
        data = load_json_data(self.recipe_file)
        return [Recipe(r["name"], r["ingredients"]) for r in data]

    def get_recipe_by_name(self, name):
        """
        Find the recipe by the same name from the list of recipes loaded.
        """
        for r in self.recipes:
            if r.name.lower() == name.lower():
                return r
        return None

    def plan(self):
        """
        return cookable recipes.
        """
        cookable = []
        for r in self.recipes:
            if r.cookable(self.pantry):
                cookable.append(r.name)
        return cookable

    def recipe_gap(self, recipe_name):
        """
        return missing ingredients for given recipe.
        """
        recipe = self.get_recipe_by_name(recipe_name)
        if not recipe:
            print(f"Recipe '{recipe_name}' not found.")
            return {}
        missing = recipe.missing_ingredients(self.pantry)
        return missing

    def recipe_cook(self, recipe_name):
        """
        If there no missing ingredients, cook the recipe and consume corresponding ingredients.
        """
        recipe = self.get_recipe_by_name(recipe_name)
        if not recipe:
            print(f"Recipe '{recipe_name}' not found.")
            return False
        missing = recipe.missing_ingredients(self.pantry)
        if missing:
            print(f"Cannot cook '{recipe_name}', missing:")
            for ingredients, quantity in missing.items():
                print(f" - {ingredients}: {quantity}")
            return False
        for ingredients, quantity in recipe.ingredients.items():
            self.pantry.use(ingredients, quantity)
        print(f"Successfully cooked '{recipe_name}'. Pantry has been updated.")
        return True