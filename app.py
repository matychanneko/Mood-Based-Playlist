import streamlit as st
import time
import psutil
import os
from googleapiclient.discovery import build

# ------------------ UI CONFIG ------------------ #
st.set_page_config(page_title="Mood-Based Pop Playlist", layout="centered")
st.title("🎧 Mood-Based Pop Playlist")
st.markdown("Let's create your mood-matching playlist from YouTube!")

# ------------------ User Inputs ------------------ #
mood = st.selectbox("🎭 How are you feeling today?",
                    ["Happy", "Sad", "Energetic", "Chill", "Romantic"])

api_key = st.text_input("🔑 Enter your YouTube Data API Key", type="password")
max_results = st.slider("🎚️ Number of Songs", 1, 10, 5)

# ------------------ Mood Keywords ------------------ #
mood_query_map = {
    "Happy": "happy pop music playlist",
    "Sad": "sad emotional pop songs",
    "Energetic": "energetic pop workout music",
    "Chill": "chill pop lofi beats",
    "Romantic": "romantic love pop songs"
}
query = mood_query_map[mood]

# ------------------ Playlist Generation ------------------ #
if st.button("🎬 Generate Playlist") and api_key:
    try:
        start_time = time.time()
        youtube = build("youtube", "v3", developerKey=api_key)

        request = youtube.search().list(
            q=query,
            part="snippet",
            type="video",
            maxResults=max_results
        )
        response = request.execute()
        results = response.get("items", [])

        if not results:
            st.warning("No results found.")
        else:
            st.success(f"Showing {len(results)} results for mood: {mood}")
            # ✅ OS Metrics
            import psutil, os, time
            memory = psutil.Process(os.getpid()).memory_info().rss / 1024**2
            cpu = psutil.cpu_percent(interval=1)
            duration = time.time() - start_time
            st.markdown("### 📈 System Performance")
            st.info(f"⏱️ Search completed in **{duration:.2f} seconds**")
            st.info(f"🧠 Memory used: **{memory:.2f} MB**")
            st.info(f"⚙️ CPU usage: **{cpu:.1f}%**")
            st.caption(f"🆔 Process ID: {os.getpid()}")

            # ------------------ YouTube Thumbnail Gallery ------------------ #
            st.markdown("## 🖼️ Mood-Based Thumbnail Gallery")
            mood_emoji_map = {
                "Happy": "😊",
                "Sad": "💔",
                "Energetic": "⚡",
                "Chill": "🌙",
                "Romantic": "💖"
            }
            mood_emoji = mood_emoji_map.get(mood, "")

            cols = st.columns(3)
            for i, item in enumerate(results):
                video_id = item["id"]["videoId"]
                title = item["snippet"]["title"]
                channel = item["snippet"]["channelTitle"]
                thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
                with cols[i % 3]:
                    st.image(thumbnail_url, use_container_width=True)
                    st.markdown(f"**🎵 {title}**")
                    st.caption(f"{mood_emoji} {channel}")

            # ------------------ Word Cloud Section ------------------ #
            from wordcloud import WordCloud
            import matplotlib.pyplot as plt

            st.markdown("## ☁️ Playlist Word Cloud")
            try:
                all_titles = " ".join([item["snippet"]["title"] for item in results])
                wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_titles)
                fig, ax = plt.subplots()
                ax.imshow(wordcloud, interpolation='bilinear')
                ax.axis("off")
                st.pyplot(fig)
            except Exception as e:
                st.warning(f"Unable to generate Word Cloud: {e}")


            for item in results:
                video_id = item["id"]["videoId"]
                title = item["snippet"]["title"]
                channel = item["snippet"]["channelTitle"]

                st.markdown(f"#### 🎵 {title}")
                st.caption(f"By {channel}")
                st.video(f"https://www.youtube.com/watch?v={video_id}")
                st.markdown("---")

    except Exception as e:
        st.error(f"❌ Error: {e}")
