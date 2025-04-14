import streamlit as st
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

