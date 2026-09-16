# Basic Terminal-based Calculator

A simple terminal-based calculator written in Python. Takes two numbers and an operator as input and returns the result.

## Features

- Supports 7 operations:
  - `+` Addition
  - `-` Subtraction
  - `*` Multiplication
  - `/` Division
  - `//` Floor Division
  - `%` Modulus
  - `**` Exponentiation
- Handles invalid operator input gracefully

## Tech Stack

- Python 3

## How to Run

1. Clone the repository
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. Run the script
   For Windows : 
   ```bash
   python code.py
   ```
   For Mac :
   ```bash
   python3 code.py
   ```

4. Follow the prompts
   ```
   Enter a : 10
   Enter b : 5
   Enter Operator : +
   Answer : 15
   ```

## Example

```
Enter a : 20
Enter b : 4
Enter Operator : //
Answer : 5
```

## Possible Improvements

- Wrap input parsing in try/except to handle non-numeric input
- Add a loop to allow multiple calculations without restarting
- Move operator logic into a dictionary of functions instead of if/elif chains

## Author

Atul Gupta
