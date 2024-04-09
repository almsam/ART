ALTER USER 'ART' IDENTIFIED WITH mysql_native_password BY 'ARTpw';

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

-- We are only using one server, so we will not be using this table or any references to this table from other tables
-- create table Servers (
-- id int AUTO_INCREMENT,
-- name varchar(64),
-- serverPicture BLOB,
-- Primary key (id)
-- );

create table Channel (
id int AUTO_INCREMENT,
-- serverId int,
name varchar(64),
-- Foreign key (serverId) references Servers(id),
-- Primary key (id, serverId)
isDM bit,
Primary key (id)
);

-- create table Friends (
-- userId int,
-- friendId int,
-- foreign key (userId) references User(id),
-- foreign key (friendId) references User(id),
-- primary key (userId,friendId)
-- );

create table DM (
userId int,
otherId int,
channelId int,
foreign key (userId) references User(id),
foreign key (otherId) references User(id),
foreign key (channelId) references Channel(id),
primary key (userId,otherId,channelId)
);

create table Admins (
userId int,
channelId int,
-- serverId int,
foreign key (userId) references User(id),
-- foreign key (serverId) references Servers(id),
foreign key (channelId) references Channel(id),
-- primary key (userId,serverId)
primary key (userId,channelId)
);

-- create table ServerMember (
-- userId int,
-- serverId int,
-- foreign key (userId) references User(id),
-- foreign key (serverId) references Servers(id),
-- primary key (userId,serverId)
-- );

create table ChannelMember (
userId int,
-- serverId int,
channelId int,
foreign key (userId) references User(id),
-- foreign key (serverId) references Channel(serverId),
foreign key (channelId) references Channel(id),
-- primary key (userId,serverId)
primary key (userId,channelId)
);

create table Message (
messageId int AUTO_INCREMENT,
userId int,
messageTime DateTime,
channelId int,
messageContent nvarchar(500),
-- serverId int,
foreign key (userId) references User(id),
foreign key (channelId) references Channel(id),
-- foreign key (serverId) references Servers(id),
-- primary key (messageTime,channelId,serverId)
primary key (messageId)
);
