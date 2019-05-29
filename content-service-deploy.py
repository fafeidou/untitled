# -*- coding=utf-8 -*
import datetime
import os

import paramiko

hostname = '192.168.138.52'
username = 'ckitadmin'
password = 'p@ssw0rd'
port = 22

# 文件路径  只需设置到文件夹即可
def upload(local_dir, remote_dir):
    try:
        t = paramiko.Transport((hostname, port))
        t.connect(username, password)
        sftp = paramiko.SFTPClient.from_transport(t)
        print('upload file start %s ' % datetime.datetime.now())
        for root, dirs, files in os.walk(local_dir):
            print('[%s][%s][%s]' % (root, dirs, files))
            for filespath in files:
                local_file = os.path.join(root, filespath)
                print(11, '[%s][%s][%s][%s]' % (root, filespath, local_file, local_dir))
                a = local_file.replace(local_dir, '').replace('\\', '/').lstrip('/')
                print('01', a, '[%s]' % remote_dir)
                remote_file = os.path.join(remote_dir, a)
                print(22, remote_file)
                try:
                    sftp.put(local_file, remote_file)
                except Exception as e:
                    sftp.mkdir(os.path.split(remote_file)[0])
                    sftp.put(local_file, remote_file)
                    print("66 upload %s to remote %s" % (local_file, remote_file))
            for name in dirs:
                local_path = os.path.join(root, name)
                print(0, local_path, local_dir)
                a = local_path.replace(local_dir, '').replace('\\', '')
                print(1, a)
                print(1, remote_dir)
                remote_path = os.path.join(remote_dir, a)
                print(33, remote_path)
                try:
                    sftp.mkdir(remote_path)
                    print(44, "mkdir path %s" % remote_path)
                except Exception as e:
                    print(55, e)
        print('77,upload file success %s ' % datetime.datetime.now())
        t.close()
    except Exception as e:
        print(88, e)


# 执行linux命令
def sshclient_execmd(hostname, port, username, password, execmd):
    paramiko.util.log_to_file("paramiko.log")
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command(execmd)
    stdin.write("Y")  # Generally speaking, the first connection, need a simple interaction.
    stdout.read()
    s.close()


def restartService():
    execmd = "cd /home/ckitadmin/ck-project/ && ./content-restart.sh "
    sshclient_execmd(hostname, port, username, password, execmd)


if __name__ == '__main__':
    # 打包
    os.system(
        "cd C:\idea_work\git\content-center && mvn clean package && cd ./target &&  mkdir jar && move .\content-0.0.1-SNAPSHOT.jar .\jar")
    local_dir = r'C:\idea_work\git\content-center\target\jar'
    remote_dir = '/home/ckitadmin/ck-project/'
    # 上传
    upload(local_dir, remote_dir)
    # 重启
    restartService()
