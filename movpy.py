from moviepy.editor import VideoFileClip

clip1_name = '149d5777-ba16-48fa-8abd-a0886feba294.mp4'
clip2_name = 'cb365106-1c9e-43c4-a4a0-ec23872e0453.mp4'
# clip1_name = 'processedVideo.mp4'

clip1 = VideoFileClip(clip1_name)
# clip2 = VideoFileClip(clip2_name)

clip1.write_videofile("processedVideo1.mp4")
# clip2.write_videofile("processedVideo2.mp4")