# Password Generator (V1)

A simple Python script that generates a password by combining parts of your name, surname, and birth year with some randomness.

> ⚠️ **This is a learning project, not a real security tool.** Do not use the passwords this generates for actual accounts. Because they're built from personal information (name, surname, birth year), they're more predictable than a truly random password and should be treated as a string-manipulation exercise, not a password manager.

## What it does

The script asks for your name, surname, and birth year, validates the input, then builds a password by combining and rearranging parts of that information with a random number and a random special character.

## How to run it

\```bash
python password_gen.py
\```

You'll be prompted for:
- Your name
- Your surname
- Your birth year (4 digits)

The script will then print a generated password to the terminal.

## What I learned building this

- Working with Python string methods (`.upper()`, slicing, indexing)
- Using the `random` module for the first time
- Writing input validation loops
- Strengthening general Python fundamentals

## Roadmap

- [ ] Check the generated password against known data breaches (e.g. via the [Have I Been Pwned API](https://haveibeenpwned.com/API/v3)) and regenerate if it's been exposed
- [ ] Refactor the repeated input-validation blocks into a single reusable function
- [ ] Add stronger validation for name/surname fields
 
