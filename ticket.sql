create table "tickets"
(
    id integer primary key autoincrement,
    ticket_type int not null,
    status int not null,
    message text not null
);