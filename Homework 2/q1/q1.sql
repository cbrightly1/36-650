
create table rdata(
    id SERIAL PRIMARY KEY,
    a TEXT CHECK (char_length(a) > 0),
    b TEXT CHECK (char_length(a) > 0),
    moment DATE,
    x NUMERIC(5,2)
);