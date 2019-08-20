from flask import Flask,render_template,request,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect
import datetime
import os
#from flask.ext.login import LoginManager
#from f.lask.ext.login import login_required
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/stock.sqlite3' 
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)


class stocks(db.Model):
	id = db.Column('stock_id', db.Integer, primary_key = True) 
	tanggal =  db.Column(db.Date)
	jenis =  db.Column(db.String(10))
	res_partner_id = db.Column(db.String(10))
	name = db.Column(db.String(100))
	jumlah = db.Column(db.String(50))
	addr = db.Column(db.String(200))
	user_id = db.Column(db.String(10))
	create_date = db.Column(db.String(10))
	update_date = db.Column(db.String(10))

class products(db.Model):
	id = db.Column('product_id', db.Integer, primary_key = True) 
	tanggal =  db.Column(db.Date)
	jenis =  db.Column(db.String(10))
	name = db.Column(db.String(100))
	jumlah = db.Column(db.String(50))
	addr = db.Column(db.String(200))
	pin = db.Column(db.String(10))
	

def __init__(self, name, city, addr,pin): 
	self.name = name
	self.city = city
	self.addr = addr
	self.pin = pin	

def generatetemplate(namaobj,namafile):
	filename='templates/'+namafile+'.html'
	if not os.path.isfile('filename'):
		f= open(filename,"w+")
		f.write('{% extends "base.html" %}')
		f.write('{% block content %}')
		f.write('{% if action=="add" %}')
		f.write('<form>')
		for c in namaobj.__table__.columns:
			#error
			if str(c.type) == 'DATE':
				f.write('<label>'+str(c)+'</label><div class="input-group date" id="datetimepicker1"><input type="text" class="form-control" />')
				f.write('<i class="icon-calendar"></i>')
				f.write('</div>')
			else:
				f.write('<label>'+str(c)+'</label><input type"text" id="'+str(c)+'" placeholder="'+str(c.type)+'">')
		
			
	f.write('<input type="submit"><br>')
	f.write('</form>')
	f.write('{% endif %}')
	f.write('{% if action=="list" %}')
	f.write('<a class="btn btn-info" href="/masterdata?action=add"><i class="icon-plus"/></a>')
	f.write('<table class="table table-striped table-bordered"><tbody>')
	f.write('<thead>')
	for c in namaobj.__table__.columns:
		f.write('<th>'+str(c)+'</th>')
	f.write('<th>action</th>')	
	f.write('</thead>')
	f.write('{% for stocks in content %}')	
	f.write('<tr>\n')
	for c in namaobj.__table__.columns:
		f.write('<td>{{'+str(c)+'}}</td>')
		f.write('<td><a href=""><i class="icon-trash"></a><td>')	
	f.write('</tr>')
	f.write('{% endfor %}')	
	f.write('</tbody></table>')	
	f.write('{% endif %}')
	f.write('{% endblock %}')
	f.close()
	return namafile
	




menus=[{'title':'Persediaan(0)','href':'/persediaan?action=list'}
      ,{'title':'Pembelian(1)','href':'/pembelian'}
      ,{'title':'Penjualan(2)','href':'/penjualan?action=list'}
      ,{'title':'Stock','href':'/stock?action="list"'}
      ,{'title':'Master data','href':'/masterdata?action=list'}]

@app.route("/")
def index():
 contents="""
 Aplikasi Simple Warehouse
 """
 db.create_all()
 stock=stocks()
 stock.name="felino"
 stock.tanggal=datetime.datetime.now()
 #
 db.session.add(stock)
 db.session.commit()
 sto=stocks.query.all()
 contents=sto
 return render_template("welcome.html",menus=menus,content=contents)

@app.route("/persediaan")
def persediaan():
 action=request.args.get("action")
 if action=="del":
 	pass

 frm="persediaan.html"
 flash('persediaan')	
 generatetemplate(stocks,'persediaan')
 sto=stocks.query.all()
 contents=sto
 return render_template(frm,menus=menus,content=contents,action=action) 



@app.route("/pembelian")
def pembelian():
	if request.args.get("action") == "add":
		stock=stocks()
		stock.name="add"
		stock.tanggal=datetime.datetime.now()
		db.session.add(stock)
		#return 1
	flash("delete record")
	sto=stocks.query.all()
	contents=sto
	return render_template("pembelian.html",menus=menus,content=contents)

@app.route("/stock")
def pembelianstock():
 action=request.args.get("action")
 generatetemplate(stocks,'stocks')
 sto=stocks.query.all()
 contents=sto
 return render_template("stocks.html",menus=menus,content=contents,action=action)


@app.route("/penjualan")
def penjualan():
 action=request.args.get("action")
 contents=stocks.query.all()
 return render_template("penjualan.html",menus=menus,content=contents,action=action) 

@app.route("/masterdata")
def masterdata():
	table = inspect(stocks)
	action=request.args.get("action") 
	contents=""
	for c in stocks.__table__.columns:
		contents=contents+c
	nama=""   
	if not os.path.isfile('./templates/masterdata.html'):
		f= open("./templates/masterdata.html","w+")
		f.write('{% extends "base.html" %}')
		f.write('{% block content %}')
		f.write('{% if action=="add" %}')
		f.write('<form>')
	for c in stocks.__table__.columns:
		if str(c.type)=='DATE':
			f.write('<label>'+str(c)+'</label><div class="input-group date" id="datetimepicker1"><input type="text" class="form-control" />')
			f.write('<i class="icon-calendar"></i>')
			f.write('</div>')
		else:
			f.write('<label>'+str(c)+'</label><input type"text" id="'+str(c)+'" placeholder="'+str(c.type)+'">')
		
			
	f.write('<input type="submit"><br>')
	f.write('</form>')
	f.write('{% endif %}')
	f.write('{% if action=="list" %}')
	f.write('<a class="btn btn-info" href="/masterdata?action=add"><i class="icon-plus"/></a>')
	f.write('<table class="table table-striped table-bordered"><tbody>')
	f.write('<thead>')
	for c in stocks.__table__.columns:
		f.write('<th>'+str(c)+'</th>')
	f.write('<th>action</th>')	
	f.write('</thead>')
	f.write('{% for stocks in content %}')	
	f.write('<tr>\n')
	for c in stocks.__table__.columns:
		f.write('<td>{{'+str(c)+'}}</td>')
	f.write('<td><a href=""><i class="icon-trash"></a><td>')	
	f.write('</tr>')
	f.write('{% endfor %}')	
	f.write('</tbody></table>')	
	f.write('{% endif %}')
	f.write('{% endblock %}')
	f.close()
	sto=stocks.query.all()
	contents=sto
	return render_template("masterdata.html",menus=menus,content=contents,action=action)  



if __name__ == '__main__':
 app.run(host='0.0.0.0',port=5000, debug=True)
