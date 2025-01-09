import json
import os

# Define the path to Brave's Preferences file (Windows example)
BRAVE_PREF_PATH = os.path.expanduser("~\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Preferences")

# Function to extract hotkeys
def extract_brave_hotkeys():
    try:
        with open(BRAVE_PREF_PATH, 'r', encoding='utf-8') as file:
            preferences = json.load(file)

        hotkeys = preferences.get('extensions', {}).get('commands', {})
        if not hotkeys:
            print("No hotkeys found!")
            return

        print("Brave Browser Hotkeys:")
        for command, details in hotkeys.items():
            for detail in details:
                key_combination = detail.get('shortcut', 'Not Set')
                print(f"{command}: {key_combination}")

    except FileNotFoundError:
        print("Preferences file not found. Ensure Brave Browser is installed.")
    except json.JSONDecodeError:
        print("Error parsing the Preferences file. It may be corrupted.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the hotkey extraction
if __name__ == "__main__":
    extract_brave_hotkeys()
