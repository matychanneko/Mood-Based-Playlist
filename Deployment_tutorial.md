# Deployment Tutorial: Ngrok & Streamlit Cloud

This guide explains how to deploy the Mood-Based Playlist Generator using either **Ngrok** for local/Colab-based testing or **Streamlit Cloud** for public access.

---

## 1. Deploying with Ngrok (Google Colab / Local)

Ngrok allows you to expose your local or notebook-based Streamlit app to the internet through a temporary public URL, ideal for testing or demos.

### Requirements
- Google Colab or local Jupyter Notebook
- `streamlit` and `pyngrok` installed:
```bash
!pip install streamlit pyngrok --quiet
```

### Steps (for Google Colab)

1. Write your app to `app.py` using:
```python
%%writefile app.py
# (your Streamlit app code goes here)
```

2. Start the Streamlit server in the background (silently):
```bash
!streamlit run app.py &>/dev/null &
```

3. Setup ngrok to create a public URL:
```python
from pyngrok import ngrok, conf
ngrok.kill()

# Set ngrok auth token
conf.get_default().auth_token = "your_ngrok_auth_token"
ngrok.set_auth_token("your_ngrok_auth_token")
```
> You can get your auth token from: [https://dashboard.ngrok.com/get-started/setup](https://dashboard.ngrok.com/get-started/your-authtoken)

4. Create the public tunnel using Ngrok:
```python
from pyngrok import ngrok
public_url = ngrok.connect(addr="8501")
print("Streamlit app available at:", public_url)
```

5. Click the printed link to access the web app.

> Make sure to input your YouTube API key in the app when prompted.

---

## 2. Deploying with Streamlit Cloud (Public Deployment)

Streamlit Cloud allows you to deploy your app to the internet easily and without local hosting.

### Requirements
- GitHub repository with your project
- Streamlit Cloud account

### Steps

1. **Push your code to GitHub**
   - Make sure your repository includes the necessary files:
     - `app.py` (the main Streamlit application)
     - `requirements.txt` (list of required Python libraries)

2. **Sign in to Streamlit Cloud**
   - Visit [https://streamlit.io/cloud](https://streamlit.io/cloud)
   - Sign in using your GitHub account

3. **Create a New App**
   - Click **"New App"**
   - Select your GitHub repository and target branch
   - Set the **main file path** to `app.py`
   - Click **"Deploy"**

4. **Configure API Key using Secrets Management**
   - In the Streamlit Cloud dashboard, go to your app settings → **Secrets**
   - Add the following configuration:
     ```toml
     [api]
     youtube_key = "YOUR_YOUTUBE_API_KEY"
     ```
   - In your `app.py`, you can access the API key using:
     ```python
     import streamlit as st
     youtube_key = st.secrets["api"]["youtube_key"]
     ```

```

---

## 3. Deployment Demo Video

📽️ A full walkthrough of the deployment process and app usage is available here:  
🔗 [Deployment Demo Video](link here)
