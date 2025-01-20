import pandas as pd
import requests


def fetch_quiz_data(quiz_url):
    try:
        response = requests.get(quiz_url)
        response.raise_for_status()  # Raise an error for bad responses
        return pd.DataFrame(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error fetching quiz data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

def fetch_quiz_submission_data(submission_url):
    try:
        response = requests.get(submission_url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        print("Raw submission data:", data)  # Print the raw data for debugging
        
        # Extract the topic from the nested 'quiz' dictionary
        topic = data['quiz']['topic'] if 'quiz' in data and 'topic' in data['quiz'] else None
        
        # Create a DataFrame and include the topic
        submission_data = {
            'id': data['id'],
            'quiz_id': data['quiz_id'],
            'user_id': data['user_id'],
            'submitted_at': data['submitted_at'],
            'score': data['score'],
            'topic': topic,  # Add the topic here
            # Add other fields as needed
        }
        
        return pd.DataFrame([submission_data])  # Wrap the dictionary in a list
    except requests.exceptions.RequestException as e:
        print(f"Error fetching quiz submission data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error
    except ValueError as ve:
        print(f"Error parsing JSON: {ve}")
        return pd.DataFrame()  # Return an empty DataFrame on error

def fetch_api_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses
        return pd.DataFrame(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error fetching API data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error