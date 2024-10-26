# profile_manager.py
import os
import shutil
import zipfile
from pathlib import Path

# Define the path to Aska's game data
ASKA_DATA_PATH = Path(os.getenv('USERPROFILE')) / 'AppData/LocalLow/Sand Sailor Studio/Aska/data'
PROFILES_DIR = Path('profiles')  # Folder to store the compressed profiles


def save_profile(profile_name: str):
    """Save the current Aska data as a compressed profile."""
    profile_path = PROFILES_DIR / f"{profile_name}.zip"

    # Create the profiles directory if it doesn't exist
    if not PROFILES_DIR.exists():
        PROFILES_DIR.mkdir(parents=True)

    with zipfile.ZipFile(profile_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(ASKA_DATA_PATH):
            for file in files:
                file_path = Path(root) / file
                zipf.write(file_path, file_path.relative_to(ASKA_DATA_PATH))

    print(f"Profile '{profile_name}' saved successfully at {profile_path}.")


def load_profile(profile_name: str):
    """Restore the Aska data from a compressed profile."""
    profile_path = PROFILES_DIR / f"{profile_name}.zip"
    if profile_path.exists():
        with zipfile.ZipFile(profile_path, 'r') as zipf:
            zipf.extractall(ASKA_DATA_PATH)
        print(f"Profile '{profile_name}' loaded successfully.")
    else:
        print(f"Profile '{profile_name}' does not exist.")


def list_profiles():
    """List all available profiles."""
    return [file.stem for file in PROFILES_DIR.glob('*.zip')]
