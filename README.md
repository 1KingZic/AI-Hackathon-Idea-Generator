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

## Simple Demo
Example input - Georgia State University as school, Fintech as interest area

Outputs -

<img width="728" height="953" alt="image" src="https://github.com/user-attachments/assets/f6e457d0-a085-48b8-aee0-10b90656ff20" />
<img width="809" height="913" alt="image" src="https://github.com/user-attachments/assets/ff935bb6-a4c4-4bbf-a4c5-784cca8e114d" />
<img width="819" height="761" alt="image" src="https://github.com/user-attachments/assets/f5163112-fabe-4597-ab3c-53cec604a21a" />
<img width="804" height="532" alt="image" src="https://github.com/user-attachments/assets/2325a3ed-6080-498d-9321-2bc3772a6625" />




## To Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
