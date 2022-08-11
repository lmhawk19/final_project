mySQL database

CREATE DATABASE IF NOT EXISTS input_feature;
USE input_feature;

CREATE TABLE IF NOT EXISTS users(
    id INTEGER NOT NULL AUTO_INCREMENT,
    username VARCHAR(20) NOT NULL UNIQUE,
    display_name VARCHAR(50) NOT NULL,

    PRIMARY KEY (id),
    CHECK (LENGTH(username) > 0),
    CHECK (LENGTH(display_name) > 0)
);

INSERT INTO users (username, display_name, love_language, activity) VALUES
('janet', 'Janet O','gift giving','ring'),
('kyla', 'Kyla L','quality time','cuddling'),
('lucy', 'Lucy H','acts of service','be present'),
('reema', 'Reema R','acts of service','carry me home'),
('kim', 'Kim K','gift giving','nobu sushi'),
('charlie', 'Charlie P','physical touch','cuddling'),
('Maya', 'Maya I','words of affirmation','tell me you love me'),
('John', 'John S','words of affirmation',"tell me I'm good-looking");