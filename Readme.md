# Brave Hotkeys and Shortcuts Import and Export

This pyton script will import and export:
- The users custom shortcuts
- Extensions can also have shortcuts, it also works for them

The script does not modify any other settings

# Where is Braves settings?
- in a file that is called "Preferences", you can open it in notepad/text-editor
- The format inside the file is JSON

# When using the script - Remember:
- To comment and uncomment the last two methods to you need
- Point the paths to the correct Brave-Profile


# Why is the shortcuts not synced between computers?
- My best guess is that if, you on one computer, have multiple brave-profiles, it would be best to have the same hotkeys for all the profiles, and not have individual hotkeys for each brave-profile.

# Can you make a better version?
Note: Most of the script was made with ChatGPT very fast to fit my need - And it worked as expected. Please fork and make a better version. Try make a user-interface with Tkinter.

User Interface:
- There should be a brave-profile selector. It should scan for brave profiles in startup.
- A filepath to a json file where you can import export to
- import button, export button
- it should backup the "Preferences" file with a timestamp, before doing anything
- a large text-area where it log each operation for what the program is doing
- Create exe and binarys for windows/mac/linux

Cheers 😁
