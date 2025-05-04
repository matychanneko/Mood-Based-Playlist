# Mood-Based Playlist Generator 🎧

## 1. Overview
This project is a mood-based music playlist generator built using Python and Streamlit. Users can select a mood (Happy, Sad, Energetic, Chill, Romantic), and the app will retrieve and visualize a playlist of YouTube music videos accordingly. The application uses the YouTube Data API to fetch video results and displays them through an interactive dashboard featuring thumbnail galleries, word clouds, and embedded players.

## 2. Requirements
- Python 3.8+
- Required libraries:
  - streamlit
  - google-api-python-client
  - psutil
  - wordcloud

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## 3. Running the Project Locally

To launch the app:

```bash
streamlit run app.py
```

This will open the app in your default browser at `http://localhost:8501/`.

## 4. YouTube API Key Setup

1. Go to the [Google Cloud Console](https://console.developers.google.com/)
2. Create a new project
3. Enable the **YouTube Data API v3**
4. Generate an **API key**
5. When running the app, paste the API key into the input field when prompted

## 5. User Interface Guide

The Streamlit dashboard contains the following:

- **Mood Dropdown**: Choose a mood from the predefined list
- **Slider**: Select the number of videos to retrieve
- **Submit Button**: Triggers the YouTube API call
- **Results Display**:
  - Video thumbnails
  - Word cloud of video titles
  - Embedded YouTube player
  - CPU and memory usage display (via `psutil`)

## 6. Outputs

- Playlists based on selected moods
- Dynamic visual elements (thumbnails, word cloud)
- Performance feedback (CPU and memory usage)

## 7. Additional Resources

- [Deployment Tutorial](Deployment_tutorial.md): Instructions for deploying the app using Ngrok and Streamlit Cloud
- [Demo Video](#): Watch the application in action

