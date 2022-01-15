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

INSERT INTO public.listings (user_id, "name",state,suburb,image_url,website,description)
	VALUES (2, 'Beauty Test 2','VIC','Meadow','https://images.pexels.com/photos/897270/pexels-photo-897270.jpeg?cs=srgb&dl=pexels-m%C3%ADdia-897270.jpg&fm=jpg','www.google.com','Hair stuff'), 
	(3, 'Beauty Test 3','TAS','Townland','https://images.pexels.com/photos/897270/pexels-photo-897270.jpeg?cs=srgb&dl=pexels-m%C3%ADdia-897270.jpg&fm=jpg','www.google.com','Makeup things'),
	(4, 'Beauty Test 4','NSW','Cityville','https://images.pexels.com/photos/897270/pexels-photo-897270.jpeg?cs=srgb&dl=pexels-m%C3%ADdia-897270.jpg&fm=jpg','www.google.com','Product shop'),
	(5, 'Beauty Test 5','QLD','Suburbia','https://images.pexels.com/photos/897270/pexels-photo-897270.jpeg?cs=srgb&dl=pexels-m%C3%ADdia-897270.jpg&fm=jpg','www.google.com','Massage therapy')