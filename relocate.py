import re
import os
import shutil

base_dir = 'C:/Users/ulf/Downloads/TvShows'
files = [f for f in os.listdir(base_dir) if os.path.isfile(os.path.join(base_dir, f))]
for file in files:
    show = re.findall(r"""(.*)          # Title
                           [ .]
                           S(\d{1,2})    # Season
                           E(\d{1,2})    # Episode
                           [ .a-zA-Z]*  # Space, period, or words like PROPER/Buried
                           (\d{3,4}p)?   # Quality
                       """, file, re.VERBOSE)
    if len(show) > 0:
        print("---------- TV ----------")
        print("Show: " + show[0][0].replace(".", " "))
        print("Season: " + str(int(show[0][1])))
        print("Episode: " + str(int(show[0][2])))
        print("Quality: " + (show[0][3] if len(show[0][3]) > 0 else "nonHD"))
        print("Relocating")
        targetPath =  show[0][0].replace(".", " ")+ "/Season "+str(int(show[0][1])) + "/"+file
        print('C:/Users/ulf/Downloads/TvShows/'+ file + " TO : " + 'Y:/'+targetPath)

        shutil.move('C:/Users/ulf/Downloads/TvShows/'+ file, 'Y:/' + targetPath)
    else:
        print('error')


