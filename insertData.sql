-- Insert sample data into bands table
INSERT INTO bands (name, hometown) VALUES ('Sauti Sol', 'Nairobi');
INSERT INTO bands (name, hometown) VALUES ('Burna Boy', 'Port Harcourt');
INSERT INTO bands (name, hometown) VALUES ('Spoek Mathambo', 'Johannesburg');
INSERT INTO bands (name, hometown) VALUES ('Femi Kuti', 'Lagos');
INSERT INTO bands (name, hometown) VALUES ('Amadou & Mariam', 'Bamako');

-- Insert sample data into venues table
INSERT INTO venues (title, city) VALUES ('KICC', 'Nairobi');
INSERT INTO venues (title, city) VALUES ('Eko Convention Center', 'Lagos');
INSERT INTO venues (title, city) VALUES ('Sun Arena', 'Pretoria');
INSERT INTO venues (title, city) VALUES ('Mariam Makeba Hall', 'Johannesburg');
INSERT INTO venues (title, city) VALUES ('National Theatre', 'Accra');

-- Insert sample data into concerts table
INSERT INTO concerts (date, band_id, venue_id) VALUES ('2024-09-20', 1, 1);
INSERT INTO concerts (date, band_id, venue_id) VALUES ('2024-10-12', 2, 2);
INSERT INTO concerts (date, band_id, venue_id) VALUES ('2024-11-05', 3, 3);
INSERT INTO concerts (date, band_id, venue_id) VALUES ('2024-12-01', 4, 4);
INSERT INTO concerts (date, band_id, venue_id) VALUES ('2024-12-15', 5, 5);