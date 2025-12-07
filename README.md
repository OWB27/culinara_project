My coursework project in Python.



This project is a comprehensive command-line application that serves as a smart kitchen
assistant. It combines interactive commands with batch file processing to manage a recipe
book and a virtual pantry. The goal is to build a robust, object-oriented application that
demonstrates your mastery of all concepts covered in the course so far, from data structures
and OOP to error handling and file management.

The application will operate in two modes:
1. Single Command Mode (Default): When run with a command (e.g., python main.py
plan), it executes the task and immediately exits.
2. Interactive Mode: When run with the special manage command (python main.py
manage), it enters a continuous command-line session for managing the pantry and
recipes.

○ Application Mode:
  ■ manage: Enters the interactive command loop.
  
○ Recipe Commands:
  ■ recipe list: Prints a simple, numbered list of all available recipe
names.

  ■ recipe view "<recipe_name>": Prints the full details of a specific
recipe, including its name and list of ingredients.

  ■ recipe gap "<recipe_name>": Performs a "gap analysis" and prints
a shopping list of missing ingredients for a specific recipe.

  ■ recipe cook "<recipe_name>": Checks if a recipe is cookable. If it
is, it consumes the required ingredients from the pantry. If not, it reports
an error.

○ Pantry Commands:
  ■ pantry add “<ingredient_name>” <quantity>: Adds the
specified quantity to an ingredient in the pantry. If the ingredient doesn't
exist, it should be added. The quantity should be an integer.

  ■ pantry use “<ingredient_name>” <quantity>: Reduces the
quantity of an ingredient. Must fail with an error if stock is insufficient.

  ■ pantry process <filepath>: Reads a text file where each line is a
command (e.g., ADD sugar 300) and executes them sequentially.

○ Analysis Command:
  ■ plan: Analyzes the current pantry and prints a list of all "cookable"
recipes.

○ Interactive-Only Command:
  ■ exit: Saves the final state of the pantry and terminates the interactive
session.
