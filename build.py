# Rebuilds index.html from the source files (python3 build.py)
s = open("template.html").read()
s = s.replace("/*__CORE__*/", open("core.js").read()).replace("/*__UI__*/", open("ui.js").read())
open("index.html", "w").write(s)

