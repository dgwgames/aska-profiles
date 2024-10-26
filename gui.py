# gui.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QComboBox, QLineEdit, QLabel, QMessageBox
from profile_manager import save_profile, load_profile, list_profiles


class ProfileManagerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aska Profile Manager")
        self.setGeometry(200, 200, 400, 200)

        # Layout and widgets
        layout = QVBoxLayout()

        # Profile name input for saving
        self.profile_name_input = QLineEdit(self)
        self.profile_name_input.setPlaceholderText("Enter profile name to save")
        layout.addWidget(self.profile_name_input)

        # Save profile button
        save_button = QPushButton("Save Profile", self)
        save_button.clicked.connect(self.save_profile)
        layout.addWidget(save_button)

        # Profile selection for loading
        self.profile_selector = QComboBox(self)
        self.update_profile_list()
        layout.addWidget(self.profile_selector)

        # Load profile button
        load_button = QPushButton("Load Profile", self)
        load_button.clicked.connect(self.load_profile)
        layout.addWidget(load_button)

        # Set the main layout
        self.setLayout(layout)

    def save_profile(self):
        profile_name = self.profile_name_input.text()
        if profile_name:
            save_profile(profile_name)
            self.update_profile_list()
            QMessageBox.information(self, "Success", f"Profile '{profile_name}' saved successfully!")
        else:
            QMessageBox.warning(self, "Error", "Please enter a profile name.")

    def load_profile(self):
        profile_name = self.profile_selector.currentText()
        if profile_name:
            load_profile(profile_name)
            QMessageBox.information(self, "Success", f"Profile '{profile_name}' loaded successfully!")
        else:
            QMessageBox.warning(self, "Error", "Please select a profile to load.")

    def update_profile_list(self):
        self.profile_selector.clear()
        profiles = list_profiles()
        self.profile_selector.addItems(profiles)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProfileManagerGUI()
    window.show()
    sys.exit(app.exec_())
