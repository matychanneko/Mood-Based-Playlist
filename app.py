# app_threaded.py
# %%writefile app.py
import streamlit as st
import time
import psutil
import os
import threading
from googleapiclient.discovery import build
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# ------------------ UI CONFIG ------------------ #
st.set_page_config(page_title="Mood-Based Playlist", layout="centered")
st.title("Mood-Based Playlist")
st.markdown("Let's create your mood-matching playlist from YouTube!")

# ------------------ User Inputs ------------------ #
mood = st.selectbox("How are you feeling today?", ["Happy", "Sad", "Energetic", "Chill", "Romantic"])
api_key = st.text_input("Enter your YouTube Data API Key", type="password")
max_results = st.slider("Number of Songs", 1, 10, 5)

# ------------------ Mood Keywords ------------------ #
mood_query_map = {
    "Happy": "happy pop music playlist",
    "Sad": "sad emotional pop songs",
    "Energetic": "energetic pop workout music",
    "Chill": "chill pop lofi beats",
    "Romantic": "romantic love pop songs"
}
query = mood_query_map[mood]

results = []  # global list for fetched results

def fetch_youtube_data():
    global results
    youtube = build("youtube", "v3", developerKey=api_key)
    request = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=max_results
    )
    response = request.execute()
    results = response.get("items", [])

# ------------------ Playlist Generation ------------------ #
if st.button("Generate Playlist") and api_key:
    try:
        start_time = time.time()

        # Start fetching in background
        thread = threading.Thread(target=fetch_youtube_data)
        thread.start()

        with st.spinner('Fetching playlist...'):
            thread.join()

        duration = time.time() - start_time

        if not results:
            st.warning("No results found.")
        else:
            st.success(f"Showing {len(results)} results for mood: {mood}")

            # System performance
            memory = psutil.Process(os.getpid()).memory_info().rss / 1024**2
            cpu = psutil.cpu_percent(interval=1)

            st.markdown("### System Performance")
            st.info(f"Search completed in **{duration:.2f} seconds**")
            st.info(f"Memory used: **{memory:.2f} MB**")
            st.info(f"CPU usage: **{cpu:.1f}%**")
            st.caption(f"Process ID: {os.getpid()}")

            # Thumbnail Gallery
            st.markdown("## Mood-Based Thumbnail Gallery")
            cols = st.columns(3)
            for i, item in enumerate(results):
                video_id = item["id"]["videoId"]
                title = item["snippet"]["title"]
                channel = item["snippet"]["channelTitle"]
                thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
                with cols[i % 3]:
                    st.image(thumbnail_url, use_container_width=True)
                    st.markdown(f"**{title}**")
                    st.caption(f"{channel}")

            # Word Cloud
            st.markdown("## Playlist Word Cloud")
            all_titles = " ".join([item["snippet"]["title"] for item in results])
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
            fig, ax = plt.subplots()
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis("off")
            st.pyplot(fig)

            # Embedded Video Section
            for item in results:
                video_id = item["id"]["videoId"]
                title = item["snippet"]["title"]
                channel = item["snippet"]["channelTitle"]

                st.markdown(f"#### {title}")
                st.caption(f"By {channel}")
                st.video(f"https://www.youtube.com/watch?v={video_id}")
                st.markdown("---")

    except Exception as e:
        st.error(f"Error: {e}")
