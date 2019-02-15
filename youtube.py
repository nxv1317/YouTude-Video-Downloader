from pytube import YouTube

#enter the link from the browser and retrieve all the streams with the resolutions
yt = YouTube(str(input("Enter the video link: ")))
videos = yt.streams.all()

#loop through the videos and assign a number to each video
print(" ")

s = 1
for v in videos:
    print(str(s)+". "+str(v))
    s += 1

#ask the user to enter the number of the specific video to be downloaded
print(" ")

n = int(input("Enter the number of the video: "))
vid = videos[n-1]


#ask the user to enter the area where the file should be downloaded
print(" ")

destination = str(input("Enter the destination: "))

#ask the user to name the file
print(" ")

fileName = str(input("Please enter the name of the file: "))
#begin the download

print(" ")
vid.download(destination, filename=fileName) #download the file to the destination the user entered
print("Download successful.") #print a success message to the user

