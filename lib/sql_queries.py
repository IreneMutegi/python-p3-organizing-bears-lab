# Select all female bears, returning their name and age
select_all_female_bears_return_name_and_age = """
SELECT name, age FROM bears WHERE sex = 'F';
"""

# Select the oldest bear's name
select_oldest_bear_name = """
SELECT name FROM bears ORDER BY age DESC LIMIT 1;
"""

# Select the youngest bear's name
select_youngest_bear_name = """
SELECT name FROM bears ORDER BY age ASC LIMIT 1;
"""

# Select all bears ordered by name
select_all_bears_ordered_by_name = """
SELECT * FROM bears ORDER BY name ASC;
"""

# Select all alive bears
select_all_alive_bears = """
SELECT * FROM bears WHERE alive = 1;
"""
