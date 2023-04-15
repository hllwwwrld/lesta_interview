create table ships (
ship varchar(255) not null,
weapon varchar(255),
hull varchar(255),
engine varchar(255),
constraint ships_pk primary key (ship),
constraint ships_fk_weapons foreign key (weapon) references weapons(weapon),
constraint ships_fk_hulls foreign key (hull) references hulls(hull) ,
constraint ships_fk_engines foreign key (engine) references engines(engine) 
);


create table weapons (
weapon varchar(255) not null,
reload_speed int8,
rotational_speed int8,
"diameter" int8,
power_volley int8,
"count" int8,
constraint weapons_pk primary key (weapon)
);

create table hulls (
hull varchar(255) not null,
armor int8,
"type" int8,
capacity int8,
constraint hulls_pk primary key (hull)
);

create table engines (
engine varchar(255) not null,
"power" int8,
"type" int8,
constraint engines_pk primary key (engine)
);
