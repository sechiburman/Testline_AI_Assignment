def generate_recommendations(insights):
    recommendations = []
    
    if insights['average_score'] < 50:
        recommendations.append("Focus on improving your overall score by revisiting fundamental topics.")
    
    for topic, score in insights['weak_areas'].items():
        recommendations.append(f"Consider revising the topic: {topic} where your average score is {score:.2f}.")
    
    return recommendations

def define_student_persona(insights):
    if insights['average_score'] >= 75:
        return "High Achiever"
    elif insights['average_score'] >= 50:
        return "Average Performer"
    else:
        return "Struggling Learner"