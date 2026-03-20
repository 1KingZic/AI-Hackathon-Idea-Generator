import os
from openai import OpenAI
from sample_projects import sample_projects
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def filter_projects_by_location(location: str):
    location = location.lower().strip()
    matched = []

    for project in sample_projects:
        project_location = project["location"].lower()
        if location in project_location or project_location in location:
            matched.append(project)

    if not matched:
        matched = sample_projects[:5]

    return matched


def build_context(projects):
    lines = []
    for idx, project in enumerate(projects, start=1):
        lines.append(
            f"{idx}. {project['name']} | {project['hackathon']} | {project['theme']} | {project['description']}"
        )
    return "\n".join(lines)


def generate_hackathon_ideas(school_name: str, location: str, interest_area: str):
    relevant_projects = filter_projects_by_location(location)
    context = build_context(relevant_projects)
    prompt = f"""
You are a hackathon strategy assistant.

Student school: {school_name}
Student location: {location}
Preferred interest area: {interest_area}

Past strong hackathon-style projects:
{context}

Return ONLY valid JSON in this exact structure:

{{
  "patterns": ["pattern 1", "pattern 2", "pattern 3"],
  "ideas": [
    {{
      "name": "Idea name",
      "pitch": "One-sentence pitch",
      "why_it_could_rank": "Why judges may like it",
      "Potential_score": 8,
      "difficulty": "Easy"
    }}
  ]
}}

Rules:
- Include exactly 5 ideas
- Potential_score must be an integer from 1 to 10
- difficulty must be Easy, Medium, or Hard
- Make ideas realistic for a 24-48 hour student hackathon
- Do not include markdown
- Do not include explanation outside the JSON
"""
    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return response.output_text

def refine_top_idea(idea_name: str, idea_pitch: str, school_name: str, location: str):
    prompt = f"""
You are helping a student turn a hackathon idea into a strong 24-48 hour MVP.

School: {school_name}
Location: {location}

Top idea:
Name: {idea_name}
Pitch: {idea_pitch}

Return ONLY valid JSON in this exact structure:

{{
  "mvp_title": "string",
  "core_problem": "string",
  "target_users": "string",
  "must_have_features": ["feature 1", "feature 2", "feature 3"],
  "nice_to_have_features": ["feature 1", "feature 2"],
  "tech_stack": ["tool 1", "tool 2", "tool 3"],
  "implementation_plan": [
    "Step 1",
    "Step 2",
    "Step 3",
    "Step 4"
  ],
  "judge_pitch": "string"
}}

Rules:
- Keep it realistic for beginner/intermediate students
- Prefer simple tools like Python, Streamlit, SQLite, Firebase, or basic APIs
- Focus on what can actually be built in 24-48 hours
- Do not include markdown
- Do not include explanation outside the JSON
"""

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    return response.output_text

    