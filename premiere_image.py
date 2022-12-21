import premiere

# Connect to Premiere
pr = premiere.Application()

# Open a project
project = pr.OpenProject('C:\\path\\to\\project.prproj')

# Get a reference to the first video track in the project
video_track = project.Tracks[0]

# Create a new sequence
sequence = project.CreateNewSequence()

# Get a reference to the first video track in the sequence
seq_video_track = sequence.VideoTracks[0]

# Import the PNG file
png_file = project.ImportAsset('C:\\path\\to\\image.png')

# Add the PNG file to the sequence as a clip
clip = seq_video_track.AddClip(png_file)

# Set the position of the clip in the sequence
clip.Start = premiere.PTS(0)
clip.End = premiere.PTS(1000)

# Save the project
project.Save()