from  moviepy.editor import *

clip = VideoFileClip(r"D:\HuaweiMoveData\Users\86189\Desktop\picture\last.mp4")
clipInvert_colors = clip.fx(vfx.invert_colors)
clipInvert_colors.write_videofile (r"D:\HuaweiMoveData\Users\86189\Desktop\picture\last_invert.mp4")