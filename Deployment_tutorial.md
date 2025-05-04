# Deployment Tutorial: Ngrok & Streamlit Cloud

This tutorial explains how to deploy the Mood-Based Playlist Generator using either Ngrok for local testing or Streamlit Cloud for public deployment.

---

## 1. Deploying with Ngrok (for Local Testing)

### Requirements
- Python and Streamlit installed
- Ngrok installed and logged in

### Steps

1. Launch the Streamlit app:
```bash
streamlit run app.py
```

2. In a new terminal window, run:
```bash
ngrok http 8501
```

3. Ngrok will generate a public URL like `https://xxxx.ngrok.io` - copy and share this to access your app remotely.

Note: Your local machine must remain running for Ngrok to work.

---

## 2. Deploying with Streamlit Cloud (for Public Access)

### Requirements
- GitHub account with your project uploaded
- Streamlit Cloud account

### Steps

1. Push your full project (including `app.py`, `requirements.txt`, etc.) to a GitHub repository.
2. Visit [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click "New app" and link your GitHub repository.
4. Configure your secrets (API key) by creating a `secrets.toml` in the Cloud settings:

```toml
[api]
youtube_key = "YOUR_YOUTUBE_API_KEY"
```

5. Click "Deploy" — your app will be accessible via a permanent public URL.

---

## 3. Demo Video

A demonstration of the full deployment process and live application is available here:

📽️ [Deployment Demo Video](link here) 
