spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    """Return a list of strings with the names of each spicy food."""
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    """Return a list of dictionaries where the heat level is greater than 5."""
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    """Print each spicy food in a formatted way."""
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        # Create the heat level emoji string
        heat_emojis = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """Return a single dictionary for the spicy food matching the given cuisine."""
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None  # Return None if no match found

def print_spiciest_foods(spicy_foods):
    """Print only the spicy foods with heat level greater than 5."""
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)

def get_average_heat_level(spicy_foods):
    """Return the average heat level of all spicy foods."""
    if not spicy_foods:  # Handle empty list
        return 0
    
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    average = total_heat / len(spicy_foods)
    return int(average)  # Return as integer as specified

def create_spicy_food(spicy_foods, spicy_food):
    """Return the original list with the new spicy food added."""
    # Create a copy of the original list to avoid modifying it
    new_list = spicy_foods.copy()
    new_list.append(spicy_food)
    return new_list