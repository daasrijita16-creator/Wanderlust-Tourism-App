-- =========================
-- CREATE DATABASE
-- =========================
DROP DATABASE IF EXISTS tourism_db;
CREATE DATABASE tourism_db;
USE tourism_db;

-- =========================
-- USERS TABLE
-- =========================
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- =========================
-- PACKAGES TABLE
-- =========================
CREATE TABLE packages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    price FLOAT NOT NULL,
    duration VARCHAR(50)
);

-- =========================
-- BOOKINGS TABLE (ADVANCED)
-- =========================
CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    package_id INT,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (package_id) REFERENCES packages(id) ON DELETE CASCADE
);

-- =========================
-- SAMPLE USERS
-- =========================
INSERT INTO users (username, password) VALUES
('admin', '1234'),
('user1', '1234');

-- =========================
-- SAMPLE PACKAGES
-- =========================
INSERT INTO packages (title, description, price, duration) VALUES
('Paris Getaway', 'Experience the city of lights', 20500, '5 Days'),
('Bali Retreat', 'Relax in tropical paradise', 15000, '7 Days'),
('Grand Canyon', 'Explore natural wonder', 16000, '3 Days'),
('Swiss Alps Expedition', 'Snowy mountain adventure', 30000, '6 Days'),
('Tokyo City Lights', 'Modern city experience', 25000, '5 Days');

-- =========================
-- SAMPLE BOOKINGS
-- =========================
INSERT INTO bookings (user_id, package_id) VALUES
(1,1),
(1,2),
(2,3);

ALTER TABLE packages ADD image_url VARCHAR(255);