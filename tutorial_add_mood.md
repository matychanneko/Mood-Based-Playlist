# Tutorial: How to Add a New Mood

This guide explains how to add a new mood to the Mood-Based Playlist Generator application.

## 1. Update Mood Query Mapping

In your `app.py`, locate the following dictionary:

```python
mood_query_map = {
    "Happy": "happy music playlist",
    "Sad": "sad emotional songs",
    "Energetic": "energetic workout music",
    "Chill": "chill lofi beats",
    "Romantic": "romantic love songs"
}
```

Add a new mood like this:

```python
"Angry": "angry rock music"
```

## 2. Update the Mood Dropdown

Find the line that defines the mood selection dropdown and add your new mood:

```python
selected_mood = st.selectbox("Choose your mood", ["Happy", "Sad", "Energetic", "Chill", "Romantic", "Angry"])
```

## 3. (Optional) Customize Visualizations

You can apply different themes or icons based on the new mood, such as:
- Changing word cloud color scheme
- Adding mood-specific emoji or labels
- Applying filtering rules for search results

## 4. Test the New Mood

Run the app using:

```bash
streamlit run app.py
```

Choose your new mood from the dropdown and verify that:
- YouTube videos load correctly
- Visuals (thumbnails, word cloud) reflect the change