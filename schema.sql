CREATE TABLE visitors (
    id SERIAL PRIMARY KEY, 
    time TIMESTAMP
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    password TEXT,
    role INTEGER,
    visible BOOLEAN
);

CREATE TABLE exercises (
    id SERIAL PRIMARY KEY,
    name TEXT,
    intensity INTEGER,
    time INTEGER,
    creator_id INTEGER, 
    visible BOOLEAN
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    exercise_id INTEGER REFERENCES exercises,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP,
    comment TEXT
);

CREATE TABLE summary (
    user_id INTEGER REFERENCES users,
    exercise_id INTEGER REFERENCES exercises
);

