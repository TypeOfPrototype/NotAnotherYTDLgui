# Import the required modules
from gooey import Gooey, GooeyParser
import youtube_dl
import os # Add this line
import sys # Add this line

# Define the Gooey decorator
@Gooey(program_name='YouTube Downloader', 
       program_description='Download videos or audio from YouTube',
       default_size=(600, 400))

# Define the main function
def main():
    # Create a parser object
    parser = GooeyParser()
    # Add the arguments
    parser.add_argument('url', 
                        metavar='YouTube URL', 
                        help='Enter the URL of the video or playlist to be downloaded')
    parser.add_argument('destination', 
                        widget='DirChooser', 
                        metavar='Destination Folder', 
                        help='Choose the folder where the files will be saved')
    parser.add_argument('format', 
                        choices=['Video', 'Audio'], 
                        metavar='Format', 
                        help='Select the format of the output')
    # Parse the arguments
    args = parser.parse_args()
    # Create a youtube-dl options dictionary
    ydl_opts = {}
    # Set the output template
    ydl_opts['outtmpl'] = args.destination + '/%(title)s.%(ext)s'
    # Set the ffmpeg location
    ydl_opts['ffmpeg_location'] = os.path.join(sys._MEIPASS, 'ffmpeg') # Modify this line
    # Set the format option based on the user's choice
    if args.format == 'Video':
        ydl_opts['format'] = 'mp4'
    elif args.format == 'Audio':
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    # Download the video or audio
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([args.url])

# Run the main function
if __name__ == '__main__':
    main()
