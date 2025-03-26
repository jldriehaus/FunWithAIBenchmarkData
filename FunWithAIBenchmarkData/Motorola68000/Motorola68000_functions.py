# File Name : FunWithAIBenchmarkData
# Student Name: Jack Driehaus and Madison Geier
# email:  driehajl@mail.uc.edu & geierml@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   03/27/2025
# Course #/Section:   IS4010-002
# Semester/Year:   spring 2025
# Brief Description of the assignment:  Display an image and some interesting data visualization

# Brief Description of what this module does. Has the functions that visualize the data
# Citations: chatgpt.com and grok.com

# Anything else that's relevant:


# You may have to download the matplotlib and pandas libraries if you do not already have them
import matplotlib.pyplot as plt
import pandas as pd
import os
from PIL import Image

def display_team_image():
        img = Image.open("Motorola68000/Motorola_68000.jpg")
        img.show()

def load_benchmark_data():
    # Path to your .txt file
    data_file = "dataPackage/MMLU/results/MMLU_correct_answers.txt"
    print(f"Current directory: {os.getcwd()}")
    print(f"Looking for file: {data_file}")
    print(f"File exists: {os.path.exists(data_file)}")
    
    try:
        # Load the .txt file (comma-separated)
        data = pd.read_csv(data_file, sep=",", header=None, names=["row_number", "correct_answer"])
        print("Data loaded successfully.")
        print("Columns:", data.columns.tolist())
        print("First few rows:\n", data.head())
        print("Unique answers:", data["correct_answer"].unique())
    except FileNotFoundError:
        print(f"Error: {data_file} not found. Using dummy data.")
        data = pd.DataFrame({
            "row_number": range(1, 104),
            "correct_answer": ["A", "B", "C", "D"] * 26  # Dummy data for 103 rows
        })
    except Exception as e:
        print(f"Error loading data: {e}. Using dummy data.")
        data = pd.DataFrame({
            "row_number": range(1, 104),
            "correct_answer": ["A", "B", "C", "D"] * 26
        })
    return data

def visualize_benchmark_data(data):
    # Count the frequency of each answer
    answer_counts = data["correct_answer"].value_counts()
    print("Answer counts before reindex:\n", answer_counts)
    
    # Reindex to ensure A, B, C, D are all present
    answer_counts = answer_counts.reindex(["A", "B", "C", "D"], fill_value=0)
    print("Answer counts after reindex:\n", answer_counts)
    
    # Calculate percentages
    total_questions = len(data)
    percentages = (answer_counts / total_questions * 100).round(1)
    
    # Create a bar chart
    plt.figure(figsize=(10, 6))
    bars = plt.bar(answer_counts.index, answer_counts.values, 
                   color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"], 
                   edgecolor="black")
    
    # Customize the plot
    plt.title("Frequency of Correct Answers (A, B, C, D)", fontsize=14, pad=20)
    plt.xlabel("Correct Answer", fontsize=12)
    plt.ylabel("Number of Questions", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    
    # Add count and percentage labels on top of bars
    for i, bar in enumerate(bars):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height + 0.5, 
                 f"{int(height)}\n({percentages[i]}%)", 
                 ha="center", fontsize=10)
    
    # Adjust y-axis
    plt.ylim(0, max(answer_counts.values) * 1.2)
    
    # Display the plot
    plt.show()

    

def plot_pie_chart(data):
    # Ensure data is not empty
    if data.empty or "correct_answer" not in data:
        print("No valid data available for pie chart.")
        return
    
    # Count occurrences of each answer
    answer_counts = data["correct_answer"].value_counts()
    
    # Ensure all options (A, B, C, D) are present
    answer_counts = answer_counts.reindex(["A", "B", "C", "D"], fill_value=0)

    # Define colors
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
    
    # Create a pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(answer_counts, labels=answer_counts.index, autopct="%1.1f%%", 
            colors=colors, startangle=140, wedgeprops={"edgecolor": "black"})
    
    # Add a title
    plt.title("Proportion of Correct Answers (A, B, C, D)", fontsize=14, pad=20)
    
    # Display the chart
    plt.show()

# Load data
data = load_benchmark_data()

# Call the function
plot_pie_chart(data)