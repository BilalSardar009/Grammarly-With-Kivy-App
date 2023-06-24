# Grammarly-With-Kivy-App

This is a simple Grammar Correction App built using the Kivy framework. The app allows users to enter a sentence and get it corrected using the GingerIt library.

## Prerequisites

Before running the app, ensure that you have the following dependencies installed:

- Python (version 3.6 or later)
- Kivy (version 2.0.0 or later)
- KivyMD (version 0.104.2 or later)
- Matplotlib (version 3.3.4 or later)
- Numpy (version 1.20.1 or later)
- GingerIt (version 0.8.1 or later)

## Installation

1. Clone the repository:version. The corrected sentence is then displayed in the app.
git clone https://github.com/username/repository.git](https://github.com/BilalSardar009/Grammarly-With-Kivy-App.git


2. Install the required dependencies using pip:

pip install kivy kivymd matplotlib numpy gingerit

## Usage

To run the app, execute the following command:
python grammarly.py

Upon launching the app, you will see a graphical interface with the following elements:

- Toolbar: Displays the title of the app and a button to change the theme.
- Logo: An image representing the app's logo.
- Input Field: Enter the sentence you want to correct.
- "CORRECTION" Button: Click this button to perform the grammar correction.
- Label: Displays the result message, indicating if the input was corrected or if there was an error.
- Corrected Sentence: Displays the corrected sentence.

## Features

### Grammar Correction

The `correct` method is responsible for performing the grammar correction. It uses the GingerIt library to parse the input sentence and retrieve the corrected version. The corrected sentence is then displayed in the app.

### Theme Change

The `flip` method allows you to change the theme of the app dynamically. It randomly selects a theme from a predefined list and updates the UI accordingly.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
