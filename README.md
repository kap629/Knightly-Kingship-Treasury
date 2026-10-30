# Knightly Kingship Treasury

A Python and MySQL sports data management system built as a Class 12 Computer Science project (session 2025-26) at Amity International School, Sector 46, Gurugram.

It stores and analyses data on Indian sports (viewership, revenue, government support) and the players who have won national awards, with separate interfaces for an Admin and a User.

## Features

**User side**
- Revenue bar graph
- Viewership (popularity) line graph
- Government support funds bar graph
- Comparison of revenue and government support funds
- Table of players awarded the Padma Shri

**Admin side** (password protected)
- Add records to the sports data and awards tables
- View all sports data and all awards
- Search a sport
- Delete a sport
- Update a sport's revenue

## Tech stack

- Python
- MySQL
- mysql-connector-python
- Matplotlib
- Tabulate

## Database

Two tables, created by `setup.sql`:

- `sports_data` (sport, viewership_millions, revenue_crores, govt_support_crores)
- `best_player` (sport, player_name, year, award)

The tables start empty. Use the Admin menu to add your own records.

## How to run

1. Install Python and MySQL.
2. Install the libraries:
   ```
   pip install mysql-connector-python matplotlib tabulate
   ```
3. Run `setup.sql` in MySQL to create the database and tables.
4. Copy `config.example.py` to `config.py` and fill in your MySQL password and an admin password.
5. Start the program:
   ```
   python ISMS.py
   ```

## Team

- Advait Narayan Kota (User Side Python functions Code)
- Kapish Kashyap (database code and Python-MySQL connectivity)
- Yuvraj Tyagi (Admin side Python functions code

Guided by Ms. Gurminder Kaur, Computer Science teacher, Amity International School, Sector 46, Gurugram.

## Future scope

- Individual player records, sport-wise
- Player-wise record search
- List of awards given in a specific year
