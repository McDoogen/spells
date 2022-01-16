DROP TABLE IF EXISTS spells;

CREATE TABLE spells (
    spell_name TEXT,
    author TEXT,
    ingredients TEXT,
    process TEXT
);

INSERT INTO spells
VALUES (
    "Minimal Vanilla Cake",
    "Douglas Smith",
    "100g Sugar; 100g Flour; 1/4 tbsp Baking Powder; 1/4 tsp Salt; 40g Butter; 85g Milk; 1/4 tbsp Vanilla; 1 Egg",
    "350F for 20-30 min; All Ingredients need to be room temperature; We will be using the Paste Method! :D; Mix Flour, Sugar, Salt, and Baking Powder; Whisk in Butter until sandy; Add Milk and Vanilla; Mix for 30s, then beat for 30s; Add one egg at a time and beat for 30s; Beat higher speed for 30s after all eggs are added; Pour and Bake!; Makes 6 cupcakes or a 9in round cake");

INSERT INTO spells
VALUES (
    "Cake",
    "Douglas Smith",
    "600g Flour, 20g Sugar, 100g Milk, 64oz of America, 400kg Powdered Sugar, 14 cords of butter",
    "Mix the dry stuff, Mix the wet stuff, put it all together and what do you get?, NOTHING!");