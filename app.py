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
        "exploratory analysis, machine learning and model evaluation. I build and deploy "
        "end-to-end ML web apps - from computer-vision systems to prediction dashboards."
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
                "Completed a 1-month internship specializing in Data Science, gaining practical exposure to data-driven problem solving.",
                "Hands-on exposure to AI/ML algorithms, data preprocessing and model evaluation techniques.",
                "Developed an understanding of data analysis workflows and industry-level practices for solving data-driven problems.",
            ],
        },
    ],
    "projects": [
        {
            "name": "Medical Insurance Cost Prediction",
            "type": "Regression | XGBoost",
            "date": "2026",
            "stack": ["Python", "Pandas", "Scikit-learn", "XGBoost", "Flask", "Render"],
            "desc": "Machine Learning web app that estimates medical insurance cost using an XGBoost model, built on the Medical Insurance Cost dataset and deployed with Flask on Render.",
            "github": "https://github.com/bunnyjadhao",
            "demo": "https://xgboast-algorithm.onrender.com/",
        },
        {
            "name": "Loan Approval Classification",
            "type": "Classification | Decision Tree",
            "date": "2026",
            "stack": ["Python", "Pandas", "Scikit-learn", "Decision Tree", "Flask", "Render"],
            "desc": "Classification web app that predicts loan approval using a Decision Tree model trained on a loan approval dataset, deployed with Flask on Render.",
            "github": "https://github.com/bunnyjadhao",
            "demo": "https://decision-tree-algorithm-pn2t.onrender.com/",
        },
        {
            "name": "Laptop Users Prediction",
            "type": "Classification | Support Vector Machine",
            "date": "2026",
            "stack": ["Python", "Pandas", "NumPy", "Scikit-learn", "Flask", "Machine Learning", "Render"],
            "desc": (
                "Web app that predicts a Yes/No outcome from age, gender, region, occupation and income. "
                "Uses an SVM to find the maximum-margin decision boundary, with data preprocessing, feature "
                "scaling and categorical encoding. Results are shown with confidence scores."
            ),
            "github": "https://lnkd.in/dZEy7gzh",
            "demo": "https://lnkd.in/d8DzzMjx",
        },
        {
            "name": "Heart Disease Prediction",
            "type": "Classification | K-Nearest Neighbors",
            "date": "2026",
            "stack": ["Python", "Pandas", "NumPy", "Scikit-learn", "Machine Learning", "Render"],
            "desc": (
                "Web app that predicts the likelihood of heart disease from patient details such as age, "
                "blood pressure, cholesterol, maximum heart rate, chest pain type and ST depression. "
                "Uses KNN to find similar records in the training data, with data preprocessing, feature "
                "scaling and handling of numerical and categorical features."
            ),
            "note": "Educational project only - not intended for medical diagnosis.",
            "github": "https://lnkd.in/dttRxCzG",
            "demo": "https://lnkd.in/dQjBR3bR",
        },
        {
            "name": "AI Impact on Students",
            "type": "Classification | Logistic Regression",
            "date": "Oct 2026",
            "stack": ["Python", "Pandas", "NumPy", "Scikit-learn", "Logistic Regression", "Flask"],
            "desc": (
                "Python-based Machine Learning application that analyzes student AI usage patterns and "
                "predicts impact levels as Low, Medium or High. Features an interactive Flask dashboard "
                "covering academic profiles and AI usage habits, with prediction results shown with confidence scores."
            ),
            "github": "https://github.com/bunnyjadhao/Logistic-Regression.ML",
            "demo": "https://logistic-regression-ml-ueu3.onrender.com",
        },
        {
            "name": "House Price Prediction",
            "type": "Regression | Linear Regression",
            "date": "Sep 2026",
            "stack": ["Python", "Flask", "Scikit-learn", "Pandas", "HTML", "CSS"],
            "desc": (
                "Linear Regression model that predicts house prices from seven property features. "
                "Deployed as an interactive Flask web app that collects property details and displays the estimated price."
            ),
            "github": "https://github.com/bunnyjadhao/LinearRegression",
            "demo": "https://linearregression-3698.onrender.com/",
        },
        {
            "name": "Drowsiness Detection System",
            "type": "Computer Vision | EAR + MAR",
            "date": "Feb 2025",
            "stack": ["Python", "Flask", "JavaScript", "MediaPipe", "Render"],
            "desc": (
                "Real-time driver drowsiness detection web app that analyzes webcam video to spot signs of fatigue. "
                "Uses EAR and MAR-based eye closure and yawning detection, with siren, screen flash and vibration alerts."
            ),
            "github": "https://github.com/bunnyjadhao/Driver-Drowsiness-Detection",
            "demo": "https://driver-drowsiness-detection-wwkt.onrender.com",
        },
    ],
    "skills": {
        "Data Science": ["Pandas", "NumPy", "Matplotlib", "Data Preprocessing", "Data Analysis",
                         "Data Visualization", "Machine Learning"],
        "Languages": ["Python", "SQL", "Java", "C", "C++", "JavaScript", "PHP", "HTML", "CSS"],
        "Web & APIs": ["React", "Node.js", "Express.js", "MongoDB", "Next.js", "REST APIs", "API Testing"],
        "Tools": ["VS Code", "Eclipse", "Android Studio", "Google Cloud Platform", "Postman"],
    },
    "workflow": [
        ("01", "Data Collection", "Datasets, Pandas"),
        ("02", "Preprocessing", "Cleaning, scaling"),
        ("03", "Encoding", "Categorical features"),
        ("04", "Model Training", "Scikit-learn, XGBoost"),
        ("05", "Evaluation", "Predictions, confidence"),
        ("06", "Deployment", "Flask + Render"),
    ],
    "certifications": [
        "Skill India - AI For India 2.0",
        "Great Learning - Front End Development (HTML)",
        "Udemy - Java and C++ Complete Course for Beginners",
        "Scaler Topics - MySQL and Database Design Course",
    ],
}

PAGE = """
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{ p.name }} | Data Science Portfolio</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
<script>try{document.documentElement.dataset.theme=localStorage.getItem('theme')||'dark'}catch(e){}</script>
<style>
  :root[data-theme="dark"] { --bg:#0d1117; --bg2:#0d1117; --panel:#161b22; --line:#30363d; --ink:#e6edf3; --mut:#8b949e;
    --a1:#58a6ff; --a2:#3fb950; --a3:#d2a8ff; --a4:#ffa657; --nav:rgba(13,17,23,.85); --hero:var(--ink); --shadow:none; }
  :root[data-theme="gradient"] { --bg:linear-gradient(135deg,#667eea,#764ba2 55%,#f093fb); --panel:rgba(255,255,255,.95);
    --line:#e8e8f5; --ink:#1f2340; --mut:#6b6f8d; --a1:#667eea; --a2:#764ba2; --a3:#764ba2; --a4:#c0392b;
    --nav:rgba(31,35,64,.4); --hero:#fff; --shadow:0 10px 30px rgba(0,0,0,.15); }
  * { box-sizing:border-box; margin:0; padding:0; }
  html { scroll-behavior:smooth; }
  body { font-family:'Poppins',system-ui,sans-serif; color:var(--ink); background:var(--bg); background-attachment:fixed; min-height:100vh; }
  .mono { font-family:'JetBrains Mono',ui-monospace,monospace; }
  nav { position:sticky; top:0; z-index:10; display:flex; justify-content:center; flex-wrap:wrap; gap:4px; padding:10px;
        backdrop-filter:blur(10px); background:var(--nav); border-bottom:1px solid var(--line); }
  nav a { color:var(--hero); text-decoration:none; padding:6px 12px; border-radius:6px; font-size:.82rem; font-family:'JetBrains Mono',monospace; }
  nav a:hover { background:rgba(128,128,128,.25); }
  #themeBtn { position:fixed; right:16px; bottom:16px; z-index:20; border:0; cursor:pointer; padding:10px 16px; border-radius:30px;
        font:600 .85rem 'Poppins'; color:#fff; background:linear-gradient(90deg,#667eea,#764ba2); box-shadow:0 4px 14px rgba(0,0,0,.4); }
  header { max-width:1000px; margin:0 auto; padding:50px 20px 30px; display:grid; grid-template-columns:auto 1fr; gap:28px; align-items:center; color:var(--hero); }
  .avatar { width:170px; height:170px; border-radius:50%; object-fit:cover; border:4px solid var(--a1); box-shadow:0 0 25px rgba(88,166,255,.45); }
  header h1 { font-size:clamp(1.9rem,5vw,3rem); line-height:1.15; }
  .role { font-size:1.15rem; margin:8px 0; color:var(--a2); min-height:1.6em; }
  :root[data-theme="gradient"] .role { color:#fff; opacity:.95; }
  .cursor { display:inline-block; width:9px; height:1.1em; background:currentColor; vertical-align:-3px; animation:blink 1s steps(1) infinite; }
  @keyframes blink { 50% { opacity:0; } }
  .btns { margin-top:16px; display:flex; gap:10px; flex-wrap:wrap; }
  .btn { padding:9px 20px; border-radius:8px; text-decoration:none; font-weight:600; font-size:.85rem; background:var(--a1); color:#fff; border:2px solid var(--a1); }
  .btn.ghost { background:transparent; color:var(--hero); border-color:var(--hero); }
  :root[data-theme="gradient"] .btn { background:#fff; color:#764ba2; border-color:#fff; }
  main { max-width:1000px; margin:0 auto; padding:0 20px 80px; }
  .cell { background:var(--panel); border:1px solid var(--line); border-radius:12px; margin-bottom:22px; box-shadow:var(--shadow); overflow:hidden; }
  .cell-head { display:flex; align-items:center; gap:12px; padding:10px 18px; border-bottom:1px solid var(--line); font-size:.8rem; color:var(--mut); }
  .cell-head .in { color:var(--a1); font-weight:600; }
  .cell-head .kw { color:var(--a3); }
  .cell-body { padding:22px; }
  h2 { font-size:1.3rem; margin-bottom:14px; }
  .grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:16px; }
  .card { border:1px solid var(--line); border-radius:10px; padding:18px; transition:.25s; }
  .card:hover { transform:translateY(-4px); border-color:var(--a1); }
  .card h3 { font-size:1.02rem; margin-bottom:4px; }
  .muted { color:var(--mut); font-size:.85rem; }
  .tag { display:inline-block; margin:4px 4px 0 0; padding:3px 11px; border-radius:20px; font-size:.75rem; font-family:'JetBrains Mono',monospace;
         color:var(--a1); border:1px solid var(--a1); }
  .badge { display:inline-block; padding:3px 10px; border-radius:6px; font-size:.72rem; color:#fff; background:linear-gradient(90deg,var(--a1),var(--a2)); margin-bottom:8px; }
  .stat { text-align:center; } .stat b { display:block; font-size:1.9rem; color:var(--a2); font-family:'JetBrains Mono',monospace; }
  ul { padding-left:20px; margin-top:8px; } li { margin-bottom:6px; font-size:.92rem; }
  a { color:var(--a1); }
  .bar { display:flex; align-items:center; gap:10px; margin:10px 0; font-size:.82rem; }
  .bar span:first-child { width:110px; flex:none; } .bar i { display:block; height:12px; border-radius:6px; background:linear-gradient(90deg,var(--a1),var(--a3)); }
  .out { margin-top:14px; padding:12px 16px; border-radius:8px; background:rgba(128,128,128,.12); font-size:.82rem; border-left:3px solid var(--a2); }
  #net { position:fixed; inset:0; z-index:0; pointer-events:none; opacity:.55; }
  nav, header, main, footer { position:relative; z-index:1; } nav { position:sticky; }
  table.df { width:100%; border-collapse:collapse; font-family:'JetBrains Mono',monospace; font-size:.78rem; margin-bottom:20px; }
  .tblwrap { overflow-x:auto; }
  table.df th { text-align:left; padding:8px 12px; border-bottom:2px solid var(--a1); color:var(--a3); white-space:nowrap; }
  table.df td { padding:8px 12px; border-bottom:1px solid var(--line); white-space:nowrap; }
  table.df td:first-child { color:var(--mut); } table.df tr:hover td { background:rgba(128,128,128,.12); }
  .flow { display:grid; grid-template-columns:repeat(auto-fit,minmax(135px,1fr)); gap:10px; }
  .step { position:relative; border:1px solid var(--line); border-radius:10px; padding:14px 12px; }
  .step b { font-family:'JetBrains Mono',monospace; color:var(--a2); font-size:1.1rem; display:block; }
  .step h4 { font-size:.9rem; margin:2px 0; }
  .step:not(:last-child)::after { content:'\2192'; position:absolute; right:-9px; top:40%; color:var(--a1); z-index:2; font-size:1rem; }
  footer { text-align:center; color:var(--hero); padding:24px; opacity:.8; font-size:.8rem; }
  @media (max-width:680px){ header { grid-template-columns:1fr; text-align:center; justify-items:center; } .btns{justify-content:center;} }
</style>
</head>
<body>
<canvas id="net"></canvas>
<nav>
  <a href="#about">about</a><a href="#experience">experience</a><a href="#projects">projects</a><a href="#workflow">workflow</a>
  <a href="#skills">skills</a><a href="#certs">certs</a><a href="#contact">contact</a>
</nav>
<button id="themeBtn" onclick="toggleTheme()">Switch theme</button>

<header>
  <img class="avatar" src="{{ url_for('static', filename='profile.jpg') }}" alt="{{ p.name }}">
  <div>
    <p class="mono muted" style="color:var(--a3)">import pandas as pd &nbsp;# hello, world</p>
    <h1>{{ p.name }}</h1>
    <p class="role mono"><span id="typed"></span><span class="cursor"></span></p>
    <p class="muted" style="color:var(--hero);opacity:.8">&#128205; {{ p.location }} &middot; {{ p.education.degree }}</p>
    <div class="btns">
      <a class="btn" href="#projects">View Projects</a>
      <a class="btn ghost" href="{{ p.github }}" target="_blank" rel="noopener">GitHub</a>
      <a class="btn ghost" href="{{ p.linkedin }}" target="_blank" rel="noopener">LinkedIn</a>
    </div>
  </div>
</header>

<main>
  <div class="cell" id="about">
    <div class="cell-head mono"><span class="in">In [1]:</span><span><span class="kw">print</span>(about_me)</span></div>
    <div class="cell-body">
      <h2>About Me</h2>
      <p>{{ p.summary }}</p>
      <div class="grid" style="margin-top:18px">
        <div class="card stat"><b>{{ p.education.cgpa.split(' ')[0] }}</b><span class="muted">CGPA</span></div>
        <div class="card stat"><b>{{ p.projects|length }}</b><span class="muted">ML projects</span></div>
        <div class="card stat"><b>{{ n_algos }}</b><span class="muted">ML algorithms</span></div>
        <div class="card stat"><b>{{ p.certifications|length }}</b><span class="muted">certifications</span></div>
      </div>
      <h3 style="margin-top:22px">&#127891; {{ p.education.degree }}</h3>
      <p class="muted">{{ p.education.school }} &middot; {{ p.education.period }}</p>
      <div>{% for c in p.education.coursework %}<span class="tag">{{ c }}</span>{% endfor %}</div>
    </div>
  </div>

  <div class="cell" id="experience">
    <div class="cell-head mono"><span class="in">In [2]:</span><span>experience.<span class="kw">head</span>()</span></div>
    <div class="cell-body">
      <h2>Experience</h2>
      {% for e in p.experience %}
      <h3>{{ e.role }} &middot; {{ e.org }}</h3>
      <p class="muted">{{ e.period }} &middot; {{ e.mode }}</p>
      <ul>{% for pt in e.points %}<li>{{ pt }}</li>{% endfor %}</ul>
      {% endfor %}
    </div>
  </div>

  <div class="cell" id="projects">
    <div class="cell-head mono"><span class="in">In [3]:</span><span>model.<span class="kw">fit</span>(projects)</span></div>
    <div class="cell-body">
      <h2>Projects</h2>
      <div class="tblwrap"><table class="df">
        <tr><th></th><th>project</th><th>task</th><th>algorithm</th><th>deployed</th></tr>
        {% for pr in p.projects %}<tr><td>{{ loop.index0 }}</td><td>{{ pr.name }}</td><td>{{ pr.type.split(' | ')[0] }}</td><td>{{ pr.type.split(' | ')[1] }}</td><td>{{ 'Render' if 'Render' in pr.stack else 'Web' }}</td></tr>{% endfor %}
      </table></div>
      <div class="grid">
        {% for pr in p.projects %}
        <div class="card">
          <span class="badge mono">{{ pr.type }}</span>
          <h3>{{ pr.name }}</h3>
          <p class="muted">{{ pr.date }}</p>
          <p style="margin:10px 0;font-size:.9rem">{{ pr.desc }}</p>
          <div>{% for t in pr.stack %}<span class="tag">{{ t }}</span>{% endfor %}</div>
          {% if pr.note %}<p class="muted" style="margin-top:10px">&#9888;&#65039; {{ pr.note }}</p>{% endif %}
          <p style="margin-top:14px;display:flex;gap:14px;flex-wrap:wrap">
            {% if pr.demo %}<a href="{{ pr.demo }}" target="_blank" rel="noopener"><b>&#9654; Live Demo</b></a>{% endif %}
            <a href="{{ pr.github }}" target="_blank" rel="noopener">GitHub &rarr;</a>
          </p>
        </div>
        {% endfor %}
      </div>
    </div>
  </div>

  <div class="cell" id="workflow">
    <div class="cell-head mono"><span class="in">In [4]:</span><span>pipeline.<span class="kw">run</span>()</span></div>
    <div class="cell-body">
      <h2>My ML Workflow</h2>
      <div class="flow">
        {% for n,t,d in p.workflow %}<div class="step"><b>{{ n }}</b><h4>{{ t }}</h4><span class="muted">{{ d }}</span></div>{% endfor %}
      </div>
    </div>
  </div>

  <div class="cell" id="skills">
    <div class="cell-head mono"><span class="in">In [5]:</span><span>skills.<span class="kw">value_counts</span>()</span></div>
    <div class="cell-body">
      <h2>Technical Skills</h2>
      {% set mx = p.skills.values()|map('length')|max %}
      {% for cat, items in p.skills.items() %}
      <div class="bar"><span class="mono">{{ cat }}</span><i style="width:{{ (items|length / mx * 60)|round|int }}%"></i><span class="muted">{{ items|length }}</span></div>
      {% endfor %}
      <div class="grid" style="margin-top:16px">
        {% for cat, items in p.skills.items() %}
        <div class="card"><h3>{{ cat }}</h3>{% for i in items %}<span class="tag">{{ i }}</span>{% endfor %}</div>
        {% endfor %}
      </div>
      <div class="out mono">Out[5]: {{ p.skills.values()|map('length')|sum }} skills across {{ p.skills|length }} categories</div>
    </div>
  </div>

  <div class="cell" id="certs">
    <div class="cell-head mono"><span class="in">In [6]:</span><span>certifications</span></div>
    <div class="cell-body"><h2>Certifications</h2>
      <ul>{% for c in p.certifications %}<li>{{ c }}</li>{% endfor %}</ul></div>
  </div>

  <div class="cell" id="contact">
    <div class="cell-head mono"><span class="in">In [7]:</span><span>contact.<span class="kw">send</span>()</span></div>
    <div class="cell-body"><h2>Get In Touch</h2>
      <p>&#9993; <a href="mailto:{{ p.email }}">{{ p.email }}</a></p>
      <p>&#128222; {{ p.phone }}</p>
      <p>&#128205; {{ p.location }}</p></div>
  </div>
</main>

<footer class="mono">&copy; {{ year }} {{ p.name }} &middot; built with Flask</footer>

<script>
  function toggleTheme(){
    var r=document.documentElement, t=r.dataset.theme==='dark'?'gradient':'dark';
    r.dataset.theme=t; try{localStorage.setItem('theme',t)}catch(e){}
  }
  var roles=['Data Science Student','Machine Learning Enthusiast','Flask Developer','Python Programmer'], ri=0, ci=0, del=false, el=document.getElementById('typed');
  (function tick(){
    var w=roles[ri];
    el.textContent=w.slice(0,ci);
    if(!del && ci<w.length){ci++; return setTimeout(tick,80);}
    if(!del){del=true; return setTimeout(tick,1400);}
    if(ci>0){ci--; return setTimeout(tick,40);}
    del=false; ri=(ri+1)%roles.length; setTimeout(tick,300);
  })();

  (function(){
    var c=document.getElementById('net'), x=c.getContext('2d'), N=[], W, H;
    function size(){ W=c.width=innerWidth; H=c.height=innerHeight; }
    size(); addEventListener('resize', size);
    for(var i=0;i<55;i++) N.push({x:Math.random()*innerWidth,y:Math.random()*innerHeight,vx:(Math.random()-.5)*.4,vy:(Math.random()-.5)*.4});
    (function draw(){
      var col=getComputedStyle(document.documentElement).getPropertyValue('--a1').trim()||'#58a6ff';
      x.clearRect(0,0,W,H); x.fillStyle=col; x.strokeStyle=col;
      N.forEach(function(a,i){
        a.x+=a.vx; a.y+=a.vy; if(a.x<0||a.x>W)a.vx*=-1; if(a.y<0||a.y>H)a.vy*=-1;
        x.beginPath(); x.arc(a.x,a.y,2,0,6.3); x.fill();
        for(var j=i+1;j<N.length;j++){ var b=N[j], d=Math.hypot(a.x-b.x,a.y-b.y);
          if(d<130){ x.globalAlpha=1-d/130; x.beginPath(); x.moveTo(a.x,a.y); x.lineTo(b.x,b.y); x.stroke(); x.globalAlpha=1; } }
      });
      requestAnimationFrame(draw);
    })();
  })();
</script>
</body>
</html>
"""


@app.route("/")
def home():
    from datetime import datetime
    n_algos = sum(1 for x in PROFILE["projects"] if not x["type"].startswith("Computer"))
    return render_template_string(PAGE, p=PROFILE, year=datetime.now().year, n_algos=n_algos)


@app.route("/api/portfolio")
def api_portfolio():
    return jsonify(PROFILE)


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
