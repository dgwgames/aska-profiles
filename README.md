# Aska Profile Manager

The **Aska Profile Manager** is a simple tool that allows you to save and load profiles for the game **Aska**. This can help you back up your game settings and restore them whenever you want, without any technical knowledge.

## Features

- **Save Profiles**: Save your current game settings under a unique profile name.
- **Load Profiles**: Restore game settings from any previously saved profile.
- **Profile Management**: Easily switch between profiles to explore different configurations or restore previous settings.

## How It Works

This program creates "profiles" by making a copy of your Aska game settings. Each profile is saved as a separate file on your computer, so you can come back to it at any time. When you load a profile, the settings are restored in the Aska game folder, allowing you to pick up where you left off.

## Getting Started

### Requirements

- This tool requires **Python** (version 3.8 or newer).
- **PyQt5** library to create a simple graphical interface.

### Installation Guide

1. **Download the Project**: Download the project files and open the project folder.
2. **Install Python and Required Libraries**:
   - If Python is not installed, download and install it from [Python.org](https://www.python.org/downloads/).
   - After installing Python, open a terminal window and install the required library with this command:

     ```bash
     pip install PyQt5
     ```

3. **Running the Program**:
   - Double-click `gui.py` to open the program in the terminal window, or run the following command in the terminal:

     ```bash
     python gui.py
     ```

## Using the Aska Profile Manager

Once the program is open, you’ll see a simple window with options to save and load profiles.

### Saving a Profile

1. In the **Enter profile name** field, type the name you want to use for this profile (e.g., `Profile1`, `AdventureMode`, etc.).
2. Click **Save Profile**.
3. A message will pop up to confirm that your profile was saved. Now, your current Aska settings are safely backed up under that profile name!

### Loading a Profile

1. From the dropdown list, select the profile you want to load.
2. Click **Load Profile**.
3. A confirmation message will appear once the profile is restored. Your Aska settings are now restored to that profile’s saved state!

### Deleting a Profile (optional future feature)

Currently, there isn’t a delete button. If you wish to remove any profile, delete the `.zip` file for that profile from the `profiles` folder in the project directory.

## Troubleshooting

- **No profiles are showing up in the dropdown**: This may mean that no profiles have been saved yet. Create a profile by following the **Saving a Profile** instructions.
- **Cannot open the program**: Ensure Python is installed correctly, and PyQt5 is installed as per the installation guide above.

## Important Note

This tool only saves and restores settings within the Aska game settings folder. It does **not** change or affect other parts of your computer or other game files.

## License

This project is open-source and free to use.
