#!/usr/bin/env python
# tweepy-bots/bots/autotweet.py

import tweepy
import logging
"""
from config import create_api
"""
import time
import random
import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def create_api():
    consumer_key = "aFeI8XzKw8AG7orSry1TkQWg8"
    consumer_secret = "Z6Bf8T5tvIWnRuVEd01ifmLbfMK29KMg4q1WEMqblJ7J4zi8Eg"
    access_token = "1317731508535263232-n9eFyw27DeK6vwLb2mVWGqAd04hyDI"
    access_token_secret = "MgMVErDI1N8wKaQixExxmWQesCJpBlOZjdLd01dUFNDbw"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api

"""
ここにツイートの内容を記入
"""
tweets = ["新卒の就活は、早い者勝ちのイス取りゲームです。黙って動かないでいると、知らない内に「定員に達した」と負けが確定していきます。私はこれで逃した企業がありました。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"就活のスケジュールは、企業ごとに本当にバラバラです。３年生・修士１年生の夏の段階で募集がほぼ終わっている所さえあります。経団連のスケジュールに惑わされず、各企業の生の情報を集めましょう。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"新卒の就活は、仕事上の実績を問われない唯一の機会です。ここで内定した企業でどんな能力をつけられるかが、その後に企業内・転職先で生き残っていけるかに直結します。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"「大卒」というものは、ある種の資格として機能しているように感じます。運転免許のように、「大卒」でないだけで何故か応募できない仕事が多い。辛くても、無意味に思えても、大学を卒業するのが大切です。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"新卒採用の場において、その仕事に直結する実績を持っている人は限りなくゼロに近いです。もしあなたが、その実績を持っていたら、無双できますよ。例えば、ＩＴ企業応募者「プログラム書いたことあります」\n#就活 #21卒 #22卒 #23卒 #24卒",\
"質問の回答を考える時は、自分が人事担当になったつもりで自己評価するといいです。例えば志望動機。「待遇がよさそう」より「自分の○○な能力を活かせそうだから」な方が取りたいと感じませんか？\n#就活 #21卒 #22卒 #23卒 #24卒",\
"就活で何をやればいいか分からない時。合同説明会へ行き、自分の「絶対に嫌なこと」と「惹かれること」を集めてみましょう。自己分析と企業研究が同時に出来て、しかもやるべきことをやってる感も得られるのでオススメです。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"「この会社でどんな能力を伸ばせるか？」を念頭に置いて就活するといいです。能力は、その会社で自分が活躍できそうかの目安になります。将来の転職に使えそうかも分かります。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"総合職という枠組みで、どんな能力を伸ばせそうか見当も付かない所は地雷です。配属ガチャに外れると、自分に全く合わない職種、市場価値が著しく低い職種に回される可能性があります。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"ジョブローテーション方式は、メリットよりデメリットが圧倒的に大きいです。メリットは、入社時点でやりたいことが分からなくても大丈夫。デメリットは、広く浅い能力しか身に付かず、会社を離れたらやっていけなくなる。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"就活の目的は、需要と汎用性の高い能力を身につけられる環境の獲得です。そんな能力があれば、会社でも活躍でき、いざ転職の時にも役立ちます。能力に注目して就活を進めましょう。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"気力がなくなる、いわゆる就活うつの時は。肉食って寝ましょう。無理なときは無理、回復に専念しましょう。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"既卒か留年かで迷ったら。間違いなく卒業したほうがいいです。卒業後３年程度は新卒と同じ扱いになりますので、全くデメリットはありません。逆に留年して就活しても、もしミスって卒業できなかったら、内定が取り消されますよ。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"既卒で就活しましたが、新卒と全く遜色なく戦えました。私は吟味して選別した６社を受けて、うち４社から内定を貰えています。雑に就活をやるくらいなら、卒業前から戦略を練りつつ、卒業後も就活した方が実りが大きいです。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"既卒は選考で不利になりません。ＡＮＡ、電通、講談社、伊藤忠商事、三井物産、三菱商事、アクセンチュア、富士フイルム、野村総研、三菱ＵＦＪ銀行。これらの会社の人事担当に、直接質問して確認しました。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"「何か質問はありますか？」へは、面接官の役割ごとに質問を用意しておきましょう。現場レベル・管理職レベル・経営レベルに大別して用意すると吉。「質問はありません」は「興味がありません」と同義で死亡フラグです。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"「学生時代に力を入れたこと」は、その会社の業務に直結することか、スゲェと万人が思うことのどちらかにしましょう。ただ、直結しない場合がほとんどなので、なるべくスゲェことを言いましょう。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"「学生時代に力を入れたこと」でウケがいいのは、総じて人を使った経験です。リーダーや部長など、将来的に管理職になるのにふさわしいポテンシャルがあるかを推し量れるためです。リーダー経験、掴み取っていきましょう。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"「学生時代に力を入れたこと」で、個人的な努力を話す場合は、わかりやすい指標と高いレベルの両方が必要になります。例えば、英語を頑張りました→TOEICで900点取りました、のような感じです。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"面接やESでは、数字を使うことを意識するようにしましょう。英語を頑張った→TOEICで900点、バイトリーダーだった→バイトで8人の後輩をまとめていた、など。イメージしやすさが全然違ってきませんか？\n#就活 #21卒 #22卒 #23卒 #24卒",\
"面接の答えを暗記する必要はありませんが、面接練習の必要はあります。よくある質問に対して、回答に慣れておくことは、緊張する面接の場でしっかりと答える上で、極めて重要です。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"就活の要点は、「相手を知り、自己を知り、ターゲットを絞って戦略を練る」です。会社を知らなければ何もできません。自己分析が不十分だと、優先順位をつけられません。ターゲットを絞らないと、戦略を練れません。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"何からやればいいか分からないときは、とにかく動いてみること。私のオススメは、大学が行っている就活イベントに片っ端から参加してみることです。得体の知れない「就活」の、実体や戦い方が見えてくるでしょう。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"就活とポケモンは似ていて、相手と自分のわざのタイプを見極めるのが重要です。くさタイプのフシギバナにかえんほうしゃを使う＝IT系の企業に「プログラミングの経験があります」とぶつける、といった感じです。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"就活とポケモンは似ています。自分のわざの強さやタイプを見誤ると効果が薄いです。くさタイプのフシギバナにみずでっぽうを当てる＝コミュ力高い人材が欲しい会社の面接で、プログラミングの経験を推す、といった感じです。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"面接が苦手なら、10回練習しましょう。手段は、大学のキャリアセンターでも、一般の就職支援団体でも、友達でもなんでもいいです。面接は確実に避けては通れない道です。練習で苦手は「できる！」になります！\n#就活 #21卒 #22卒 #23卒 #24卒",\
"面接の質問に対して、話す内容が出てこない時。これは、自己分析が不足している可能性が高いです。自己分析を今一度やり直してみると、面接の質問に対する答えを導き出しやすくなります。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"「弊社の志望度は？」に対しては、「第一志望です」一択しかありません。最終的に残った2名の志望者、「第一志望です」と「ええと、第三志望ですね」のどちらに内定を出すと思いますか？\n#就活 #21卒 #22卒 #23卒 #24卒",\
"TOEICは就活生も人事も全員が知っている、最強の資格です。900点以上取れると、面接で強力な実績として語れる武器になります。これ1つで他の就活生に比べて、圧倒的優位性を確保できます。英語頑張って取りましょう、TOEIC 900点。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"TOEIC 900点は就活時も、その後もメリットだらけです。就活時には強力な実績として使えます。就活後には、TOEIC 900点持ってるだけで5万円もらえたり、転職時に有利に使えたりします。取得が大変でも価値のある資格です、頑張って取りましょう！\n#就活 #21卒 #22卒 #23卒 #24卒",\
"自己分析が難しいときは、家族や友達に他己分析をお願いすると効果的です。ただ、いきなり「私ってどんな人間？」と聞いても答えづらい。オススメ4項目はこちら↓\n「私の長所は？」\n「私の短所は？」\n「私の目立つところは？」\n「私の優秀なところは？」\n#就活 #21卒 #22卒 #23卒 #24卒",\
"自己分析は、所属団体に関してやるとやりやすいです。自分は何年生の時、どんな役職やポジションで、どんな語れる実績を作ってきたのか。分解してみると、漠然と思い出すより整理しやすいです。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"リクナビの使い方が分からなかったら。インターンの項目で場所と業界を1つに絞って、出てきたところを片っ端から回りましょう。オススメは、東京・IT業界です。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"面接の対策で、暗記はダメです。質問内容がちょっと変わっただけで対応不能になります。そしてなにより、多くの面接官が「暗記した内容を読み上げてる人は雰囲気で分かる」と言います。記憶するのは話す内容にとどめましょう。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"会社は自社に利益をもたらす人物を求めています。消費者の視点ではなく、自分はこの会社で何が出来るだろうという、生産者の視点に立てると吉です。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"就活の終わりは、ゴールであると共に新たなスタートでもあります。その会社で得られる能力はどんなもの？その能力は市場価値がどれくらい高い？将来を念頭に、進む会社を見極めましょう。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"「就活何やればいいのか分からない」状態が一番辛いです。私のブログに、方法と考え方を全部載せてあります。読めばその状態を脱することが出来ます。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"「需要と汎用性の高い能力が欲しい」だと、自己中心的なのではと心配する方へ。「その能力を使って御社に貢献しながら、自分のスキル・キャリアアップもできるから」の一言で、やる気のある新人という印象を掴めます。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"IT系を目指しながらも、話せる実績がないなら。ProgateでHTML/CSSコースを中級までやって、試行錯誤しながら自己PRホームページを作りましょう。「ゼロから独学でHTMLでホームページ作成」は、1週間でできます。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"IT系が気になるけど、自分がプログラミングとかできるか分からない時は。ProgateでHTML/CSSコースと、Rubyコースをやってみるといいです。ゼロの状態から、ちょっと出来るという自信と、語れる実績が作れます。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"プログラミングの適性は、やってみないと分かりません。とりあえずProgateでやってみるのがいいです。文系・理系・数学得意苦手、関係なし。やってみれば、できそうか、できないか、肌感で分かります。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"「何をやればいいか分からない」から発生する不安は、やるべきことが分かれば解決します。体系的にまとまった就活戦略が欲しかったら、私のブログを読んでみてください。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"就活セミナーや就活イベントについて。参加しまくることで多くの情報を得られますが、「就活全体の流れの中で、これはどこに位置づけられる？」という視点で臨むと、より経験をものにしやすいです。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"就活では、内定を得ることがゴールになりがちです。それは新たなスタートであり、「内定を得た会社で、自分はどんな能力を伸ばせる？」という視点こそ、幸せでやりがいのある労働に必要な考え方です。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"就活の目的は、「需要と汎用性の高い能力を、伸ばせる環境を手に入れること」です。能力があれば、会社に依存しない生き方ができ、転職もできる。しかしなにより、今いる会社に貢献でき、新たなチャンスを掴める。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"新卒の時点で、その会社の業務内容に直結する実績を持っている人なんて、百人に一人もいません。だから、今の自分に実績がないことは「普通」です。逆に、実績を作れれば、百人に一人の逸材になれるのです。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"選考スケジュールは会社ごとに全く違います。4月に説明会解禁、6月に選考開始などという会社は、ごく稀です。僕の場合は最速で、12月に選考開始、2月に内々定という会社もありました。合同説明会等で、会社ごとの生の情報を集めましょう。\n#就活 #21卒 #22卒 #23卒 #24卒",\
"就活うつになったら。いったん就活を中断し、心療内科へ行き、薬で対処しましょう。うつは心の風邪などという甘いものではなく、癌のように全身を蝕みます。手遅れになる前に、治療へ踏み切りましょう。\n#就活 #21卒 #22卒 #23卒 #24卒",\
]

"""
ツイートの総数から、整数の乱数生成
"""
def generate_random_number():
    rn = random.randrange(len(tweets))
    return rn

random_number = generate_random_number()
print(random_number)

hold = -1

"""
while hold != random_number:
    print("もちゃ")
    hold = random_number
else:
    print("おわり")
"""

"""
while hold != random_number:
    random_number = generate_random_number()
    print(random_number)
    print("TWEET")
    hold = random_number
    print(hold)
else:
    print("同じ！")
"""

while True:
    if random_number != hold and __name__ == "__main__":
        api = create_api()
        randomtweet = tweets[random_number]
        params = {"status": randomtweet}
        api.update_status(randomtweet)
        print("TWEET")
        logger.info("Waiting...")
        time.sleep(5)
        hold = random_number
        random_number = generate_random_number()
        print(hold)
        print(random_number)
    else:
        print("同じ！")
        print(hold)
        print(random_number)
        random_number = generate_random_number()
        print("再生成")
        print(random_number)
    


"""
def random_tweet():

    api = create_api()

    random_number = random.randrange(len(tweets))
    random_number2 = random_number
    

    randomtweet = tweets[random_number]
    params = {"status": randomtweet} 
    api.update_status(randomtweet)

def put_tweet():
    while True:
        random_tweet()
        logger.info("Waiting...")
        time.sleep(5)

if __name__ == "__main__":
    put_tweet()
"""