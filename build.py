# Rebuilds index.html from src/ (python3 build.py)
s = open("src/template.html").read()
s = s.replace("/*__CORE__*/", open("src/core.js").read()).replace("/*__UI__*/", open("src/ui.js").read())
open("index.html", "w").write(s)
