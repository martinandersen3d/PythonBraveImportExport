import json
import os
import platform

# Determine the Brave Preferences file path based on the operating system
def get_brave_pref_path():
    if platform.system() == "Windows":
        return os.path.expanduser(r"~\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Preferences")
    else:
        return os.path.expanduser("~/.config/BraveSoftware/Brave-Browser/Default/Preferences")

# Function to extract and export hotkeys to a JSON file
def extract_and_export_brave_hotkeys():
    try:
        brave_pref_path = get_brave_pref_path()
        with open(brave_pref_path, 'r', encoding='utf-8') as file:
            preferences = json.load(file)

        hotkeys = preferences.get('extensions', {}).get('commands', {})
        accelerators = preferences.get('brave', {}).get('accelerators', {})

        osname = platform.system().lower()
        export_path = f"brave_hotkeys_export_{osname}.json"
        with open(export_path, 'w', encoding='utf-8') as file:
            json.dump({"commands": hotkeys, "accelerators": accelerators}, file, indent=4)
        print(f"Hotkeys and accelerators exported to {export_path}")

    except FileNotFoundError:
        print("Preferences file not found. Ensure Brave Browser is installed.")
    except json.JSONDecodeError:
        print("Error parsing the Preferences file. It may be corrupted.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to import hotkeys and accelerators from a JSON file
def import_hotkeys_and_accelerators_from_file():
    osname = platform.system().lower()
    import_path = f"brave_hotkeys_import_{osname}.json"
    try:
        brave_pref_path = get_brave_pref_path()
        with open(import_path, 'r', encoding='utf-8') as file:
            imported_data = json.load(file)

        with open(brave_pref_path, 'r+', encoding='utf-8') as file:
            preferences = json.load(file)
            preferences['extensions']['commands'] = imported_data.get('commands', {})
            preferences['brave']['accelerators'] = imported_data.get('accelerators', {})
            file.seek(0)
            json.dump(preferences, file, indent=4)
            file.truncate()
        print(f"Hotkeys and accelerators imported from {import_path}")
    except Exception as e:
        print(f"An error occurred while importing hotkeys and accelerators: {e}")

# Example usage
if __name__ == "__main__":
    # Export hotkeys and accelerators
    extract_and_export_brave_hotkeys()
    # Import hotkeys and accelerators
    # import_hotkeys_and_accelerators_from_file()
