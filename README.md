# 🎬 Movie Recommendation System

A simple Streamlit app that recommends movies based on a selected title. It uses **cosine similarity** on a precomputed dataset to suggest similar movies.

---

## 🚀 Features

- Select a movie from a dropdown list
- Get top 5 similar movie recommendations
- Lightweight and easy to run locally
- Uses `pickle` files for fast loading of movie data and similarity scores

---

## 🛠 How to Run

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <project-folder>
```

2. Ensure Required Files Exist
Make sure the following files are in the project directory:

movie_dict.pkl — Contains the movie metadata dictionary
similarity.pkl — Contains the similarity matrix

3. Install Dependencies
```bash
pip install streamlit pandas
```

4. Run the App
```bash
streamlit run <your-script-name>.py
```
💡 How It Works
Loads movie metadata and similarity matrix using pickle
Uses cosine similarity to find top 5 most similar movies
Renders a dropdown for movie selection and displays results upon clicking "Recommend"

📁 Folder Structure
```bash
📂 your_project/
├── app.py                  # Main Streamlit application
├── movie_dict.pkl          # Pickled dictionary with movie data
├── similarity.pkl          # Pickled similarity matrix
└── README.md               # Project description
```
🧠 Example

Select a movie like The Matrix from the dropdown
Click "Recommend"
You'll see 5 similar movies recommended below

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

The recommendations are based on precomputed similarity scores
You must have the .pkl files in the same folder as your .py script
Works with any .pkl-based cosine similarity setup (if formatted correctly)

📌 Dependencies

streamlit
pandas
pickle (built-in)


