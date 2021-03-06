# coding=utf-8
import aiml
import os
import sys

# 获取aiml的安装路径
def get_module_dir(name):
    print("module", sys.modules[name])
    path = getattr(sys.modules[name], '__file__', None)
    print(path)
    if not path:
        raise AttributeError('module %s has not attribute __file__' % name)
    return os.path.dirname(os.path.abspath(path))

def prepare():
    # 补充路径名称
    alice_path = get_module_dir('aiml') + '\\botdata\\alice'

    # 切换到语料库所在工作目录
    os.chdir(alice_path)

    # 创建机器人alice对象
    alice = aiml.Kernel()

    print("正在加载语料库")

    # 这里做一个判断
    # 如果是第一次加载语料库，就进入else部分，读取数据，同时保存资料至bot_brain.brn
    # 如果是之后再加载语料库，就不需要读取所有数据了，直接读取保存数据bot_brain.brn
    if os.path.isfile("bot_brain.brn"):
        alice.bootstrap(brainFile="bot_brain.brn")
    else:
        alice.learn("startup.xml")  # 加载...\\botdata\\alice\\startup.xml
        alice.respond('LOAD ALICE')  # 加载...\\botdata\\alice目录下的语料库
        alice.saveBrain("bot_brain.brn")
    print("数据加载完毕，开始对话\n")
    return alice

def getRespond(data):
    robot = prepare()
    response = robot.respond(data)  # 机器人应答
    # print(response)
    return response

# Reference: https://www.jb51.net/article/195347.htm