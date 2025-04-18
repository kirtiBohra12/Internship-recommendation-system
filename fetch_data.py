import requests
import pandas as pd

def fetch_remoteok_internships():
    api_url = 'https://remoteok.com/api'
    
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()  
    else:
        print("Failed to retrieve data.")
        return []

def save_as_csv(internships, filename='remoteok_internships.csv'):
    if not internships:
        print("No data to save.")
        return
    
    structured_data = []
    for internship in internships:
        internship_info = {
            'Job Description': internship.get('position', 'N/A'),
            'Skill Set': internship.get('tags', 'N/A'),  
            'Link': internship.get('url', 'N/A')
        }
        structured_data.append(internship_info)

    df = pd.DataFrame(structured_data)

    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def main():
    internships = fetch_remoteok_internships()
    
    if internships:
        save_as_csv(internships)
    else:
        print("No internship data available.")

if __name__ == '__main__':
    main()

