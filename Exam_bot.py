import os
import requests
import pandas as pd
import fitz
import time
from datetime import datetime

# Telegram bot token and channel chat_id
token = "7908477619:AAEGzl1w_UHNolSiS1o7J4TRXdx0y7E1_wU"  # Bot token
chat_id = "@Books_exam"  # Channel username

# Folders for books and screenshots
books_folder = "Books"  # The folder containing PDF books
output_folder = "Screenshots"  # Folder to save screenshots

# Create the screenshots folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get a list of books in the folder
books = [f for f in os.listdir(books_folder) if f.endswith(".pdf")]

# Create a DataFrame to store book information with new structure
df = pd.DataFrame(columns=["ID", "File Name", "Status", "Time"])

# Function to capture the first page of a PDF as an image
def get_first_page_screenshot(pdf_path, output_folder):
    try:
        # Open the PDF file
        doc = fitz.open(pdf_path)
        
        # Load the first page (index 0 means the first page)
        page = doc.load_page(0)
        
        # Render the page as an image
        pix = page.get_pixmap(dpi=400)
        
        # Save the image
        image_path = f"{output_folder}/{os.path.basename(pdf_path).replace('.pdf', '.png')}"
        pix.save(image_path)
        
        print(f"Screenshot saved: {image_path}")
        return image_path
    except Exception as e:
        print(f"Error capturing screenshot for {pdf_path}: {e}")
        return None

# Function to send an image to Telegram channel
def send_photo(token, chat_id, photo_path):
    try:
        url = f"https://api.telegram.org/bot{token}/sendPhoto"
        with open(photo_path, "rb") as photo:
            files = {"photo": photo}
            payload = {"chat_id": chat_id}
            response = requests.post(url, data=payload, files=files)
        return response.json()
    except Exception as e:
        print(f"Error sending image: {e}")
        return None

# Function to send a file as a reply to an image message
def send_document_as_reply(token, chat_id, document_path, reply_to_message_id):
    try:
        url = f"https://api.telegram.org/bot{token}/sendDocument"
        with open(document_path, "rb") as document:
            files = {"document": document}
            payload = {"chat_id": chat_id, "reply_to_message_id": reply_to_message_id}
            response = requests.post(url, data=payload, files=files)
        return response.json()
    except Exception as e:
        print(f"Error sending file: {e}")
        return None

# Main process
for idx, book in enumerate(books):
    pdf_path = os.path.join(books_folder, book) # f"books_folder/{book}"
    status = "Failed"
    time_sent = None
    
    try:
        # Capture the first page screenshot
        screenshot_path = get_first_page_screenshot(pdf_path, output_folder)
        
        if screenshot_path:
            # Send the screenshot to the Telegram channel
            photo_response = send_photo(token, chat_id, screenshot_path)
            
            if photo_response and "result" in photo_response:
                message_id = photo_response["result"]["message_id"]
                
                # Send the PDF file as a reply to the image
                document_response = send_document_as_reply(token, chat_id, pdf_path, message_id)
                
                # Only mark as "Sent" if both the photo and document were successfully sent
                if document_response and "result" in document_response:
                    status = "Sent"
                    time_sent = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"{book} successfully sent!")
                else:
                    print(f"Error sending document for {book}.")
                    status = "Failed"
            else:
                print(f"Failed to send screenshot for {book}.")
                status = "Failed"
        else:
            print(f"Failed to capture screenshot for {book}.")
            status = "Failed"
    except Exception as e:
        print(f"Error sending {book}: {e}")
        status = "Failed"
    
    # Append the results to the DataFrame using pd.concat()
    df = pd.concat([df, pd.DataFrame([{
        "ID": idx + 1,
        "File Name": book,
        "Status": status,
        "Time": time_sent if time_sent else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }])], ignore_index=True)
    
    # Delay to comply with Telegram API rate limits
    time.sleep(1)  # Wait for 1 second

# Save the report as a CSV file
df.to_csv("books_report.csv", index=False)
print("Report saved as: books_report.csv")

