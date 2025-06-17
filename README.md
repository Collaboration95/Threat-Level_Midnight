# Threat-Level_Midnight
**Test Your Wits in the Ultimate Trivia Challenge!**

## Course
10.014 - Computation Thinking for Design | SUTD

## Technologies
* **Python Libraries**: Tkinter for GUI, OS for File Management

## Overview
Trivia Quest is an interactive command-line trivia game that challenges players with randomized questions, tracks scores, and provides administrative controls for managing game data. The game reads questions from a text file, displays images for some questions using Tkinter, and normalizes scores based on the number of questions answered to ensure fair comparisons.

## Features
* **Dynamic Question System**: Loads and shuffles questions from a text file, supporting multiple-choice options, point values, and optional image display.
* **Score Management**: Tracks player scores in a text file, normalizes scores for fairness, and provides options to view high scores or reset data.
* **Admin Controls**: Password-protected interface for sorting scores, listing players, or resetting the score database.

## Skills Demonstrated
* **File I/O and Data Management**: Implemented functions to read/write scores and questions from text files, ensuring robust data persistence (e.g., Read_Scores, Write_Scores).
* **User Interface Design**: Utilised Tkinter to display images for questions and created a command-line menu system for intuitive navigation (e.g., Game_Session, Show_And_Get_Options).
* **Algorithm Development**: Designed sorting algorithms (e.g., bubble sort in List_HighScores) and score normalization logic to ensure fair player comparisons.

## Installation and Usage
1. Clone the repository: `git clone [repo-url]`
2. Install dependencies: Ensure Python 3.x and Tkinter are installed (Tkinter is included with standard Python installations).
3. Place Questions.txt and users.txt in the Final/Resources/ directory.
4. Run the project: `python Game.py`

**Note**: Ensure image files referenced in Questions.txt are accessible at the specified file paths.

## Lessons Learned
Developing Trivia Quest taught me the importance of robust input validation to handle edge cases, such as invalid user inputs or missing files. I overcame challenges with Tkinter's event loop by integrating a manual close button, enhancing user experience. Additionally, managing text file data structures improved my understanding of data persistence and parsing.

## License
MIT License
