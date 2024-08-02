data = []
rating = []

def read_files(all_files):
    for file_name in all_files:
        try:
            with open(file_name, 'r') as f:
                data.extend(f.readlines())
        except FileNotFoundError:
            print(f"File not found: {file_name}")
    return data

def separate(data_lines):
    ratings = []
    for line in data_lines:
        parts = line.split(':')
        if len(parts) > 1:
            ratings.append(float(parts[1].split('-')[0]))
    return ratings

def get_ratings(file):
    feedbacks = file.readlines()
    return feedbacks

try:
    files = ["feedback1.txt", "feedback2.txt", "feedback3.txt"]
    all_feedbacks = read_files(files)
    ratings = separate(all_feedbacks)
    
    total_sum = sum(ratings)
    average_rating = total_sum / len(ratings) if ratings else 0
    
except FileNotFoundError:
    print("One or more files not found")

def summary_file():
    try:
        with open("feedback_summary.txt", 'w') as fs:
            fs.write(f"Total Feedback Entries: {len(ratings)}\n")
            fs.write(f"Average Rating: {round(average_rating, 2)}\n")
            fs.write("\nFeedbacks:\n")
            for feedback in all_feedbacks:
                fs.write(f"{feedback}\n")
    except Exception as e:
        print("Error:", e)

# Generate the summary file
summary_file()
