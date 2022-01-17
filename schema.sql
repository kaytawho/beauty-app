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
rating integer NOT NULL,
listing_id INT,
constraint fk_listing foreign KEY(listing_id) references listings(id) on delete CASCADE 
)


INSERT INTO reviews (listing_id, "review", rating)
	VALUES (7, 'Amazing place',5),
	(2, 'My new local',5),
	(2, 'Great service and always great for a chat',5),
	(4, 'The best treatment I have ever had',5),
	(7, 'Would go again',4),
	(5,'Bit too busy on Saturdays',3),
	(2, 'Better than other places around',4),
	(5, 'I wouldnt go here again',1)