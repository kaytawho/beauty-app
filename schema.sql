create table users (
    id SERIAL NOT null primary key,
    name VARCHAR(100) not null,
    email TEXT not null unique,
    password VARCHAR(255) not null
);

create table listings (
    id SERIAL NOT null primary key,
    name VARCHAR(100) not null unique,
    state state,
    suburb TEXT,
    image_url TEXT,
    website TEXT,
    description text,
    user_id INT,
    constraint fk_user foreign KEY(user_id) references users(id) on delete CASCADE 
)

INSERT INTO listings (user_id, "name",state,suburb,image_url,website,description)
	VALUES (2, 'Beauty Test 2','VIC','Meadow','https://images.pexels.com/photos/897270/pexels-photo-897270.jpeg?cs=srgb&dl=pexels-m%C3%ADdia-897270.jpg&fm=jpg','www.google.com','Hair stuff'), 
	(3, 'Beauty Test 3','TAS','Townland','https://images.pexels.com/photos/897270/pexels-photo-897270.jpeg?cs=srgb&dl=pexels-m%C3%ADdia-897270.jpg&fm=jpg','www.google.com','Makeup things'),
	(4, 'Beauty Test 4','NSW','Cityville','https://images.pexels.com/photos/897270/pexels-photo-897270.jpeg?cs=srgb&dl=pexels-m%C3%ADdia-897270.jpg&fm=jpg','www.google.com','Product shop'),
	(5, 'Beauty Test 5','QLD','Suburbia','https://images.pexels.com/photos/897270/pexels-photo-897270.jpeg?cs=srgb&dl=pexels-m%C3%ADdia-897270.jpg&fm=jpg','www.google.com','Massage therapy')

create table reviews (
id SERIAL NOT null PRIMARY KEY,
review text,
rating numeric CHECK (rating > 0 and rating < 5) NOT NULL,
listing_id INT,
user_id INT,
constraint fk_listing foreign KEY(listing_id) references listings(id) on delete cascade, 
constraint fk_user foreign KEY(user_id) references users(id) on delete CASCADE
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