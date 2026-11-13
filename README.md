# Python Password Generator

An interactive command-line password generator developed in Python to practice programming fundamentals, input validation, and secure randomization.

## Features

- Generates passwords between 12 and 18 characters.
- Guarantees at least one uppercase letter.
- Generates 3–5 additional numeric characters.
- Allows users to select one special character.
- Uses Python's `secrets` module for cryptographically secure random character generation.
- Implements input validation and exception handling.
- Features color-coded terminal output and an interactive help menu.

## Technologies Used

- Python 3
- `secrets` — Secure random character generation
- `string` — Character sets and punctuation
- ANSI escape codes — Terminal formatting

## Getting Started

1. Download or clone this repository.
2. Ensure Python 3 is installed.
3. Run the application:

```bash
py password_generator.py
```

4. Follow the terminal prompts to generate a password.

No third-party dependencies are required.

## What I Learned

This project helped strengthen my understanding of:

- Python functions and reusable code
- While loops and conditional statements
- Exception handling with `try` and `except`
- String manipulation and user input validation
- Differences between standard pseudorandom generation and cryptographically secure randomization
- Building interactive command-line applications

## Future Improvements

- Randomize the positions of all password characters.
- Allow users to generate passwords with fully randomized special characters.
- Add more flexible password customization options.
- Improve password policy enforcement and validation.

## Project Purpose

This project was developed as a hands-on learning exercise to strengthen my Python programming skills while exploring concepts relevant to cybersecurity and password security.
