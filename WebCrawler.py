import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs, urljoin
import csv
import tkinter as tk
from tkinter import messagebox, filedialog

# --- Web Crawling Functions ---

def crawl(url, domain, visited, parameters_data, max_pages, status_label):
    queue = [url]
    
    while queue and len(visited) < max_pages:
        current_url = queue.pop(0)
        
        if current_url in visited:
            continue

        try:
            if status_label:
                status_label.config(text=f"Crawling: {current_url}")
                status_label.update()

            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            response = requests.get(current_url, headers=headers, timeout=5)
            if response.status_code != 200:
                continue

            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.find_all('a', href=True)

            parsed_url = urlparse(current_url)
            params = parse_qs(parsed_url.query)
       #     if params:
        #        parameters_data.append({
         #           'url': current_url,
          #          'parameters': params
           #     })
            
            params = parse_qs(parsed_url.query)
            parameters_data.append({
                'url': current_url,
                'parameters': params if params else {}
            })


            visited.add(current_url)

            for link in links:
                absolute_url = urljoin(current_url, link['href'])
                parsed_link = urlparse(absolute_url)

                # Only add internal links
                if parsed_link.netloc == domain and absolute_url not in visited and absolute_url not in queue:
                    queue.append(absolute_url)

        except Exception as e:
            print(f"Error crawling {current_url}: {e}")

def save_to_csv(data, filepath):
    try:
        with open(filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["URL", "Parameters"])

            for item in data:
                param_string = "; ".join([f"{key}={','.join(value)}" for key, value in item['parameters'].items()])
                writer.writerow([item['url'], param_string])
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False

def start_crawling(url, max_pages, filepath, status_label):
    visited = set()
    parameters_data = []

    parsed_start_url = urlparse(url)
    domain = parsed_start_url.netloc

    crawl(url, domain, visited, parameters_data, max_pages, status_label)

    success = save_to_csv(parameters_data, filepath)
    return success

# --- GUI Functions ---

def browse_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")],
        title="Choose file location"
    )
    if file_path:
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(0, file_path)

def start_crawl_gui():
    url = url_entry.get()
    pages = pages_entry.get()
    filepath = file_path_entry.get()

    if not url:
        messagebox.showwarning("Input Error", "⚠️ Please enter a valid URL.")
        return

    if not filepath:
        messagebox.showwarning("Input Error", "⚠️ Please choose a file location to save output.")
        return

    try:
        pages = int(pages)
        if pages <= 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Input Error", "⚠️ Please enter a valid positive number for pages.")
        return

    try:
        status_label.config(text="Starting crawl...")
        status_label.update()
        success = start_crawling(url, pages, filepath, status_label)
        if success:
            status_label.config(text="✅ Crawling Completed!")
            messagebox.showinfo("Success", f"✅ Crawling Completed!\nFile saved as:\n{filepath}")
        else:
            status_label.config(text="❌ Failed to save file.")
            messagebox.showerror("File Error", "❌ Could not save the output file.\nPlease check the path and try again.")
    except Exception as e:
        messagebox.showerror("Error", f"❌ An error occurred: {e}")

# --- GUI Setup ---

root = tk.Tk()
root.title("Simple Web Crawler Tool")

tk.Label(root, text="Enter Start URL:", font=('Arial', 12)).pack(pady=5)
url_entry = tk.Entry(root, width=50, font=('Arial', 12))
url_entry.pack(pady=5)

tk.Label(root, text="Enter Number of Pages to Crawl:", font=('Arial', 12)).pack(pady=5)
pages_entry = tk.Entry(root, width=10, font=('Arial', 12))
pages_entry.pack(pady=5)
pages_entry.insert(0, "5")  # Default to 5 pages

tk.Label(root, text="Select Output File Location:", font=('Arial', 12)).pack(pady=5)
file_path_frame = tk.Frame(root)
file_path_frame.pack(pady=5)

file_path_entry = tk.Entry(file_path_frame, width=38, font=('Arial', 11))
file_path_entry.pack(side=tk.LEFT, padx=(0, 5))
browse_button = tk.Button(file_path_frame, text="Browse", command=browse_file)
browse_button.pack(side=tk.LEFT)

crawl_button = tk.Button(root, text="Start Crawl", command=start_crawl_gui, font=('Arial', 12), bg="lightblue")
crawl_button.pack(pady=15)

status_label = tk.Label(root, text="", font=('Arial', 10))
status_label.pack(pady=5)

root.geometry("500x380")
root.mainloop()
