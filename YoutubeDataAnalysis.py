from googleapiclient.discovery import build

# Replace with your own API key
API_KEY = 'API_KEY_WILL_PASTED_HERE'

# Function to extract video ID from URL (Simplified)
def extract_video_id(video_url):
    if "v=" in video_url:  # Check if URL contains 'v='
        video_id = video_url.split("v=")[1]  # Get the part after 'v='
        video_id = video_id.split("&")[0]  # In case there is extra query parameter, take the first part
        return video_id
    else:
        return None

# Function to get video details
def get_video_details(video_url):
    video_id = extract_video_id(video_url)  # Extract video ID
    if not video_id:
        print("Invalid YouTube video URL.")
        return

    # Connect to YouTube API
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    # Get video details
    request = youtube.videos().list(part='snippet,statistics', id=video_id)
    response = request.execute()

    # Display the video details
    if 'items' in response and response['items']:
        video = response['items'][0]
        title = video['snippet']['title']
        channel = video['snippet']['channelTitle']
        description = video['snippet']['description']
        views = video['statistics']['viewCount']
        likes = video['statistics'].get('likeCount', 'N/A')  # If likeCount is not available, return 'N/A'
        comments = video['statistics'].get('commentCount', 'N/A')  # If commentCount is not available, return 'N/A'

        print(f"Title: {title}")
        print(f"Channel: {channel}")
        print(f"Views: {views}")
        print(f"Likes: {likes}")
        print(f"Comments: {comments}")
        print(f"Description: {description}")
    else:
        print("Video not found.")

# Example usage
video_link = input("Enter YouTube video link: ")
get_video_details(video_link)
