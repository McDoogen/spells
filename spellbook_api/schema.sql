DROP TABLE IF EXISTS spells;

CREATE TABLE spells (
    spell_name TEXT,
    author TEXT,
    ingredients TEXT,
    process TEXT
);

INSERT INTO spells
VALUES (
    "Cookies",
    "Douglas Smith",
    "600g Flour, 20g Sugar, 100g Milk, Tons Chocolate Chips",
    "Do this, Then do that, Then do something else");

INSERT INTO spells
VALUES (
    "Cake",
    "Douglas Smith",
    "600g Flour, 20g Sugar, 100g Milk, 64oz of America, 400kg Powdered Sugar, 14 cords of butter",
    "Mix the dry stuff, Mix the wet stuff, put it all together and what do you get?, NOTHING!");