import tkinter as tk
from datetime import datetime
import news
import weather



def exit_fullscreen(event=None):
    # Press ESC to exit full screen
    root.attributes('-fullscreen', False)
def enter_fullscreen(event=None):
    #press f to enter fullscreen
    root.attributes('-fullscreen', True)
# Function to update time
def update_time():
    current_time = datetime.now().strftime("%I:%M:%S %p")
    time_label.config(text=current_time)
    root.after(1000, update_time)

# Function to update weather and news every 30 minutes
def update_content():
    weather_label.config(text=weather.getWeather())
    headlines = news.get_news()
    news_text = "\n".join(headlines)
    news_label.config(text=news_text)
    root.after(45 * 60 * 1000, update_content)  # Update every 45 minutes as to not get charged

root = tk.Tk()
root.configure(bg='black')
root.title("Smart Mirror")
# Enable full-screen mode
root.attributes('-fullscreen', True)
# (Optional) Bind the Escape key to exit full-screen mode
root.bind("<Escape>", exit_fullscreen)
root.bind('f', enter_fullscreen)
root.geometry("800x800")

# Time display
time_label = tk.Label(root, font=("Helvetica", 48), fg="white", bg="black")
time_label.place(relx=0.2, rely= 0.1, anchor="n")
update_time()


#weather display
weather_label = tk.Label(root, font=("Helvetica", 24), fg="white", bg="black")
weather_label.place(relx=0.9, rely= 0.1, anchor="se")


#news display
news_label = tk.Label(root, font=("Helvetica", 18), fg="white", bg="black", justify="left")
news_label.place(relx= 0.1, rely= 0.9, anchor="sw")



update_content()

root.mainloop()
