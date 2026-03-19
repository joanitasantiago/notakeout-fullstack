CREATE TABLE foods (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    nutritional_value VARCHAR(200),
    unit VARCHAR(20),
    in_stock BOOLEAN DEFAULT FALSE
);

CREATE TABLE recipe (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    instructions TEXT NOT NULL,
    category VARCHAR(50) NOT NULL
);

CREATE TABLE menu (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL
);

CREATE TABLE recipe_food (
    id SERIAL PRIMARY KEY,
    recipe_id INTEGER NOT NULL REFERENCES recipe(id),
    food_id INTEGER NOT NULL REFERENCES foods(id),
    quantity VARCHAR(100) NOT NULL
);

CREATE TABLE menu_recipe (
    id SERIAL PRIMARY KEY,
    menu_id INTEGER NOT NULL REFERENCES menu(id),
    recipe_id INTEGER NOT NULL REFERENCES recipe(id),
    day_part VARCHAR(50) NOT NULL
);
