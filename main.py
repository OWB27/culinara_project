import sys
import shlex
from culinara.culinara_manager import CulinaraManager

def main():
    """
    The method to handle every actions by read commands. And with feedbacks for every commands.
    """
    manager = CulinaraManager()
    
    if len(sys.argv) < 2:
        print("Please provide a command, should be 'plan' or 'manage'.")
        return

    cmd = sys.argv[1].lower()

    if cmd == "manage":
        while True:
            user_input = input("> ").strip()
            if not user_input:
                continue
            if user_input.lower() == "exit":
                manager.pantry.save()
                print("Pantry saved. Goodbye!")
                break

            try:
                parts = shlex.split(user_input)
            except ValueError as e:
                print(f"Invalid input: {e}")
                continue

            if not parts:
                continue

            command = parts[0].lower()

            if command == "plan":
                cookable = manager.plan()
                if cookable:
                    print("Cookable Recipes:")
                    for r in cookable:
                        print(f"- {r}")
                else:
                    print("No recipes can be cooked with current pantry.")

            elif command == "recipe":
                if len(parts) < 2:
                    print("Missing sub-command for recipe.")
                    continue
                sub_cmd = parts[1].lower()
                if sub_cmd == "list":
                    for i, r in enumerate(manager.recipes, start=1):
                        print(f"{i}. {r.name}")
                elif sub_cmd == "view" and len(parts) >= 3:
                    recipe_name = " ".join(parts[2:])
                    recipe = manager.get_recipe_by_name(recipe_name)
                    if recipe:
                        print(recipe.view())
                    else:
                        print(f"Recipe '{recipe_name}' not found.")
                elif sub_cmd == "gap" and len(parts) >= 3:
                    recipe_name = " ".join(parts[2:])
                    missing = manager.recipe_gap(recipe_name)
                    if missing:
                        print(f"Shopping List for '{recipe_name}':")
                        for ingredients, quantity in missing.items():
                            print(f" - {ingredients}: {quantity}")
                    else:
                        print(f"All ingredients available for '{recipe_name}'.")
                elif sub_cmd == "cook" and len(parts) >= 3:
                    recipe_name = " ".join(parts[2:])
                    manager.recipe_cook(recipe_name)
                else:
                    print("Unknown recipe command.")

            elif command == "pantry":
                if len(parts) < 2:
                    print("Missing sub-command for pantry.")
                    continue
                sub_cmd = parts[1].lower()
                if sub_cmd == "add" and len(parts) >= 4:
                    ingredient = " ".join(parts[2:-1])
                    quantity = parts[-1]
                    manager.pantry.add(ingredient, quantity)
                elif sub_cmd == "use" and len(parts) >= 4:
                    ingredient = " ".join(parts[2:-1])
                    quantity = parts[-1]
                    manager.pantry.use(ingredient, quantity)
                elif sub_cmd == "process" and len(parts) >= 3:
                    file = parts[2]
                    manager.pantry.process(file, manager.report_file)
                else:
                    print("Unknown pantry command.")

            else:
                print("Unknown command.")

    else:
        if cmd == "plan":
            cookable = manager.plan()
            if cookable:
                print("Cookable Recipes:")
                for r in cookable:
                    print(f"- {r}")
            else:
                print("No recipes can be cooked with current pantry.")
        else:
            print("Unknown command, should be 'plan' or 'manage'.")

if __name__ == "__main__":
    main()
