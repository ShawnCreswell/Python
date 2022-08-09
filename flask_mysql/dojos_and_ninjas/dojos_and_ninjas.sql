

Query: Create 3 new dojos

    INSERT INTO dojos (name) VALUES ("ALASKA");

Query: Delete the 3 dojos you just created

    SET SQL_SAFE_UPDATES = 0;
    DELETE FROM `dojos_and_ninjas`.`dojos` WHERE (`id` = '3');

Query: Create 3 more dojos

    INSERT INTO dojos (name) VALUES ("ALASKA", "Las Vegas", "Chicago"); ("Ben", "Him", 40)

Query: Create 3 ninjas that belong to the first dojo

    INSERT INTO ninjas (first_name, last_name, age) VALUES ("Ben", "Him", 40), ("Harry", "Jones", 25), ("Kim", "Wong", 27);

Query: Create 3 ninjas that belong to the second dojo

    INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Larry", "Hover", 33, 3), ("Kim", "Stewart", 35, 3), ("Kim", "Kardashian", 238, 3);


Query: Create 3 ninjas that belong to the third dojo

INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES ("Jeniffer", "Lopez", 55, 13), ("lil", "baby", 30, 13), ("Aubrey", "Grahm", 38, 13);

Query: Retrieve all the ninjas from the first dojo

SELECT * FROM ninjas WHERE dojo_id = (SELECT id FROM dojos ORDER by id ASC LIMIT 1);

Query: Retrieve all the ninjas from the last dojo

SELECT * FROM ninjas WHERE dojo_id = (SELECT id FROM dojos ORDER by id DESC LIMIT 1);

Query: Retrieve the last ninja

SELECT * FROM dojos WHERE id = 13;

