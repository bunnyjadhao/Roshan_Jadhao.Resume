"""Data Science Portfolio - Roshan Jadhao
Run locally:  python app.py
Render start: gunicorn app:app
"""
import os
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

PROFILE = {
    "name": "Roshan Jadhao",
    "title": "Aspiring Data Scientist | AI/ML Enthusiast",
    "location": "Pune, Maharashtra, India",
    "email": "roshanjadhao267@gmail.com",
    "phone": "+91 7083940298",
    "github": "https://github.com/bunnyjadhao",
    "linkedin": "https://www.linkedin.com/in/roshan-jadhao-257b33344/",
    "summary": (
        "Information Technology engineer with hands-on exposure to data preprocessing, "
        "exploratory analysis, machine learning and model evaluation. I enjoy turning data "
        "into useful products - from computer-vision systems to analytics dashboards."
    ),
    "education": {
        "degree": "B.E. in Information Technology",
        "school": "Mumbai University, Atharva College of Engineering",
        "period": "Dec 2022 - Jun 2026",
        "cgpa": "7.16 / 10",
        "coursework": [
            "Data Structures & Algorithms", "DBMS", "Data Analysis", "Statistics",
            "Python Programming", "OOP", "AI & Machine Learning", "Web Development",
        ],
    },
    "experience": [
        {
            "role": "AI/ML with Data Science Intern",
            "org": "YBI Foundation",
            "period": "Mar 2025 - Apr 2025",
            "mode": "Virtual",
            "points": [
                "Completed a 1-month internship specializing in Data Science and data-driven problem solving.",
                "Hands-on exposure to AI/ML algorithms, data preprocessing and model evaluation techniques.",
                "Learned data analysis workflows and industry-level practices.",
            ],
        },
        {
            "role": "Cloud Security Intern",
            "org": "EduSkills (AICTE)",
            "period": "Jan 2025 - Feb 2025",
            "mode": "Virtual",
            "points": [
                "Worked on cloud security projects under the guidance of industry experts.",
                "Earned Course Completion and Internship Certificates from AICTE and EduSkills.",
            ],
        },
    ],
    "projects": [
        {
            "name": "Drowsiness Detection System",
            "date": "Feb 2024",
            "stack": ["Python", "OpenCV", "Machine Learning", "Deep Learning"],
            "desc": (
                "Real-time driver fatigue detection using Eye Aspect Ratio (EAR) and facial "
                "landmark detection with OpenCV, triggering alerts when drowsiness is detected."
            ),
            "link": "https://github.com/bunnyjadhao",
        },
        {
            "name": "Social Media Manager",
            "date": "Jun 2025",
            "stack": ["React", "Node.js", "Express", "MongoDB", "APIs"],
            "desc": (
                "Platform for posting images and analysing engagement across multiple networks, "
                "with real-time analytics for likes, shares, comments and impressions."
            ),
            "link": "https://github.com/bunnyjadhao",
        },
        {
            "name": "Bike Rental Management System",
            "date": "May 2023",
            "stack": ["PHP", "MySQL", "HTML", "CSS"],
            "desc": (
                "Web app for bike booking with user registration, availability tracking, "
                "rental booking and payment management."
            ),
            "link": "https://github.com/bunnyjadhao",
        },
    ],
    "skills": {
        "Data Science": ["Pandas", "NumPy", "Matplotlib", "Data Preprocessing", "Data Analysis",
                         "Data Visualization", "Machine Learning"],
        "Languages": ["Python", "SQL", "Java", "C", "C++", "JavaScript", "PHP"],
        "Web & APIs": ["React", "Node.js", "Express.js", "MongoDB", "Next.js", "REST APIs", "Postman"],
        "Tools": ["VS Code", "Eclipse", "Android Studio", "Google Cloud Platform"],
    },
    "certifications": [
        "Skill India - AI For India 2.0",
        "Great Learning - Front End Development (HTML)",
        "Udemy - Java and C++ Complete Course for Beginners",
        "Scaler Topics - MySQL and Database Design Course",
    ],
}

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{ p.name }} | Data Science Portfolio</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
<style>
  :root { --c1:#667eea; --c2:#764ba2; --c3:#f093fb; --ink:#1f2340; --card:rgba(255,255,255,.95); }
  * { box-sizing:border-box; margin:0; padding:0; }
  html { scroll-behavior:smooth; }
  body { font-family:'Poppins',system-ui,sans-serif; color:var(--ink);
         background:linear-gradient(135deg,var(--c1),var(--c2) 55%,var(--c3)); background-attachment:fixed; }
  nav { position:sticky; top:0; z-index:10; display:flex; justify-content:center; flex-wrap:wrap; gap:6px;
        padding:12px; backdrop-filter:blur(10px); background:rgba(31,35,64,.35); }
  nav a { color:#fff; text-decoration:none; padding:6px 14px; border-radius:20px; font-size:.9rem; transition:.2s; }
  nav a:hover { background:rgba(255,255,255,.25); }
  header { text-align:center; color:#fff; padding:80px 20px 60px; }
  .avatar { width:120px; height:120px; border-radius:50%; margin:0 auto 20px; display:grid; place-items:center;
            font-size:2.6rem; font-weight:700; background:rgba(255,255,255,.2); border:3px solid #fff; }
  header h1 { font-size:clamp(2rem,6vw,3.4rem); }
  header p.title { font-size:1.2rem; opacity:.95; margin:8px 0 4px; }
  header p.loc { opacity:.8; font-size:.95rem; }
  .btns { margin-top:24px; display:flex; gap:10px; justify-content:center; flex-wrap:wrap; }
  .btn { padding:10px 22px; border-radius:30px; text-decoration:none; font-weight:600; font-size:.9rem;
         background:#fff; color:var(--c2); transition:transform .2s; }
  .btn.ghost { background:transparent; color:#fff; border:2px solid #fff; }
  .btn:hover { transform:translateY(-3px); }
  main { max-width:1000px; margin:0 auto; padding:0 20px 60px; }
  section { background:var(--card); border-radius:20px; padding:30px; margin-bottom:28px;
            box-shadow:0 10px 30px rgba(0,0,0,.15); }
  h2 { font-size:1.5rem; margin-bottom:18px; background:linear-gradient(90deg,var(--c1),var(--c2));
       -webkit-background-clip:text; background-clip:text; color:transparent; }
  .grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:18px; }
  .card { border-radius:14px; padding:20px; background:#fff; border:1px solid #e8e8f5; transition:.25s; }
  .card:hover { transform:translateY(-5px); box-shadow:0 8px 20px rgba(102,126,234,.3); }
  .card h3 { font-size:1.05rem; margin-bottom:4px; }
  .muted { color:#6b6f8d; font-size:.85rem; }
  .tag { display:inline-block; margin:4px 4px 0 0; padding:4px 12px; border-radius:20px; font-size:.78rem;
         color:#fff; background:linear-gradient(90deg,var(--c1),var(--c2)); }
  ul { padding-left:20px; margin-top:8px; } li { margin-bottom:6px; font-size:.92rem; }
  .job { padding-left:18px; border-left:4px solid var(--c1); margin-bottom:22px; }
  .stat { text-align:center; } .stat b { display:block; font-size:1.8rem; color:var(--c2); }
  footer { text-align:center; color:#fff; padding:24px; opacity:.85; font-size:.85rem; }
  @media (max-width:600px){ section{padding:20px;} }
</style>
</head>
<body>
<nav>
  <a href="#about">About</a><a href="#experience">Experience</a><a href="#projects">Projects</a>
  <a href="#skills">Skills</a><a href="#certs">Certifications</a><a href="#contact">Contact</a>
</nav>

<header>
  <div class="avatar">{{ p.name.split()[0][0] }}{{ p.name.split()[-1][0] }}</div>
  <h1>{{ p.name }}</h1>
  <p class="title">{{ p.title }}</p>
  <p class="loc">&#128205; {{ p.location }}</p>
  <div class="btns">
    <a class="btn" href="{{ p.github }}" target="_blank" rel="noopener">GitHub</a>
    <a class="btn" href="{{ p.linkedin }}" target="_blank" rel="noopener">LinkedIn</a>
    <a class="btn ghost" href="#contact">Hire Me</a>
  </div>
</header>

<main>
  <section id="about">
    <h2>About Me</h2>
    <p>{{ p.summary }}</p>
    <div class="grid" style="margin-top:20px">
      <div class="card stat"><b>{{ p.education.cgpa.split(' ')[0] }}</b><span class="muted">CGPA</span></div>
      <div class="card stat"><b>{{ p.experience|length }}</b><span class="muted">Internships</span></div>
      <div class="card stat"><b>{{ p.projects|length }}</b><span class="muted">Projects</span></div>
      <div class="card stat"><b>{{ p.certifications|length }}</b><span class="muted">Certifications</span></div>
    </div>
    <h3 style="margin-top:24px">&#127891; {{ p.education.degree }}</h3>
    <p class="muted">{{ p.education.school }} &middot; {{ p.education.period }}</p>
    <div>{% for c in p.education.coursework %}<span class="tag">{{ c }}</span>{% endfor %}</div>
  </section>

  <section id="experience">
    <h2>Experience</h2>
    {% for e in p.experience %}
    <div class="job">
      <h3>{{ e.role }} &middot; {{ e.org }}</h3>
      <p class="muted">{{ e.period }} &middot; {{ e.mode }}</p>
      <ul>{% for pt in e.points %}<li>{{ pt }}</li>{% endfor %}</ul>
    </div>
    {% endfor %}
  </section>

  <section id="projects">
    <h2>Projects</h2>
    <div class="grid">
      {% for pr in p.projects %}
      <div class="card">
        <h3>{{ pr.name }}</h3>
        <p class="muted">{{ pr.date }}</p>
        <p style="margin:10px 0;font-size:.92rem">{{ pr.desc }}</p>
        <div>{% for s in pr.stack %}<span class="tag">{{ s }}</span>{% endfor %}</div>
        <p style="margin-top:12px"><a href="{{ pr.link }}" target="_blank" rel="noopener">View on GitHub &rarr;</a></p>
      </div>
      {% endfor %}
    </div>
  </section>

  <section id="skills">
    <h2>Technical Skills</h2>
    <div class="grid">
      {% for cat, items in p.skills.items() %}
      <div class="card"><h3>{{ cat }}</h3>
        {% for i in items %}<span class="tag">{{ i }}</span>{% endfor %}
      </div>
      {% endfor %}
    </div>
  </section>

  <section id="certs">
    <h2>Certifications</h2>
    <ul>{% for c in p.certifications %}<li>{{ c }}</li>{% endfor %}</ul>
  </section>

  <section id="contact">
    <h2>Get In Touch</h2>
    <p>&#9993; <a href="mailto:{{ p.email }}">{{ p.email }}</a></p>
    <p>&#128222; {{ p.phone }}</p>
    <p>&#128205; {{ p.location }}</p>
  </section>
</main>

<footer>&copy; {{ year }} {{ p.name }}. Built with Flask.</footer>
</body>
</html>
"""


@app.route("/")
def home():
    from datetime import datetime
    return render_template_string(PAGE, p=PROFILE, year=datetime.now().year)


@app.route("/api/portfolio")
def api_portfolio():
    return jsonify(PROFILE)


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
