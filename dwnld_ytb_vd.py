from pytube import YouTube

link = input("Enter Link: ")

vd1 = YouTube(link)

# print(vd1.title)

streams = vd1.streams.all()
streamlist = list(enumerate(streams))
for i in streamlist:
    print(i)

strm = int(input("Enter the stream to download : "))
streams[strm].download(output_path = './outputs/')
print("Downloaded Successfully !")




