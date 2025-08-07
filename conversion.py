from osgeo import gdal
import os
import glob


lbl_file = glob.glob( "*.lbl")                                      # Find all .lbl files in the folder
output_path = '../output'
os.makedirs(output_path, exist_ok=True)
for lbl in lbl_file:          
    file_name = os.path.splitext(lbl)[0]                            # To keep the output files' name
    output_tif = os.path.join(output_path, file_name + ".tif")      # Output GeoTIFF filename
    gdal.Translate(output_tif,lbl, format="GTiff")                  # Convert the file to .tif type file
  