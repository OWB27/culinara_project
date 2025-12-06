from .utils import load_json_data, save_json_data

class Pantry:

    def __init__(self, file):
        self.file = file
        self.inventory = load_json_data(file)

    def save(self):
        """
        Save the data of the pantry to the target file.
        """
        return save_json_data(self.inventory, self.file)

    def add(self, ingredient, quantity):
        """
        Add the ingredient with gieven quantity to the pantry.
        """
        try:
            quantity = int(quantity)
        except ValueError:
            print("Quantity must be an integer.")
            return False
        
        if quantity <= 0:
            print("Quantity must be positive.")
            return False
        self.inventory[ingredient] = self.inventory.get(ingredient, 0) + quantity
        self.save()
        print(f"Added {quantity} of '{ingredient}'.")
        return True

    def use(self, ingredient, quantity):
        """
        Consume the ingredient with gieven quantity to the pantry.
        """
        try:
            quantity = int(quantity)
        except ValueError:
            print("Quantity must be an integer.")
            return False

        if ingredient not in self.inventory:
            print(f"Ingredient '{ingredient}' not found in pantry.")
            return False
        if self.inventory[ingredient] < quantity:
            print(f"Not enough '{ingredient}', need {quantity - self.inventory[ingredient]} more.")
            return False

        self.inventory[ingredient] -= quantity
        if self.inventory[ingredient] == 0:
            del self.inventory[ingredient]
        self.save()
        print(f"Used {quantity} of '{ingredient}'.")
        return True

    def process(self, file, report_file):
        """
        This method read commands and write the results to a report file.
        """
        lines = []
        try:
            with open(file, "r", encoding="utf-8") as f:
                for raw in f:
                    line = raw.strip()
                    if not line:
                        continue
                    parts = line.split()
                    cmd = parts[0].upper()
                    try:
                        if cmd == "ADD":
                            self.add(parts[1], int(parts[2]))
                            lines.append(f"SUCCESS: {line}")
                        elif cmd == "USE":
                            if self.use(parts[1], int(parts[2])):
                                lines.append(f"SUCCESS: {line}")
                            else:
                                lines.append(f"ERROR: Cannot USE {int(parts[2])} {parts[1]}. only {self.inventory[parts[1]]} available.")
                        else:
                            lines.append(f"ERROR: Unknown command '{cmd}'.")
                    except Exception as e:
                        lines.append(f"ERROR: {line} ({e})")
            with open(report_file, "w", encoding="utf-8") as rf:
                rf.write("\n".join(lines))
            print(f"Report saved to {report_file}")
        except FileNotFoundError:
            print("Could not found the target file.")
