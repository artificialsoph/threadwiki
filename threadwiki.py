import path,mistune,flask
a,d=flask.Flask(""),path.Path("p")
@a.route("/<p>")
def s(p):
	f=d/p;k=flask.request.args.get('n',f.text());f.write_text(k);b=[f"[{l[2:]}](/{l[2:]})\n"for l in d.files()if"/"+p in l.text()]
	return mistune.markdown(f"#{p}\n{k}\n\n"+''.join(b))+f"<form><textarea name=n>{k}</textarea>\n<button>"