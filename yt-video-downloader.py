# importing the module 
import os
from pytube import YouTube 

# Functions
def set_filename(save_folder, save_filename, save_extension):

    save_full_filename = os.path.join(save_folder, save_filename + '.' + save_extension)
    
    return save_full_filename

# Saving parameters
save_folder = 'data/input-video'
save_filename = 'gangnam_style_dance_class'
save_extension = 'mp4'
save_full_filename = set_filename(save_folder, save_filename, save_extension)

# link of the video to be downloaded 
link="https://www.youtube.com/watch?v=xWOoBJUqlbI"
  
try: 
    # Creating YouTube object
    yt = YouTube(link) 
except: 
    print("Connection Error") #to handle exception 
  
try: 
    # downloading highest resolution video from mp4 files available
    where_downloaded_file_is = yt.streams.filter(file_extension='mp4').get_highest_resolution().download(filename=save_full_filename)
    print('The downloaded file is in:', where_downloaded_file_is)
except: 
    print("Some Error!") 
print('Task Completed!')