class Utils:
    @staticmethod
    def print_help_message():
        help_message = """
Usage: felis [-clone URL, -y, -g, -git, -repo, -s, -mp3, -mp4]

Options:
-y: Show usage and parameters.
-g: Check for updates.
-git: Switch to tool search mode on Github.
-repo: Switch to tool search mode on Kali Linux and Parrot Linux repositories.
-s: Delete Felis.
-clone: Tool download parameter.
-mp3 <song_name>: Download the mp3 file of the given song.
-mp4 <song_name>: Download the mp4 file of the given song.

The clone parameter must be for a file with a .zip, .deb, or .tar.gz extension. You can also use the clone parameter 
to download repositories from GitHub.

<======KernelBlog.org======>
KernelBlog Developer Team
"""
        print(help_message)
