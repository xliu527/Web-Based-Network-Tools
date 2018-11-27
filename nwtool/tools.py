import subprocess, platform, re
from typing import List, Any

time_slow = 1


def ping(IP):
    # IP = "8.8.8.8"
    print(IP)
    para = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    print(type(IP))
    print(type(para))
    ping_cmd = "ping " + para + " " + IP
    useShell = not (platform.system().lower() == "windows")
    result = subprocess.run(args=ping_cmd, universal_newlines=True, shell=useShell, stdout=subprocess.PIPE)
    print(result)
    res = result.stdout.splitlines()[2]
    p = re.compile('.*byte.*')
    if not p.match(res):
        res = IP + ' is time out!!'
    return res


def group_ping():
    global time_slow
    with open('dstips.txt') as fp:
        addresses = fp.readlines()
    print(addresses)

    res_list = []
    for addrs in addresses:
    #   print(addrs)
        res = ping(addrs.split()[0])
        print(res)
#       res2 = slow_line(res, time_slow)
        res_list.append(res)
        print(res_list)
    # res_str = "\r\n".join(res_list)
    # print(res_str)
    ### mark result by list.
    res_pair_list = []
    pa = re.compile('.*out.*')
    for i in res_list:
        if pa.match(i):
            res_pair = [i, 0]
        elif slow_line(i, time_slow):
            res_pair = [i, 1]
        else:
            res_pair = [i, 2]
        res_pair_list.append(res_pair)
    # res_pair = [[x, 1] if slow_line(x, time_slow) else [x, 0] for x in res_list]
    print(res_pair_list)
    return res_pair_list


def slow_line(line, t):
    p = re.compile('.*time.(\d+)ms.*')
    h = p.match(line)
    print('latency = ' + h.group(1))
    if int(h.group(1)) > t:
        # line = r"<div><p style='color:Tomato;'>" + line + "</p></div>"
        # print(line)
        return 1
    else:
        return 0











