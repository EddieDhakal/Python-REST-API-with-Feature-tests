create table "tickets"
(
    id int primary key not null,
    type int not null,
    status int not null,
    message text not null
);