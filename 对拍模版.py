from typing import Callable


class BeatCode: # 对拍模版

    @staticmethod
    def run(ac_fun: Callable, my_fun: Callable, params: list) -> None:
        for i, param in enumerate(params):
            ac, my = str(ac_fun(*param)), str(my_fun(*param))
            if ac != my:
                print(str(i + 1) + ' / ' + str(len(params)))
                print("测试用例：\n" + str(param))
                print("预期结果：\n" + ac)
                print("你的输出：\n" + my)
                return