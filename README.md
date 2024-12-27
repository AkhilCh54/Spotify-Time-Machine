# Spotify Time Machine

This repository contains a Python-based application that allows users to create a Spotify playlist featuring the top 100 songs from any given date. The project leverages web scraping and API integration to deliver a nostalgic and personalized music experience.

## Features

- **Dynamic Song Retrieval**:
  - Scrapes data from the "Billboard Hot 100" website to retrieve the top 100 songs for a user-specified date.
  - Ensures accurate and timely song data using Beautiful Soup.

- **Spotify Playlist Creation**:
  - Utilizes the Spotify API to create and populate a playlist directly in the user's Spotify account.
  - Seamlessly integrates with Spotify to save the playlist for future listening.

- **User Input**:
  - Prompts users to enter a date in the format `YYYY-MM-DD`.
  - Generates a curated playlist based on the entered date.

## How It Works

1. **User Input**:
   - The user enters a specific date (e.g., `1995-07-16`).
2. **Data Scraping**:
   - The application retrieves the top 100 songs from the Billboard Hot 100 for the specified date.
   - Beautiful Soup is used for efficient web scraping and data parsing.
3. **Playlist Creation**:
   - The application authenticates with the Spotify API.
   - A new playlist is created and populated with the retrieved songs.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/AkhilCh54/Spotify-Time-Machine.git
   ```
2. Navigate to the project directory:
   ```bash
   cd spotify-time-machine
   ```
3. Install the required dependencies:
   ```bash
   pip install requests beautifulsoup4 spotipy
   ```
4. Enter your Spotify client id and Soptify client secret
5. Run the application:
   ```bash
   python main.py
   ```

## Applications

- **Musical Nostalgia**: Relive the top hits from any memorable date in your life.
- **Personalized Playlists**: Create playlists tailored to specific dates and events.
- **API and Web Scraping Demonstration**: Showcases the integration of web scraping and API usage in a real-world application.
---
Relive the hits of your favorite moments with the Spotify Time Machine!

