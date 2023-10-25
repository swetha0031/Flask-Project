CREATE DATABASE users;
USE users;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(50) NOT NULL,
    role VARCHAR(50) NOT NULL
);

-- Query to insert Sample Data
INSERT INTO users (name, email, role) VALUES
	('Varun' , 'varun@gmail.com' , 'CEO'),
    ('Kabir' ,  'kabir@gmail.com' , 'Chair of the board'),
    ('Aditi' , 'aditi@gmail.com' , 'Managing Director'),
    ('Isha' , 'isha03@gmail.com' , 'Legal Advisor'),
    ('Avinash' , 'avinash@gmail.com' , 'Architect'),
    ('Mira' , 'mira@gmail.com' , ' App Developer'),
    ('Zaid' , 'zaidmk@gmail.com' , 'Web Designer'),
    ('Amar' , 'amar321@gmail.com' , 'HR Manager'),
    ('Garima' , 'garimaa@gmail.com' , 'Spokesperson'),
    ('Pranav', 'pranavv@gmail.com' , 'Medical Advisor');
    
-- Query to retrieve users from "users" table
SELECT * FROM  users;

-- Query to retrieve a specific user using ID
SELECT * FROM users WHERE id = 5;

   

