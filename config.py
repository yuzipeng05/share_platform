# 设置共享路径
share_path = 'F:\\Python成长之路'
# 设置本地IP地址，127.0.0.1只有自己访问
ip = '127.0.0.1'
# 共享最大时长，默认15min
MaxTime = 900
# 共享平台的端口，若无冲突，可不用修改
share_port = 8000
# 访问共享数据时的web地址，默认为http://127.0.0.1:8000
share_website = 'http://{0}:{1}'.format(ip,share_port)