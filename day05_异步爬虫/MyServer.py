from flask import Flask, render_template
from time import sleep

# 实例化一个flask的实例对象
app = Flask(__name__)


# 配置路由
@app.route('/jay')
# 视图函数
def index_1():
    sleep(2)
    return render_template('test.html')


@app.route('/jj')
# 视图函数
def index_2():
    sleep(2)
    return render_template('test.html')


@app.route('/hh')
# 视图函数
def index_3():
    sleep(2)
    return render_template('test.html')


if __name__ == '__main__':
    # 开启调试模式（代码保存成功后自动重启服务）
    app.run(debug=True)
