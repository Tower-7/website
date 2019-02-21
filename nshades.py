# -*- coding:utf8 -*-
import os
# 安装node
downloadNode = 'wget https://nodejs.org/dist/v10.15.1/node-v10.15.1-linux-x64.tar.xz'
def download(downloadNode):
    if os.path.exists('/usr/local/node'):
        os.system('rm -rf /usr/local/node')
    os.system('mkdir -p /usr/local/node')
    os.system('cd /usr/local/node &&' + downloadNode + '&& mv *.tar.xz node.tar.xz && tar -xvf node.tar.xz')
    os.system('cd /usr/local/node && rm -rf node.tar.xz && mv * node')
    os.system('ln -s /usr/local/node/node/bin/node /usr/local/bin/node')
    os.system('ln -s /usr/local/node/node/bin/npm /usr/local/bin/npm')
    os.system('npm -g install pm2')
    os.system('ln -s /usr/local/node/node/bin/pm2 /usr/local/bin/pm2')
download(downloadNode)
def setNginx():
    os.system('yum -y install nginx &&nginx')
setNginx()
def downloadProgram():
    os.system('yum -y install git')
    if os.path.exists('/home/wwwroot'):
        os.system('rm -rf /home/wwwroot')
    os.system('mkdir -p /home/wwwroot')
    os.system('cd /home/wwwroot && git clone https://github.com/Tower-7/nshades.git')
downloadProgram()
def running():
    os.system('cd /home/wwwroot/nshades/ && npm install && pm2 start server.js')
running()
def configNginx():
    if os.system('/etc/nginx/nginx'):
        os.system('rm -rf /etc/nginx/nginx')
    os.system('cd /etc/nginx/ && git clone https://github.com/Tower-7/nginx.git')
    os.system('mv -f /etc/nginx/nginx/* /etc/nginx/')
    os.system('nginx -s reload')
configNginx()
