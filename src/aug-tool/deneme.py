
from metots import Loop as lp

run = lp()


data_path = r"C:/Users/hakan.aktas/Desktop/save/animal1"
save_path = r"C:/Users/hakan.aktas/Desktop/qwq"

number_of_copy = 2

shift_in_x = 12
shift_in_y = 15

rondom_noise = True
rondom_contrast = True
rondom_sharpness = True
rondom_brihtness = True


run.loop(open_file= data_path,
         save_file=save_path,
         number_of_copy=2,
         shift_x=12,
         shift_y=12,
         random_brightness=rondom_brihtness,
         random_contrast=rondom_contrast,
         random_noise=rondom_noise,
         random_sharpness=rondom_sharpness)