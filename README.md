# 🎬 Movie Recommendation System

A simple Streamlit app that recommends movies based on a selected title. It uses **cosine similarity** on a precomputed dataset to suggest similar movies.

---

## 🚀 Features

- Dropdown to select any movie from the dataset  
- Recommends 5 similar movies based on cosine similarity  
- Lightweight and fast — uses pickled data for performance  
- Built using Streamlit, deployable on the web (e.g., Heroku)

---

## 🛠 How to Run

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <project-folder>
```
2. Ensure Required Files Exist
   
Make sure the following files are in your project directory:
movie_dict.pkl — Contains the movie metadata dictionary
similarity.pkl — Contains the similarity matrix
app.py — Main application script

3. Install Dependencies
```bash
pip install -r requirements.txt
```
4. Run the App
```bash
streamlit run app.py
```
💡 How It Works
Loads movie metadata and similarity matrix using pickle
Uses cosine similarity to find the top 5 most similar movies
Renders a dropdown for movie selection and displays results when "Recommend" is clicked


🗂 Folder Structure
```bash
📂 your_project/
├── app.py                 # Streamlit application script
├── movie_dict.pkl         # Pickled dictionary of movie metadata
├── similarity.pkl         # Pickled similarity matrix
├── movies.pkl             # (optional backup, unused in code)
├── requirements.txt       # Python package dependencies
├── Procfile               # For deploying on Heroku
├── .gitignore             # Git ignored files
└── README.md              # Project description
```
🧠 Example Usage
Select a movie like The Matrix from the dropdown
Click "Recommend"
You’ll see 5 similar movies recommended below

✅ Output
The app will show a list like:
```bash
Inception  
Interstellar  
The Dark Knight  
Blade Runner 2049  
Looper
```

❗ Notes
The recommendations are based on precomputed cosine similarity scores
Make sure .pkl files are in the same folder as app.py
Works with any .pkl-based similarity setup (if formatted correctly)










