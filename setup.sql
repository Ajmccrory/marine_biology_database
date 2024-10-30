-- setup.sql

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS marine_biodiversity_db;

-- Use the database
USE marine_biodiversity_db;

-- Drop tables if they exist to reset the schema (optional, for testing purposes)
DROP TABLE IF EXISTS observations;
DROP TABLE IF EXISTS researchers;
DROP TABLE IF EXISTS species;

-- Create researchers table
CREATE TABLE researchers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    affiliation VARCHAR(200)
);

-- Create species table
CREATE TABLE species (
    id INT AUTO_INCREMENT PRIMARY KEY,
    common_name VARCHAR(100) NOT NULL,
    scientific_name VARCHAR(200) NOT NULL,
    habitat VARCHAR(200),
    migratory_pattern VARCHAR(200),
    seasonal_behavior VARCHAR(200)
);

-- Create observations table with foreign keys to researchers and species
CREATE TABLE observations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    researcher_id INT,
    species_id INT,
    observation_date DATE,
    location VARCHAR(200),
    notes TEXT,
    FOREIGN KEY (researcher_id) REFERENCES researchers(id) ON DELETE CASCADE,
    FOREIGN KEY (species_id) REFERENCES species(id) ON DELETE CASCADE
);
