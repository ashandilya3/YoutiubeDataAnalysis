# YouTube Video Details Extractor

A simple Python tool that extracts detailed information about a YouTube video by utilizing the **YouTube Data API v3**. The tool fetches information like video title, channel name, views, likes, comments, and description. 

## Features

- Extracts **video title**, **channel name**, **views**, **likes**, **comments**, and **description**.
- Supports video links in the format: `https://www.youtube.com/watch?v=VIDEO_ID`.
- Uses the **Google API Client** to interact with the **YouTube Data API v3**.
- Fetches and displays video data in a user-friendly format.

## Requirements

Before running the script, you need to have the following:

1. **Python 3.x** installed on your system.
2. A **Google API key** for the YouTube Data API v3.

## Installation

### Step 1: Install Required Libraries

First, ensure you have the required libraries installed. You can install them using `pip`.

```bash
pip install google-api-python-client
