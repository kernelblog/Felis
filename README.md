# Felis

Felis is a versatile downloader tool, designed to simplify the process of downloading various types of media, updating tools, and managing downloads efficiently.

## Installation

Clone the repository and run the installation script:

```bash
git clone https://github.com/kernelblog/felis.git --depth=1
cd felis
sudo ./setup.sh
```

## Prerequisites

Felis requires **ffmpeg** for processing multimedia files. Ensure it's installed on your system.
> If you have any ssl issues, run: `pip install pyopenssl --upgrade`

## Usage

Felis has been refactored to a more modular design, introducing a command-driven approach for better usability and maintainability. Here's a quick overview:

- **Help**: `felis -y` shows usage and parameters.
- **Update**: `felis -g` checks for updates.
- **Remove**: `felis -s` deletes Felis.
- **Download Music**: `felis -mp3 <song_name>` downloads the specified song as a MP3 file.
- **Download Video**: `felis -mp4 <song_name>` downloads the specified video as a MP4 file.
- **Git Mode**: `felis -git` switches to tool search mode on GitHub.
- **Repository Mode**: `felis -repo` searches tools on Kali Linux and Parrot Linux repositories.
- **Clone Tool**: `felis -clone <URL>` downloads tools from a specified URL. Supports .zip, .deb, or .tar.gz files, or git repositories.

## Project Website

For more information, visit [Felis Project Website](https://felis.kernelblog.org).

## Contact

For support or queries, reach out to us:

- Website: [www.kernelblog.org](https://www.kernelblog.org)
- Email: <info@kernelblog.org>, <emre@kernelblog.org>
- Telegram: [KernelBlog](https://www.t.me/kernelblog), [Kernel_Blog](https://www.t.me/kernel_blog)
