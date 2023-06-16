import subprocess

# video_name: str = 'part1.mp4'
# output_name: str = 'output.mp4'

# def process_video(inputVideo, outputVideo):
#     ffmpeg_commands: list = [
#         'ffmpeg',
#         '-i', inputVideo,
#         outputVideo,
#     ]

#     try:
#         subprocess.run(ffmpeg_commands, check=True)
#         print("successfully processed!")
#     except subprocess.CalledProcessError as e:
#         print("Error happened when processing video!")


# process_video(video_name, output_name)




import ffmpeg

stream = ffmpeg.input('part1.mp4')
# stream = ffmpeg.filter(stream, 'fps', fps=25, round='up')
stream = ffmpeg.output(stream, 'dummy.mp4')
ffmpeg.run(stream)


# (
#     ffmpeg
#     .input("part1.mp4")
#     # .hflip()
#     .output('output.mp4')
#     .run()
# )