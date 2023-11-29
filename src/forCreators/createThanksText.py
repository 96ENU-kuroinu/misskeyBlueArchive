import requests
import pprint
import json
import sys

# 起動コマンド python createThanksText.py 対象のニコニコ静画ID(im...)

# 作者自身の名前を設定してください
MY_NAME         = 'くろいぬ'
# クリップのリンク等、ニコニ広告の有無に関係なく出力したい定型文をここに記入してください
TEMPLATE_TEXT   = '●ブルアカイラスト一覧 clip/3415499<br>●ブルアカ漫画一覧 clip/3415500<br>'

def getAdvertiserNames(id):
    """
    ニコニ広告してくれた人の名前・貢ポイント数を取得する

    Parameters
    ----------
    id : string
        取得対象のニコニコ静画ID(im...)
    """

    apiUrl = 'https://api.nicoad.nicovideo.jp/v1/contents/seiga/' + id + '/ranking/contribution?limit=10'
    response = requests.get(apiUrl)

    json_dict = response.json()

    result = []
    for ranks in json_dict['data']['ranking']:
        # 自分で行ったニコニ広告は出力しない
        if ranks['advertiserName'] == MY_NAME:
            continue
        result.append(ranks['advertiserName'] + 'さん' + ' (' + str(ranks['totalContribution']) +'貢)<br>')

    return result

if __name__ == '__main__':
    args = sys.argv
    if len(args) == 2:
        outputTexts = ['●前作: ' + args[1] + '<br>', TEMPLATE_TEXT]
        advertiserNames = getAdvertiserNames(args[1])

        if len(advertiserNames) > 0:
            outputTexts.extend(['<br>前作へのニコニ広告ありがとうございます<br>'])
            outputTexts.extend(advertiserNames)

        for outputText in outputTexts:
            print(outputText)
    else:
        print('ニコニコ静画のID(im...)を引数に指定してください')