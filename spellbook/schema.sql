DROP TABLE IF EXISTS spells;

CREATE TABLE spells (
    spell_name TEXT,
    author TEXT,
    ingredients TEXT
);

INSERT INTO spells
VALUES ("Cookies", "Douglas Smith", "600g Flour, 20g Sugar, 100g Milk, Tons Chocolate Chips");