import matplotlib.pyplot as plt


def plot_improvement_trends(improvement_trends):
    if improvement_trends is not None and not improvement_trends.empty:
        improvement_trends.plot(kind='line', marker='o')
        plt.title('Improvement Trends Over Quizzes')
        plt.xlabel('Quiz ID')
        plt.ylabel('Average Score')
        plt.xticks(rotation=45)
        plt.grid()
        plt.show()
    else:
        print("No improvement trends to display.")

def plot_average_scores(weak_areas):
    topics = list(weak_areas.keys())
    scores = list(weak_areas.values())

    plt.bar(topics, scores, color='skyblue')
    plt.title('Average Scores by Topic')
    plt.xlabel('Topics')
    plt.ylabel('Average Score')
    plt.xticks(rotation=45)
    plt.ylim(0, max(scores) + 10)  # Set y-axis limit to be a bit higher than the max score
    plt.show()