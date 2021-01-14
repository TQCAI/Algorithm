# -*- coding: UTF-8 -*-
# !/usr/bin/python
# @time     :2019/5/17 15:17
# @author   :Mo
# @function :change chinese digit to Arab or reversed

import random

# number_to_chinese, 单位-数字
num_dict = {0: "零", 1: "一", 2: "二", 3: "三", 4: "四",
            5: "五", 6: "六", 7: "七", 8: "八", 9: "九"}
unit_map = [["", "十", "百", "千"], ["万", "十万", "百万", "千万"],
            ["亿", "十亿", "百亿", "千亿"], ["兆", "十兆", "百兆", "千兆"]]
unit_step = ["万", "亿", "兆"]


class number_to_chinese():
    """
       参考: https://github.com/tyong920/a2c
    """

    def __init__(self):
        self.result = ""

    def number_to_str_10000(self, data_str):
        """一万以内的数转成大写"""
        res = []
        count = 0
        # 倒转
        str_rev = reversed(data_str)  # seq -- 要转换的序列，可以是 tuple, string, list 或 range。返回一个反转的迭代器。
        for i in str_rev:
            if i is not "0":
                count_cos = count // 4  # 行
                count_col = count % 4  # 列
                res.append(unit_map[count_cos][count_col])
                res.append(num_dict[int(i)])
                count += 1
            else:
                count += 1
                if not res:
                    res.append("零")
                elif res[-1] is not "零":
                    res.append("零")
        # 再次倒序，这次变为正序了
        res.reverse()
        # 去掉"一十零"这样整数的“零”
        if res[-1] is "零" and len(res) is not 1:
            res.pop()

        return "".join(res)

    def number_to_str(self, data):
        """分段转化"""
        assert type(data) == float or int
        data_str = str(data)
        len_data = len(str(data_str))
        count_cos = len_data // 4  # 行
        count_col = len_data - count_cos * 4  # 列
        if count_col > 0: count_cos += 1

        res = ""
        for i in range(count_cos):
            if i == 0:
                data_in = data_str[-4:]
            elif i == count_cos - 1 and count_col > 0:
                data_in = data_str[:count_col]
            else:
                data_in = data_str[-(i + 1) * 4:-(i * 4)]
            res_ = self.number_to_str_10000(data_in)
            res = res_ + unit_map[i][0] + res
        return res

    def decimal_chinese(self, data):
        assert type(data) == float or int
        data_str = str(data)
        if "." not in data_str:
            res = self.number_to_str(data_str)
        else:
            data_str_split = data_str.split(".")
            if len(data_str_split) is 2:
                res_start = self.number_to_str(data_str_split[0])
                res_end = "".join([num_dict[int(number)] for number in data_str_split[1]])
                res = res_start + random.sample(["点", "."], 1)[0] + res_end
            else:
                res = str(data)
        return res


if __name__ == "__main__":
    ######  1.测试阿拉伯数字转中文  ########################################
    ntc = number_to_chinese()
    for i in range(1945, 2100):
        print(ntc.decimal_chinese(i))
    print(ntc.decimal_chinese(0.112354))
    print(ntc.decimal_chinese(1024.112354))