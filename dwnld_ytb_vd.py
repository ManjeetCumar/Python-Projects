from pytube import YouTube

link = input("Enter Link: ")

vd1 = YouTube(link)

# print(vd1.title)

streams = vd1.streams.all()
# streams = vd1.streams.filter(only_audio= True)
# streams = vd1.streams.filter(only_video= True)
streamlist = list(enumerate(streams))
for i in streamlist:
    print(i)

strm = int(input("Enter the stream to download : "))
streams[strm].download(output_path = './outputs/')
print("Downloaded Successfully !")




