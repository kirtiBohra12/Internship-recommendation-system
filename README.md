
# 🚀 Internship Recommendation System

A smart web app that helps users discover relevant internships based on their skills or preferred job roles — powered by real-time data from [RemoteOK](https://remoteok.com).

## Open the application in browser

https://internship-recommendation-system.onrender.com/

## 📌 Features

- 🔍 **Search by Skills or Job Role**  
  Enter keywords like "Python", "React", or "Marketing" to find tailored internship listings.

- 🌐 **Data from RemoteOK API**  
  Automatically fetches fresh internship opportunities from the web.

- 📂 **CSV Export**  
  Data is saved locally in `remoteok_internships.csv` for easy access and analysis.

- 🖥️ **Streamlit Web App**  
  Simple, intuitive UI that runs in your browser — works on desktop and mobile.

---

## 📁 Project Structure

    Internship-Recommendation-System/  
    ├── recommendation_system.py # Streamlit app
    ├── fetch_data.py # Fetches data from RemoteOK API 
    ├── remoteok_internships.csv # Internship dataset  
    └── README.md # This file


---

## 🛠️ How to Run

1. **Clone the repository**

```bash
git clone https://github.com/your-username/Internship-Recommendation-System.git
cd Internship-Recommendation-System

pip install -r requirements.txt

streamlit run recommendation_system.py

