# 🎯 Hackathon Idea Generator

AI-powered web app that generates ranked hackathon project ideas near your region campus and turns them into actionable MVP plans.

## Features
- Generate hackathon ideas based on school + interest area
- Looks at Previous Hackathons in region to identify winning patterns
- Ranked by Potential "Winning" score
- Highlighted “Top Pick” recommendation
- Convert ideas into full MVP plans with:
  - core features
  - recommended tech stack
  - implementation steps
  - how to frame/pitch to judges

## Tech Stack
- Python
- Streamlit
- OpenAI API

## How It Actually Works
1. User selects their school and interest area  
2. The app analyzes patterns from strong student hackathon projects  
3. Generates ranked, high-potential ideas  
4. Refines selected ideas into realistic MVP build plans  

## Create .env file in project folder
inside it add OPENAI_API_KEY=your_api_key_here

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
