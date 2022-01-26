DROP TABLE IF EXISTS sources;
DROP TABLE IF EXISTS sounds;

CREATE TABLE sounds (
  id SERIAL PRIMARY KEY,
  sound_name VARCHAR(255),
  genre VARCHAR(255)
);

CREATE TABLE sources (
  id SERIAL PRIMARY KEY,
  items VARCHAR(255),
  no_items INT,
  sound_id INT REFERENCES sounds(id)
);