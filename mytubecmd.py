from pytube import YouTube
from pytube import Playlist
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip



import os

Continue=True
def download_vid(link,resu):
    try:
        y=YouTube(link,on_complete_callback=print("download complete"))
        try:
        
            stream = y.streams.filter(resolution=resu,progressive=True)
            print(stream.first().title)
            video=stream.first().download()
            vid=os.path.abspath(video)
            
        except:
            audio_stream = y.streams.filter(only_audio=True)
            name=audio_stream.first().title
            out_file=audio_stream.first().download()
            base, ext = os.path.splitext(out_file)
            
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            audio_path=os.path.abspath(new_file)
            
            vid_stream = y.streams.filter(resolution=resu)
            vid=vid_stream.first().download()
            vid_path=os.path.abspath(vid)
            
            audio1 = AudioFileClip(audio_path)
            clip2 = VideoFileClip(vid_path)
            clip2.audio = audio1
            print(name)
            clip2.write_videofile("temp_name.mp4")
            vid=rename_file(name)
            os.remove(audio_path)
            os.remove( vid_path )
           
            
    except:
        print("invalid url")
    return vid
def rename_file(nam="" ,file="",count='' ,tr=0):
    if tr !=0:
        base= os.path.basename(file)
        new_file = f"{count}-{base}" 
        os.rename(file, new_file)
    else:
        for l in nam:
            if l in ['"',"<",">","|","*","?","\\","/",":"]:
                new=nam.replace(l," ")
            else:
                new=nam
        os.rename(os.path.abspath("temp_name.mp4"),f'{new}.mp4')
        return os.path.abspath(f'{new}.mp4')
    
            
while Continue:
    #print("welcome to mytube")
    answer=input("type v to download a video or p for a playlist \n")
    if answer=="v":
        ext=input("type 3 for mp3 or 4 for mp4\n")
        if ext == "3":
            url=input("please inter video url\n")
            yt=YouTube(url)
            stream=yt.streams.filter(only_audio=True)
            out_file=stream.first().download()
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            
        elif ext=="4":
            url=input("please enter video url\n")
            r=input("type video resolution  \n")
            res=f"{r}p"
            download_vid(url,res)
            
    elif answer=="p":
        url=input("please enter playlist url\n")
        p=Playlist(url)
        r=input("type video resolution  \n")
        res=f"{r}p"
        cuont=0
        num=int(input("start with video number   \n"))
        for i in p.video_urls:
            if num==cuont:
                na=download_vid(i,res)
                rename_file(file=na,count=cuont,tr=2)
                num+=1
            cuont+=1
            
            
    else:
        print("invalid answer")
    
    