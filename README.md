# Birthday Reminder Script

A simple Python program that lists upcoming birthdays for the next week, grouping weekend birthdays (Saturday and Sunday) into Monday.

## Features

- Scans a list of users, each with a name and birthday.
- Calculates which birthdays fall within the next 7 days.
- Rolls weekend birthdays into Monday to ensure they're acknowledged on the next working day.
- Prints a list of user names grouped by weekday.

## Requirements

- Python 3.6 or higher

## Installation

**Clone the repository**

```bash
git clone https://github.com/<your-username>/homework1-1.git
cd homework1-1
```

## Usage

```bash
python3 homework1-1.py
```

### Example Output

```text
Today is 2025-04-18

Monday: Test User
```

### Customizing the Script

Open `homework1-1.py` and edit the `users` list. Each entry should look like:

```python
{
    "name": "User Name",
    "birthday": datetime(YYYY, M, D)
}
```
