import streamlit as st
import time
import psutil
import os
from googleapiclient.discovery import build

# ---------------- CONFIG ---------------- #
st.set_page_config(page_title="Mood-Based Playlist", layout="centered")
st.title("🎧 Mood-Based Pop Playlist (OS Enhanced)")
st.markdown("_Generate YouTube playlists by mood + track system-level performance_")

# ---------------- Mood Setup ---------------- #
MOOD_MAP = {
    "Happy": "happy pop music playlist",
    "Sad": "sad emotional pop songs",
    "Energetic": "energetic pop workout music",
    "Chill": "chill pop lofi beats",
    "Romantic": "romantic love pop songs"
}

# ---------------- Input ---------------- #
mood = st.selectbox("🎭 Choose your mood", list(MOOD_MAP.keys()))
api_key = st.text_input("🔑 YouTube API Key", type="password")
max_results = st.slider("🎚️ Number of Songs", 1, 10, 5)

query = MOOD_MAP[mood]

# ---------------- Function: Search YouTube ---------------- #
def search_youtube(api_key, query, max_results):
    try:
        youtube = build("youtube", "v3", developerKey=api_key)
        request = youtube.search().list(
            q=query,
            part="snippet",
            type="video",
            maxResults=max_results
        )
        return youtube, request.execute()
    except Exception as e:
        st.error(f"❌ YouTube API error: {e}")
        return None, None

# ---------------- Function: Log Playlist ---------------- #
def log_playlist(mood, video_list):
    log_path = "playlist_log.txt"
    with open(log_path, "a", encoding="utf-8") as f:
        for video in video_list:
            f.write(f"{mood},{video['title']},{video['url']}\n")
    st.success("✅ Playlist logged to playlist_log.txt")

# ---------------- MAIN ---------------- #
if st.button("🎬 Generate Playlist") and api_key:
    st.markdown("---")
    st.write("🔄 Processing...")

    start_time = time.time()

    youtube, response = search_youtube(api_key, query, max_results)

    if response:
        video_list = []
        results = response.get("items", [])

        if not results:
            st.warning("No results found.")
        else:
            st.success(f"Showing {len(results)} results for mood: {mood}")

            # ✅ OS Metrics
            memory = psutil.Process(os.getpid()).memory_info().rss / 1024**2
            cpu = psutil.cpu_percent(interval=1)
            duration = time.time() - start_time

            st.markdown("### 📈 System Performance")
            st.info(f"⏱️ Search completed in **{duration:.2f} seconds**")
            st.info(f"🧠 Memory used: **{memory:.2f} MB**")
            st.info(f"⚙️ CPU usage: **{cpu:.1f}%**")
            st.caption(f"🆔 Process ID: {os.getpid()}")


            for item in results:
                video_id = item["id"]["videoId"]
                title = item["snippet"]["title"]
                channel = item["snippet"]["channelTitle"]
                url = f"https://www.youtube.com/watch?v={video_id}"

                video_list.append({"title": title, "url": url})

                # ✅ UI สวยแบบเดิม
                st.markdown(f"#### 🎵 {title}")
                st.caption(f"By {channel}")
                st.video(url)
                st.markdown("---")

