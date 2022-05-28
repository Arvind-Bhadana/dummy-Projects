from pytube import YouTube
from pytube import Playlist

print('For single video press 1 and for playlist press 2')

user_need = int(input('enter your choice here : '))

if user_need==1 :
    link = input('past the link of youtube video here :')
    youtube1 = YouTube(link)
    print(youtube1.title)
    print(youtube1.thumbnail_url)
    video = youtube1.streams.all()
    vid = list(enumerate(video))
    for i in vid:
         print(i)
    userinput = int(input('select the video quality : '))
    video[userinput].download()
    print('successfully complete')

elif user_need ==2:
    link = input('enter the playlist url: ')
    py = Playlist(link)
    print(f'Downloading : {py.title}')
    for video in py.videos:
        video.streams.first().download()

else:
    print('please enter a valid option')











