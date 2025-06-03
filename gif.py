import imageio.v3 as iio
filenames=["photos/WhatsApp Image 2025-06-03 at 18.23.35_833ce82b.jpg","photos/WhatsApp Image 2025-06-03 at 18.23.35_e51f9693.jpg"]
images=[]

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('new.gif',images,duration=500,loop=0)