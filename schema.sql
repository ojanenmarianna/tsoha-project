CREATE TABLE visitors (
    id SERIAL PRIMARY KEY, 
    time TIMESTAMP
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    password TEXT,
    role INTEGER
);
