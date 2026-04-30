import requests

def get_top_stories():
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    story_ids = requests.get(url).json()

    top_10 = story_ids[:10]

    for story_id in top_10:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story = requests.get(story_url).json()

        print("-", story.get("title"))

if __name__ == "__main__":
    get_top_stories()
