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

CREATE TABLE exercises (
    id SERIAL PRIMARY KEY,
    name TEXT,
    intensity INTEGER,
    time INTEGER,
    creator_id INTEGER REFERENCES users
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    exercise_id INTEGER REFERENCES exercises,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP,
    comment TEXT
);

