#-*- coding:utf-8 -*-
import sys

supported_list = [
        'Baidu',
        'Bing',
        #'cattle',
        'Google',
        'Tencent',
        'Youdao'
        ]
supported_lang = [
        'auto',
        'en',
        'zh-CN'
        ]

def lang_repr(dict_src:str, lang:str):
    if dict_src == 'Baidu':
        if lang == 'zh-CN':
            lang = 'zh'
    elif dict_src == 'Bing':
        if lang == 'zh-CN':
            lang = 'zh-Hans'
    elif dict_src == 'Google':
        pass
    elif dict_src == 'Tencent':
        if lang == 'zh-CN':
            lang = 'zh'
    elif dict_src == 'Youdao':
        if lang == 'zh-CN':
            lang = 'zh-CHS'
        elif lang == 'auto':
            lang = 'AUTO'
    return lang

if __name__ == '__main__':
    dict_src = None
    to_lang = 'zh-CN'
    from_lang = 'auto'
    if len(sys.argv) > 1:
        dict_src = sys.argv[1]
    if (dict_src is None) or (dict_src not in supported_list):
        print('''usage: {} <dict_src>
        <dict_src> may be
        {}
        '''.format(sys.argv[0], supported_list))
    if len(sys.argv) > 2:
        to_lang = sys.argv[2]
        if to_lang not in supported_lang:
            print("lang:", supported_lang)
    if len(sys.argv) > 3:
        from_lang = sys.argv[3]
        if from_lang not in supported_lang:
            print("lang:", supported_lang)
    # params done
    from_lang = lang_repr(dict_src, from_lang)
    to_lang = lang_repr(dict_src, to_lang)

    content = ''
    for line in sys.stdin:
        content += ' ' + line.strip()

    print(to_lang)
    if dict_src == 'Baidu':
        from Baidu import Baidu
        bd = Baidu()
        print(bd.translate(from_lang, to_lang, content))
    elif dict_src == 'Bing':
        from Bing import Bing
        bing = Bing()
        print(bing.translate(from_lang, to_lang, content))
    elif dict_src == 'Google':
        from Google import Google 
        gg = Google()
        print(gg.translate(from_lang, to_lang, content))
    elif dict_src == 'Tencent':
        from Tencent import TencentTrans
        tencent = TencentTrans()
        tencent.to_lang = to_lang
        print(tencent.get_trans_result(content))
    elif dict_src == 'Youdao':
        from Youdao import Youdao
        yd = Youdao()
        print(yd.translate(from_lang, to_lang, content))
    else:
        pass
