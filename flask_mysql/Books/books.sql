Query: Create 5 different users: Jane Amsden, Emily Dixon, Theodore Dostoevsky, William Shapiro, Lao Xiu
INSERT INTO users (name) VALUES ("Jane Amsden"), ("Emily Dixon"), ("Theodore Dostoevsky"); 

Query: Create 5 books with the following names: C Sharp, Java, Python, PHP, Ruby
INSERT INTO books (title) VALUES ("C Sharp"), ("Java"), ("Python"), ("PHP"), ("Ruby"); 

Query: Change the name of the C Sharp book to C#
UPDATE `books`.`books` SET `title` = 'C#' WHERE (`id` = '1');

Query: Change the first name of the 4th user to Bill
UPDATE `books`.`users` SET `name` = 'Bill Shapiro' WHERE (`id` = '4');

Query: Have the first user favorite the first 2 books
INSERT INTO favorites (book_id, user_id) VALUES (1,1), (2, 1)

Query: Have the second user favorite the first 3 books
INSERT INTO favorites (book_id, user_id) VALUES (1, 2), (2,2), (3,2);

Query: Have the third user favorite the first 4 books
INSERT INTO favorites (book_id, user_id) VALUES (1, 3), (2,3), (3,3), (4,3);

Query: Have the fourth user favorite all the books
INSERT INTO favorites (book_id, user_id) VALUES (1, 3), (2,3), (3,3), (4,3), (5,3);

Query: Retrieve all the users who favorited the 3rd book
SELECT user_id FROM favorites 
WHERE book_id = 3;

Query: Remove the first user of the 3rd books favorites
SET SQL_SAFE_UPDATES = 0;
DELETE FROM favorites WHERE user_id = 2 AND book_id = 3



Query: Have the 5th user favorite the 2nd book
INSERT INTO favorites (book_id, user_id) VALUES (2,5)

Find all the books that the 3rd user favorited
SELECT * FROM favorites WHERE user_id = 3;

Query: Find all the users that favorited to the 5th book
SELECT * FROM favorites WHERE book_id = 5;


