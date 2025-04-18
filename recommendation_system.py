import pandas as pd
import streamlit as st

def load_data():
    data = pd.read_csv('remoteok_internships.csv')
    return data


def recommend_internships(search_input, data):
    search_input = search_input.lower()
    
    results = data[
        data['Job Description'].str.lower().str.contains(search_input) |
        data['Skill Set'].str.lower().str.contains(search_input)
    ]
    return results

def main():
    data = load_data()

    st.title("🚀 Internship Finder")
    st.markdown("Find internships based on your skills or dream job role.")
    
    search_input = st.text_input("🔍 Search internships by skill or job role:", placeholder="e.g., Python, Data Analyst, Marketing")

    if search_input:
        results = recommend_internships(search_input, data)
        
        if not results.empty:
            st.write('Found the following internships:')
            
            for index, row in results.iterrows():
                st.write(f"**Job Description:** {row['Job Description']}")
                st.write(f"**Skills Required:** {row['Skill Set']}")
                st.write(f"[Apply Here]({row['Link']})")
                st.write("---")
        else:
            st.write('No internships found matching your search criteria.')
    else:
        st.write('Please enter some skills or job description to search for internships.')

if __name__ == '__main__':
    main()
