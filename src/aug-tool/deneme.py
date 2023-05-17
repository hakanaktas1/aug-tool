import dataOpener
import dataAugmentor
import dataSaver
file_path = r"C:\Users\hakan.aktas\Desktop\7146997_997_01_200323_064923_ORJ_cropped.txt"  # Replace with the actual path to your file
output_file_path = r"C:\Users\hakan.aktas\Desktop" 

image_width = 640
image_height = 640

    
if __name__ == '__main__':
    
    label = dataOpener.TxtFileOpener(file_path).data
    aug_label = dataAugmentor.TxtAug(label,15,15,640,640).aug_anotate
    dataSaver.TxtSav(output_file_path, aug_label, "asda")
    