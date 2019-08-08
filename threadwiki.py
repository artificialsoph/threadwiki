import path;import mistune as m;import flask
a,d=flask.Flask(""),path.Path("p")
@a.route("/<p>")
def s(p):
	r,f=flask.request.args,d/p;k=f.text()if f.exists()else""
	if'n'in r: f.write_text(r['n'])
	b=[f"<a href='/{l[2:]}'>{l[2:]}</a><br>"for l in d.files()if"/"+p in l.text()]
	return f"<h1>{p}</h1>"+m.markdown(k)+"<form><textarea name=n></textarea><input type=submit>"+''.join(b)