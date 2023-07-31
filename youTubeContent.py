from pytube import YouTube

link = input("Enter the video link : ")
yt = YouTube(link)

vid = yt.streams.all()

for i, stream in enumerate(vid):
    print(f"{i}. {stream}")

strm = int(input("Enter the option: "))
vid[strm].download()
print("Downloaded successfully")