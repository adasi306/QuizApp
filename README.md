# Quizzler Application

This is a Python-based quiz application that uses the Open Trivia Database API to fetch trivia questions and allows users to answer True/False questions interactively. The application is built with Tkinter for a graphical user interface.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [License](#license)

## Description

Quizzler is an interactive trivia quiz game. The game dynamically fetches questions from the Open Trivia Database API and displays them to the user in a graphical user interface. Users can answer True/False questions and track their scores as they progress through the quiz.

## Features

1. **Dynamic Question Fetching**:
   - Retrieves 10 random True/False questions from the Open Trivia Database API.
2. **Interactive User Interface**:
   - Built using Tkinter for an engaging user experience.
3. **Score Tracking**:
   - Keeps track of the user's score throughout the game.
4. **Immediate Feedback**:
   - Highlights correct and incorrect answers with colors.

## Requirements

- Python 3.x
- Required Python libraries:
  - `requests`

## Installation

1. Clone the repository:
```bash
   git clone <repository-url>
   cd <project-directory>
```
2. Install required libraries:
```bash
   pip install -r requirements.txt
```
3. Ensure the following files and directories are correctly structured:
   - `true.png` and `false.png` images are located in `quizaplikacja/zdj/`.

## Running the Application

1. Run the main script:
```bash
   python main.py
```

2. The application window will open. Answer True/False questions and view your score as you progress.

## Project Structure

project/
├── main.py                   # Main script to run the application
├── question_model.py         # Class representing a question
├── quiz_brain.py             # Quiz logic and question handling
├── ui.py                     # Tkinter-based user interface
├── quizaplikacja/
│   └── zdj/
│   │   ├── true.png          # Image for the "True" button
│   │   └── false.png         # Image for the "False" button
└── README.md                 # Documentation

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this project.

