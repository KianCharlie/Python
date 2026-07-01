# ☕ NK Cafe - Online Barista (v1)

A terminal-based coffee ordering simulator built in Python. Users are greeted by name, can browse a formatted menu or go straight to ordering, select a coffee and size, confirm their order, pay, and receive a simulated "brewing" sequence before their order is ready.

This is my 3rd Python project, built while learning Python after prior experience with Delphi.

## Features

- Personalized greeting using the customer's name
- Choice to view the full menu or order directly
- Formatted menu display with sizes and coffee options in South African Rand (R)
- Order confirmation step before payment
- Payment validation (checks amount paid against order total)
- Simulated brewing sequence (portafilter, shot, steaming milk, mixing) with timed pacing
- Clean terminal output using screen-clearing between steps

## How to Run

```bash
python barista.py
```

Follow the prompts:
1. Enter your name
2. Type `menu` to see the full menu, or `order` to go straight to ordering
3. Choose a size (`small`, `medium`, `large`)
4. Choose a coffee (`latte`, `cappuccino`, `americano`, `flat white`, `filter coffee`, `caramel cappuccino`, `hazelnut cappuccino`)
5. Confirm your order (`yes`/`no`)
6. Enter payment amount
7. Enjoy your simulated coffee!

## Menu

| Size   | Price  |
|--------|--------|
| Small  | R25.00 |
| Medium | R32.00 |
| Large  | R38.00 |

| Coffee              | Price  |
|---------------------|--------|
| Latte               | R34.00 |
| Cappuccino          | R32.00 |
| Americano           | R26.00 |
| Flat White          | R34.00 |
| Filter Coffee       | R22.00 |
| Caramel Cappuccino  | R38.00 |
| Hazelnut Cappuccino | R38.00 |

## What I Learned

- **Type consistency matters.** Values from `input()` are always strings, and once you format a number into a display string (e.g. `f"R{price:,.2f}"`), it's no longer usable for math. I hit this bug three separate times in different parts of the script (the running total, the payment amount, and the menu display) before internalizing the rule: keep variables in their raw numeric form, and only format them for display at the point of printing.
- **String methods don't modify in place.** `some_string.lower()` returns a new string rather than changing the original — you have to reassign it (`some_string = some_string.lower()`) for the change to stick.
- **Dictionaries as lookup tables.** Instead of a long `if/elif` chain to match a coffee choice to its price, I used dictionaries (`ordercoffee`, `ordersize`) with `.get()` to look up values directly — cleaner and easier to extend.
- **Structuring a multi-step CLI flow** using nested `while True` loops with `break` conditions to control the sequence of menu → order → confirm → pay → complete.

## Known Limitations / Future Improvements

- Limited input validation — unexpected input (typos, blank input) isn't handled gracefully yet
- No option to retry after answering "no" at confirmation or paying an insufficient amount without restarting the script
- No support for multiple items in a single order
- Prices are hardcoded rather than loaded from a config file or database

## Tech Used

- Python 3
- Built-in `time` and `os` modules only — no external dependencies
