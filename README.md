# Text Translation Application Using Python

## Project Description

The Text Translation Application is a Python-based desktop application that allows users to enter text, select a target language, and translate the text into the selected language using the Google Translate service.

## Features

- Accepts single-line and multi-line text input.
- Allows users to select a target language.
- Translates text into the selected language.
- Displays the translated output.
- Validates empty input and language selection.
- Handles translation errors gracefully.

## Technologies Used

- Python 3.12
- Tkinter
- googletrans
- Google Translate

## Installation

1. Clone or download the project.
2. Open the project folder in Visual Studio Code.
3. Install the required dependencies using:

```bash
py -3.12 -m pip install -r requirements.txt

## How to Run the Application

1. Open the project folder in Visual Studio Code.
2. Open the terminal in the project directory.
3. Run the application using:

```bash
py -3.12 translator_app.py

## How to Use

1. Enter the text to be translated in the input text box.
2. Select the required target language from the dropdown list.
3. Click the Translate button.
4. The translated text will be displayed in the output text box.
5. If the input is empty or an error occurs during translation, the application displays an appropriate message.

## Example

The application can translate text into languages such as:

- Tamil
- Telugu
- Kannada
- English
- Hindi

## Error Handling

The application validates user input and handles translation failures gracefully. It displays appropriate warning or error messages when the input is empty, the target language is not selected, or a translation request fails due to an API or network issue.

## Project Structure

```text
TextTranslation/
├── .vscode/
├── requirements.txt
├── translator_app.py
└── README.md

## Sample Input and Output

### Sample Input 1

Text:

Hi, good morning. How are you?

Target Language:

Telugu

### Sample Output 1

హాయ్, శుభోదయం.మీరు ఎలా ఉన్నారు?

### Sample Input 2

Text:

How are you?

Target Language:

Tamil

### Sample Output 2

நீங்கள் எப்படி இருக்கிறீர்கள்?