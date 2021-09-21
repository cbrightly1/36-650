DROP TABLE rdata;
create table rdata(
    id SERIAL PRIMARY KEY,
    a TEXT UNIQUE NOT NULL CHECK (char_length(a) > 0),
    b TEXT UNIQUE NOT NULL CHECK (char_length(a) > 0),
    moment DATE DEFAULT '2020-01-01 ();',
    x NUMERIC(5,2) CHECK (X > 0)
);