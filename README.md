zcf520.py
=========
一个解密游戏的Demo
将拼音首字母与姓名进行匹配 
zcf函数如果匹配成功则返回姓名列表的下标,否则返回None
- 利用pinyin库：https://github.com/cleverdeng/pinyin.py

Example:
    test2 = ["王朗", "诸葛孔明", "孙悟空","猪八戒","罗贯中", "曹雪芹", "沙和尚", "牛魔王", "白骨精", "诸葛孔明"]


    $ python zcf520.py
    关键词  :  zgkm
    诸葛孔明

    $ python zcf520.py
    关键词  :  wl
    王朗

    $ python zcf520.py
    关键词  :  nmw
    牛魔王
    $ python zcf520.py
    关键词  :  zgl
    未匹配
