import sys
from time import sleep


def viewBar(i):
    """
    进度条效果
    :param i:
    :return:
    """
    output = sys.stdout
    for count in range(0, i + 1):
        second = 0.1
        sleep(second)
        output.write('\rcomplete percent ----->:%.0f%%' % count)
    # output.flush()


viewBar(100)