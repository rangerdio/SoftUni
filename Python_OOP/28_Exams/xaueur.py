import requests
import tkinter as tk

# Your API key from Metal Price API
API_KEY = '9dc9ceb307753aeb8f883f67c9ce15c9'
URL = 'https://api.metalpriceapi.com/v1/latest'


# Function to get the XAU/EUR rate
def get_xau_eur_rate():
    params = {
        'api_key': API_KEY,
        'base': 'XAU',
        'currencies': 'EUR'
    }
    response = requests.get(URL, params=params)

    if response.status_code == 200:
        data = response.json()
        rate = data['rates']['EUR']  # Get the EUR rate for XAU
        return rate
    else:
        print("Error fetching data:", response.status_code)
        return None


# Update the displayed rate in the Tkinter window
def update_rate():
    rate = get_xau_eur_rate()
    print(rate)
    if rate:
        rate_label.config(text=f"XAU/EUR: {rate:.3f}")
    else:
        rate_label.config(text="Error fetching rate")
    window.after(60000, update_rate)  # Update every 60 seconds


# Create the main window
window = tk.Tk()
window.title("XAU/EUR Real-time Rate")

# Label to display the XAU/EUR rate
rate_label = tk.Label(window, font=("Helvetica", 24), fg="green")
rate_label.pack(padx=20, pady=20)

# Start updating the rate
update_rate()

# Start the Tkinter event loop
window.mainloop()
