
def counter():
    # Try to open the file, if it doesn't exist, prompt the user
    try:
        with open("sample.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("File 'sample.txt' not found. Please create it by typing a paragraph:")
        with open("sample.txt", "w") as file:
            text = input("Enter your paragraph: ")
            file.write(text)
        # After creating the file, open it again to read
        with open("sample.txt", "r") as file:
            content = file.read()
    
    # Process the text (lowercase, remove punctuation)
    # Remove punctuation
    punctuation = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''
    content = content.lower()  # Convert to lowercase
    for char in punctuation:
        content = content.replace(char, "")  # Remove punctuation

    # Split the content into words
    words = content.split()
    
    # Count word frequencies using a dictionary
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    # Total words
    total_words = sum(word_counts.values())
    
    # Top 5 most common words
    top_5 = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    
    # Display output
    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in top_5:
        print(f"{word} - {count} times")
    
    # Save to "word_count_report.txt"
    with open("word_count_report.txt", "w") as report:
        report.write("Word Count Report\n")
        report.write(f"Total Words: {total_words}\n")
        report.write("Top 5 Words:\n")
        for word, count in top_5:
            report.write(f"{word} - {count}\n")

# Call the counter function
counter()
