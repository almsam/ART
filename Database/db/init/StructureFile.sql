USE ART;

create table User (
id int AUTO_INCREMENT,
username varchar(64),
password varchar(64),
email varchar (64),
dateOfBirth Date,
pronouns varchar(12),
userDescription varchar(500),
profilePicture BLOB,
Primary key (id)
);

create table Servers (
id int AUTO_INCREMENT,
name varchar(64),
serverPicture BLOB,
Primary key (id)
);

create table Channel (
id int AUTO_INCREMENT,
serverId int,
name varchar(64),
Foreign key (serverId) references Servers(id),
Primary key (id, serverId)
);

create table Friends (
userId int,
friendId int,
foreign key (userId) references User(id),
foreign key (friendId) references User(id),
primary key (userId,friendId)
);

create table Admins (
userId int,
serverId int,
foreign key (userId) references User(id),
foreign key (serverId) references Servers(id),
primary key (userId,serverId)
);

create table ServerMember (
userId int,
serverId int,
foreign key (userId) references User(id),
foreign key (serverId) references Servers(id),
primary key (userId,serverId)
);
