# AI Trend Finder

This project collects trending topics from multiple public data sources and uses AI to identify emerging trends and generate blog ideas.

## Data Sources
- Google Trends (search interest over time)
- Hacker News (tech news and discussions)

## Features (MVP)
- Fetch trending search terms from Google Trends
- Retrieve top posts from Hacker News
- Combine signals into a simple trend list

## Goal
To build an AI-assisted system that helps identify content ideas for blogging based on real-world trend data.

## Tech Stack
- Python
- Google Trends API (pytrends)
- Hacker News public API

## Next Steps
- Add AI summarisation (LLM)
- Score trends based on engagement
- Generate blog post ideas automatically

## How to Run

1. Install dependencies:
   pip install pytrends requests

2. Run script:
   python main.py
