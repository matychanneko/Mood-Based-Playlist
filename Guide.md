---

## Developer guide: How to extend or modify this project

If you would like to build on top of this project, here’s a quick overview of the code structure:

1. **Mood and Search Mapping**
   - The moods and their associated YouTube search keywords are defined in the `mood_query_map` dictionary.
   - To add more moods, simply add new entries in `mood_query_map`.

2. **YouTube API Integration**
   - The YouTube search function is handled inside `search_youtube()`.
   - You can modify the parameters inside the API call if you want different kinds of videos (e.g., by region, date, etc.).

3. **System Performance Tracking**
   - CPU, memory, and search duration are measured using `psutil` and `time`.
   - You can extend this to track network usage or GPU usage if needed.

4. **Playlist Visualization**
   - Thumbnails and embedded videos are displayed using Streamlit's `st.image()` and `st.video()`.
   - You can customize the layout (e.g., change from 3 columns to 4 columns) by modifying the `st.columns(3)` call.

5. **Word Cloud Generation**
   - The word cloud is generated from the video titles.
   - You can customize the style by adjusting `WordCloud()` parameters (e.g., font size, background color, max words).

6. **Caching System**
   - `@st.cache_data` is used to optimize search performance.
   - If you want to disable caching for development/testing, simply comment out the `@st.cache_data` decorator.

---

### Notes for further extension ideas:

- Add more moods (e.g., "Workout", "Focus", "Party").
- Add user login/authentication to save favorite playlists.
- Improve system stats visualization (charts, live graphs).
- Export playlist links to a downloadable CSV file.

---
