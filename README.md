# NotAnotherYTDLgui
Extremely Simple Youtube-dl Gui using Gooey https://github.com/chriskiehl/Gooey   
 &amp; ready to be packaged with Pyinstaller https://github.com/pyinstaller/pyinstaller    
   
 The python script itself will load a very simple gui if the python dependencies are already installed  
 The packaging allows it to be self contained and distributed to friends/family that need something simple. 0 install as it is all included in the packaged binary for the respective OS courtesy of pyinstaller.  
   
Enter URL, Provide Destination folder for download using either Browse button file picker or typed  
and lastly click format dropdown to select Video or Audio (Best Quality MP4/MP3 will be retrieved)

![NAYTDLGUIMain](https://github.com/TypeOfPrototype/NotAnotherYTDLgui/assets/37871605/8ad3b2c6-fad6-43d5-89d9-4f08e32762a6)  
![NAYTDLGUIStatus](https://github.com/TypeOfPrototype/NotAnotherYTDLgui/assets/37871605/22e73539-bac4-4a43-a6ba-de388b8bb3d6)


## Dependencies **Important - Please install latest youtube-dl from github as pip seems to have issues
https://github.com/ytdl-org/youtube-dl/issues/31530#issuecomment-1435477247  
  
pip install --upgrade --force-reinstall "git+https://github.com/ytdl-org/ytdl-nightly.git"  
& pip install Gooey  
  
**Optionally if you'd like to package also install pyinstaller  
pip install pyinstaller    
  
& ffmpeg binaries https://ffmpeg.org/download.html  

## Packaging 
from the project folder ensure ffmpeg subfolder has unpacked ffmpeg binaries  
  
pyinstaller NotAnotherYTDLgui.py --add-binary="ffmpeg/*;ffmpeg" --onefile   
  
This will produce a single binary to use depending on your OS (Currently tested on windows only...)
