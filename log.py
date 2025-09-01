
import glob
import os

#filePath = f'../../../../../../../Volumes/Seagate\ Bac/BlueberryOnMars/{NO}'

yes = f'../../../../../../Volumes/SeagateBac/BlueberryOnMars/Yes/'               # Find all .tif files in the Yes folder
no =  f'../No/'                                                                  # Find all .tif files in the No folder
suspect = f'../Suspect'                                                          # Find all .tif files in the Suspect folder

Paths = [yes, no, suspect]
contain = ['Yes','No','Suspect']
with open ('log.csv', 'w') as f:
    f.write('File Name, Sol, Camera, Spherules\n')
                                                          
    for i in range(len(Paths)):
        os.chdir(Paths[i])                                                      # change the direction to data location
        tifs = glob.glob('*.tif')                                               # read all the tif files
        for tif in tifs:
            tiff = os.path.splitext(tif)[0]                                     # To remove file type and prepare for File Name, Sol, Camera, Spherules
            f.write(f'{tif}, {tiff[0:4]}, {tiff[4:6]}, {contain[i]} \n')
        
   



