import json

def load_json_data(file):
    """
    Method to load json file and catch exception.
    """
    try:
        with open(file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Could not found the target file.")
        return {}
    except Exception as e:
        print(f"Error {e} has occurred.")
        return {}

def save_json_data(data, file):
    """
    Method to save json file and catch exception.
    """
    try:
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f)
        return True
    except Exception as e:
        print(f"Error {e} has occurred.")
        return False