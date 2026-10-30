-- Run this once in MySQL to create the database and tables for the project.

CREATE DATABASE IF NOT EXISTS ISMS;
USE ISMS;

CREATE TABLE IF NOT EXISTS sports_data (
    sport VARCHAR(50) PRIMARY KEY,
    viewership_millions FLOAT,
    revenue_crores FLOAT,
    govt_support_crores FLOAT
);

CREATE TABLE IF NOT EXISTS best_player (
    sport VARCHAR(50) NOT NULL,
    player_name VARCHAR(50) NOT NULL,
    year VARCHAR(4) NOT NULL,
    award VARCHAR(50) NOT NULL
);
