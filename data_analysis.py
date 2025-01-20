import pandas as pd


def calculate_average_score(historical_quiz_df):
    # Check if 'score' column exists
    if 'score' in historical_quiz_df.columns:
        historical_quiz_df['score'] = historical_quiz_df['score'].astype(float)
        return historical_quiz_df['score'].mean()
    else:
        print("Score column not found in the DataFrame.")
        return None  # Return None or handle as needed

def identify_weak_areas(historical_quiz_df):
    # Ensure that the DataFrame has the necessary columns
    if 'topic' in historical_quiz_df.columns and 'score' in historical_quiz_df.columns:
        return historical_quiz_df.groupby('topic')['score'].mean().nsmallest(3)
    else:
        print("Required columns are missing in the DataFrame.")
        return None  # Handle as needed

def track_improvement_trends(historical_quiz_df):
    # Ensure that the DataFrame has the necessary columns
    if 'quiz_id' in historical_quiz_df.columns and 'score' in historical_quiz_df.columns:
        return historical_quiz_df.groupby('quiz_id')['score'].mean()  # Change 'quiz_number' to 'quiz_id'
    else:
        print("Required columns are missing in the DataFrame.")
        return None  # Handle as needed