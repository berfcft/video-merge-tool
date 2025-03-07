# Video Download & Merge Tool

Video Download & Merge Tool is a Python utility that downloads HLS video segments using the `requests` and `m3u8` libraries and then merges them into a single video file using FFmpeg's concat demuxer. It supports parallel downloads for enhanced speed and lossless merging.

## Features

- **Download:** Fetch HLS video segments (.ts files) using HTTP requests.
- **Parallel Downloads:** Speeds up the process by downloading segments concurrently.
- **Merge:** Combine downloaded segments into one video file without re-encoding via FFmpeg.

## Requirements

- Python 3.x
- FFmpeg (installed and added to your PATH)
- Python packages: `requests`, `m3u8`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/video-download-merge-tool.git
   cd video-download-merge-tool
