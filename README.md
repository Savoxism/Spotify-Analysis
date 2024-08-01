# Spotify Wrapped Analysis

## Overview

In this project, we delve into the intricacies of Spotify Wrapped, focusing on the data and trends that define user listening habits over the year. Users are categorized into unique Spotify-created characters based on their listening patterns.

## Key Links

- [Understanding My Data on Spotify](https://support.spotify.com/us/article/understanding-my-data/)
- [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
- [Me in 2023: Streaming Habits Wrapped](https://newsroom.spotify.com/2023-11-29/me-in-2023-streaming-habits-wrapped/)
- [Spotify Songs Dataset on Kaggle](https://www.kaggle.com/datasets/mrmorj/dataset-of-songs-in-spotify/data)
- [Solving Spotify Multi-Class Genre Classification Problem](https://www.analyticsvidhya.com/blog/2023/03/solving-spotify-multiclass-genre-classification-problem/#Prerequisites)

## Character Descriptions

In Spotify Wrapped, users are assigned one of several characters based on their listening habits. There are 12 distinct characters

- **The Vampire**: You listen to emotional, atmospheric music more than most.
- **The Time Traveller**: You travel back in time and listen to songs on repeat, again and again. The best tracks never get old.
- **The Shapeshifter**: Quick to move from one artist to the next.
- **The Luminary**: Prefers light, upbeat music.
- **The Alchemist**: Frequently creates their own playlists.
- **The Cyclops**: Focus on one genre.
- **The Mastermind**: Listen to a wide range of different genres.
- **The Roboticist**: You like to let the algorithm decides what to play.
- **The Collector**: Listen mostly to your own playlists.
- **The Hunter**: You frequently skip tracks more than others.
- **The Fanatic**: Your top artist makes up more than a third of your listening.
- **The Hypnotist**: Your concentration is absolute. You like to play albums all the way through, from the opening track to the final note.

## Key Takeaways

1. **Data Collection Period**: Data is logged from January 1st 00:00 to November 15th 23:59. Listening activity from November 16th to December 31st is not considered.

2. **Top Songs Calculation**: Top songs are calculated based on total time listened, rather than play count.

3. **Top 100 Playlist**: The first 10 songs in the Top 100 playlist are sorted by play count. The remaining songs are sorted by artist, though they are close in play count.

4. **Total Listening Time**: Includes both music and podcasts.

5. **Top 5 Artists Calculation**: Determined by total play counts rather than total time listening.

6. **Playlist Investigation**: You can only investigate playlists that you created, not those created by others or by Spotify.

## Project Structure

- `data/`: Contains the dataset of songs on Spotify from Kaggle.
- `scripts/`: Includes scripts for data analysis and visualization.
- `results/`: Stores the results of the analysis, including character assignments and trends.

## How to Run

1. Clone the repository.
   ```sh
   git clone <repository-url>
