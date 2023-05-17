file_path = r"C:\Users\hakan.aktas\Desktop\7146943_997_01_200323_065009_ORJ_cropped.txt"  # Replace with the actual path to your file
output_file_path = r"C:\Users\hakan.aktas\Desktop\asdadasasd.txt" 

image_width = 640
image_height = 640

# # Open the file in read mode
# with open(file_path, "r") as file, open(output_file_path, "w") as output_file:

#     for line in file:
#         line = line.strip()
#         xmin, ymin, xmax, ymax = None
        
#         for i in range(len(line.split(' '))):
#             if i == 1:
#                 xmin = line.split(' ')[i]
#                 xmin_pixel = xmin * image_width 
#             if i == 2:
#                 ymin = line.split(' ')[i] 
#                 ymin_pixel = ymin * image_height  
#             if i == 3:
#                 xmax = line.split(' ')[i]
#                 xmax_pixel = xmax * image_width
#             if i == 4:
#                 ymax = line.split(' ')[i]
#                 ymax_pixel = ymax * image_height
        
#         modified_line = line.replace("old", "new")

#         # Write the modified line to the output file
#         output_file.write(modified_line + "\n")
        
 # Replace with the actual path to your file

# Read the file and split the lines into columns
with open(file_path, "r") as file:
    # Read all lines and split them into columns
    columns = [line.strip().split() for line in file]

# Transpose the columns using the zip() function
transposed_columns = zip(*columns)

# Access and process each column
for column in transposed_columns:
    # Perform operations on each column
    # You can access the column values here and perform any required operations
    print(column)