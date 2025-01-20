from data_acquisition import (fetch_api_data, fetch_quiz_data,
                              fetch_quiz_submission_data)
from data_analysis import (calculate_average_score, identify_weak_areas,
                           track_improvement_trends)
from insights import define_student_persona, generate_recommendations
from visualization import plot_average_scores, plot_improvement_trends

# Define API endpoints
quiz_url = "https://www.jsonkeeper.com/b/LLQT"  # Replace with your actual Quiz Endpoint
submission_url = "https://api.jsonserve.com/rJvd7g"  # Replace with your actual Quiz Submission Endpoint
api_url = "https://api.jsonserve.com/XgAgFJ"  # Replace with your actual API Endpoint

# Fetch data
quiz_df = fetch_quiz_data(quiz_url)
submission_df = fetch_quiz_submission_data(submission_url)
api_df = fetch_api_data(api_url)

# Analyze data
average_score = calculate_average_score(submission_df)  # Assuming submission_df contains scores
weak_areas = identify_weak_areas(submission_df)

# Check the submission_df before tracking improvement trends
print("Submission DataFrame:")
print(submission_df.head())  # Print the first few rows to check data

# Verify the data passed to the function
print("Verifying data passed to track_improvement_trends:")
print(submission_df[['quiz_id', 'score']].head())  # Print relevant columns to verify

# Track improvement trends
improvement_trends = track_improvement_trends(submission_df)
print("Improvement Trends:")
print(improvement_trends)  # Print the improvement trends to check if it's empty

# Generate insights
insights = {
    "average_score": average_score,
    "weak_areas": weak_areas.to_dict() if weak_areas is not None else {},
    "improvement_trends": improvement_trends.to_dict() if improvement_trends is not None else {}
}

# Generate recommendations and define student persona
recommendations = generate_recommendations(insights)
student_persona = define_student_persona(insights)

# Print results
print("Insights:")
print(insights)
print("Recommendations:")
print(recommendations)
print(f"Student Persona: {student_persona}")

# Visualize results
plot_improvement_trends(improvement_trends)

# Visualize average scores for weak areas
if weak_areas is not None and not weak_areas.empty:
    plot_average_scores(insights['weak_areas'])  # Pass the weak areas to the plotting function
else:
    print("No weak areas identified for visualization.")