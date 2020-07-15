# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:17:01 2020

@author: wywei
"""

"""
Created on Fri Mar 16 09:08:34 2018

@author: wywei
"""
import socket
import socketserver
from socketserver import StreamRequestHandler as SRH  
#from time import ctime  
import datetime
from threading import Thread
import time
import pickle
import os
import pprint
  
  
#host =   "192.168.173.1"  #"192.168.173.1"
servername = "GD-SC-091"
host = "127.0.0.1"  #socket.gethostbyname(servername)                      
port = 9999  
addr = (host,port)  
count_dic=dict()

ADDRESS = (host, port)  # 绑定地址
g_socket_server = None  # 负责监听的socket
g_conn_pool = []  # 连接池

def init():
    """
    初始化服务端
    """
    global g_socket_server
    g_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建 socket 对象
    g_socket_server.bind(ADDRESS)
    g_socket_server.listen(5)  # 最大等待数（有很多人理解为最大连接数，其实是错误的）
    print("服务端已启动，等待客户端连接...")


def accept_client():
    """
    接收新连接
    """
    while True:
        client, _ = g_socket_server.accept()  # 阻塞，等待客户端连接
        # 加入连接池
        g_conn_pool.append(client)
        # 给每个客户端创建一个独立的线程进行管理
        thread = Thread(target=message_handle, args=(client,))
        # 设置成守护线程
        thread.setDaemon(True)
        thread.start()
 
 
def message_handle(client):
    """
    消息处理
    """
    #client.sendall("连接服务器成功!".encode(encoding='utf8'))
    while True:
        bytes = client.recv(1024)
        msg = bytes
        print("客户端消息:", bytes.decode(encoding='utf8'))
        if msg:   
            msg = str(msg, encoding='utf-8')
            msg=msg.strip()
            msglist = msg.split('$')
            #print(msg)
            global count_dic
            if msglist[0] == "totalcook":  # only use DLL
                print("OK\n")
                modulename=msglist[1]
                modulename=modulename.strip()
                if modulename in count_dic:
                    count_dic[modulename][0]+=1    # add count
                    count_dic[modulename][1]+=1    # means will use cali DLL
                else:
                    count_dic[modulename]=[1, 1]   # add item, and will use cali DLL
                pprint.pprint(count_dic)
                client.sendall("e".encode(encoding='utf8'))
            else:
                if msglist[0] == "totalcong":  # only use DLL
                    print("NG\n")
                    modulename=msglist[1]
                    modulename=modulename.strip()
                    if modulename in count_dic:
                        count_dic[modulename][0]+=1    # add count
                    else:
                        count_dic[modulename]=[1, 0]   # add item, but will not use cali DLL
                    pprint.pprint(count_dic)
                    client.sendall("e".encode(encoding='utf8'))
                else:
                    print("RAW\n")
                    fuseid = msglist[0]
                    msglist_length = len(msglist)
                    if msglist_length == 2:
                        module_flag = msglist[1]
                        txtname = "winnie\\server\\TXT\\"+fuseid+"-"+module_flag+".txt"
                        f=open(txtname,'w')
                        f.write(fuseid+','+module_flag)
                        f.close()
                        client.sendall("e".encode(encoding='utf8'))

                    else:
                        module_flag = msglist[-1]
                        txtname = "winnie\\server\\TXT\\"+fuseid+"-"+module_flag+".txt"
                        f=open(txtname,'w')
                        for mm in msglist:
                            print(mm)
                            f.write(mm+',')
                        f.close()
        time.sleep(10)
        if True: #len(bytes) == 0:
            client.close()
            # 删除连接
            g_conn_pool.remove(client)
            print("有一个客户端下线了。")
            break

def runsavecount():
    while True:
        pkl_file = open('winnie\\server\\dic.pkl', 'wb')
        pickle.dump(count_dic, pkl_file)
        pkl_file.close()
        print("Has save: ")
        pprint.pprint(count_dic)
        time.sleep(10)

if __name__ == '__main__':
    if os.path.exists("winnie\\server\\TXT\\")==False: 
        os.makedirs("winnie\\server\\TXT\\")
    if os.path.exists("winnie\\server\\dic.pkl")==False: 
        dic={'Winnie':1}
        output = open("winnie\\server\\dic.pkl", 'wb')
        pickle.dump(dic, output)
        output.close()
    
    pkl_file = open('winnie\\server\\dic.pkl', 'rb')
    count_dic = pickle.load(pkl_file)
    print("Begin: ")
    pprint.pprint(count_dic)
    pkl_file.close()
    ta = Thread(target=runsavecount)      
    ta.start()
    
    init()
    # 新开一个线程，用于接收新连接
    for i in range(8):
        thread = Thread(target=accept_client)
        thread.setDaemon(True)
        thread.start()
    # 主线程逻辑
    while True:
        cmd = input("""--------------------------
                输入1:查看当前在线人数
                输入2:给指定客户端发送消息
                输入3:关闭服务端
                """)
        if cmd == '1':
            print("--------------------------")
            print("当前在线人数：", len(g_conn_pool))
        elif cmd == '2':
            print("--------------------------")
            index, msg = input("请输入“索引,消息”的形式：").split(",")
            g_conn_pool[int(index)].sendall(msg.encode(encoding='utf8'))
        elif cmd == '3':
            exit()



class Servers(SRH):  
    def handle(self):  
        print('got connection from ',self.client_address  )
#        self.wfile.write('connection %s:%s at %s succeed!' % (host,port,ctime()))  
        msg = self.request.recv(1024) 
        if msg:   
            msg = str(msg, encoding='utf-8')
            msg=msg.strip()
            msglist = msg.split('$')
            #print(msg)
            global count_dic
            if msglist[0] == "totalcook":  # only use DLL
                print("OK\n")
                modulename=msglist[1]
                modulename=modulename.strip()
                if modulename in count_dic:
                    count_dic[modulename][0]+=1    # add count
                    count_dic[modulename][1]+=1    # means will use cali DLL
                else:
                    count_dic[modulename]=[1, 1]   # add item, and will use cali DLL
                pprint.pprint(count_dic)
                self.request.send(bytes("e", "utf-8"))  
            else:
                if msglist[0] == "totalcong":  # only use DLL
                    print("NG\n")
                    modulename=msglist[1]
                    modulename=modulename.strip()
                    if modulename in count_dic:
                        count_dic[modulename][0]+=1    # add count
                    else:
                        count_dic[modulename]=[1, 0]   # add item, but will not use cali DLL
                    pprint.pprint(count_dic)
                    self.request.send(bytes("e", "utf-8"))  
                else:
                    print("RAW\n")
                    fuseid = msglist[0]
                    msglist_length = len(msglist)
                    if msglist_length == 2:
                        module_flag = msglist[1]
                        txtname = "E:\\DPCdetect\\Server\\TXT\\"+fuseid+"-"+module_flag+".txt"
                        f=open(txtname,'w')
                        f.write(fuseid+','+module_flag)
                        f.close()
                        self.request.send(bytes("e", "utf-8"))  

                    else:
                        module_flag = msglist[-1]
                        txtname = "E:\\DPCdetect\\Server\\TXT\\"+fuseid+"-"+module_flag+".txt"
                        f=open(txtname,'w')
                        for mm in msglist:
                            print(mm)
                            f.write(mm+',')
                        f.close()

            print ("RECV from ", self.client_address[0]  )
            
        
    def finish(self):
        self.request.sendall(bytes("e", "utf-8"))


def runmyserver():
    print ('server is running....'  )
    server = socketserver.ThreadingTCPServer(addr,Servers)  
    server.serve_forever()  
    
    
def runsavecount():
    while True:
        pkl_file = open('E:\\DPCdetect\\Server\\dic.pkl', 'wb')
        pickle.dump(count_dic, pkl_file)
        pkl_file.close()
        print("Has save: ")
        pprint.pprint(count_dic)
        time.sleep(10)
