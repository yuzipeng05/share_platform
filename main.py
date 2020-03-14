# coding=utf-8
# @公众号 : "鹏哥贼优秀"
# @Date : 2020/3/14
# @Software : PyCharm 
# @Python version: Python 3.7.2

from flask import Flask, render_template, request
from datebase import *
import os
import subprocess
import time
from config import *

app = Flask(__name__)


@app.route('/')
def share_platform():
    now_status = query()
    return render_template('share.html', status=now_status,share_path=share_path,share_website=share_website)


@app.route('/update_status', methods=['get'])
def update_status():
    new_status = request.args.get('status')
    old_status = query()
    share = Share()
    if new_status == '1' and old_status != new_status:
        share.begin_share()
        return '已开启共享！'
    elif new_status == '1' and old_status == new_status:
        return '已开启共享！'
    elif new_status == '0' and old_status != new_status:
        print('即将关闭共享……')
        share.end_share()
        return '已停止共享！'
    else:
        return '已停止共享！'


class Share():
    def begin_share(self):
        update('1')
        os.chdir(share_path)
        start_time = time.time()
        global share_process
        share_process = subprocess.Popen('python -m http.server {0}'.format(share_port))
        print('共享链接已打开！当前时间为：', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        while (time.time() - start_time) < MaxTime:
            pass
        self.end_share()

    def end_share(self):
        try:
            share_process.kill()
        except:
            print('共享链接已关闭，无法执行kill命令！')
        print('共享链接已关闭！当前时间为：', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        update('0')


if __name__ == '__main__':
    app.run(debug=True, host=ip, port=5000)
