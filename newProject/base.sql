CREATE TABLE IF NOT EXISTS mfcus (
    id SERIAL,
    user_id BIGINT,
    username VARCHAR(45),
    phone_number VARCHAR(15),
    seria VARCHAR(12),
    step INTEGER DEFAULT 0,
    language VARCHAR(15) DEFAULT('UZ')
)
--INSERT INTO mfcus (username) VALUES ('Sardor Shorahimov');
SELECT * FROM mfcus;

CREATE TABLE books (
    id INTEGER,
    user_id BIGINT,
    food_name VARCHAR(45),
    count_food INTEGER
);

CREATE TABLE sales (
    id INTEGER,
    order_cost INTEGER,
    book_day DATE,
    book_time TIME
);

