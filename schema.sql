create table users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

create table listings (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    state STATE,
    suburb TEXT,
    image_url TEXT,
    website TEXT,
    description TEXT,
    user_id INT,
    CONSTRAINT fk_listings_user_id foreign KEY(user_id) references users(id) on delete CASCADE 
)

INSERT INTO listings ("name",state,suburb,image_url,website,description,user_id)
	VALUES ('Natural Living by Tamu','VIC','Meadow','https://images.pexels.com/photos/7218974/pexels-photo-7218974.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940g','www.google.com','Natural, organic therapies for the heart, mind and soul.', 6), 
	('Braidz','TAS','Townland','https://images.pexels.com/photos/7275399/pexels-photo-7275399.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500','www.google.com','Qualified hairdresser specialising in braiding for multitextured hair.', 7),
	('Self Care Salon','NSW','Cityville','https://images.pexels.com/photos/6945660/pexels-photo-6945660.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500','www.google.com','Esthetician with over 30 years of experience. Specialising in treatments for those with melanin.', 8),
	('Akwaaba','QLD','Suburbia','https://images.pexels.com/photos/897270/pexels-photo-897270.jpeg?cs=srgb&dl=pexels-m%C3%ADdia-897270.jpg&fm=jpg','www.google.com','Massage therapy, naturopathy and so much more', 9),
    ('Allure Studio','NSW','Sydney','https://images.pexels.com/photos/4027606/pexels-photo-4027606.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500','www.google.com','Specialists in afro hair', 6),
    ('Community Collective','VIC','Footscray','https://images.pexels.com/photos/4056535/pexels-photo-4056535.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500','www.google.com','Skin treatments, massage, yoga and pilates', 6);

create table reviews (
    id SERIAL PRIMARY KEY,
    review TEXT,
    rating NUMERIC CHECK (rating > 0 and rating < 5) NOT NULL,
    listing_id INT,
    user_id INT,
    CONSTRAINT fk_listing FOREIGN KEY(listing_id) REFERENCES listings(id) ON DELETE CASCADE, 
    CONSTRAINT fk_user FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
)

INSERT INTO reviews ("review", rating, listing_id, user_id)
	VALUES ('Amazing place',4, 9,6),
	('My new local',5, 9,7),
	('Great service and always great for a chat',5,9,8),
	('The best treatment I have ever had',5,9,9),
	('Would go again',4,9,10),
	('Bit too busy on Saturdays',3,10,6),
	('Better than other places around',4,11,7),
	('I wouldnt go here again',1,11,8)