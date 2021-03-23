from flask import Flask, escape, url_for, render_template
#  escape() 函数对 name 变量进行转义处理，比如把 < 转换成 &lt;
# url_for 函数来生成 URL，它接受的第一个参数就是视图函数名
app = Flask(__name__)

name = '明君'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)

@app.route('/user/<name>')
def user_page(name):
    return 'Welcome to My Watchlist, %s 大人！' % escape(name)

if __name__=="__main__":
    app.run()