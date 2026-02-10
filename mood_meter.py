try:
    mood = int(input("今の気分を0〜100で入力: ").strip())
    mood = max(0, min(100, mood))  # 0〜100に補正

    if mood >= 80:
        print("最高。今日は攻めよう。")
    elif mood >= 60:
        print("いい感じ。このまま進もう。")
    elif mood >= 40:
        print("ぼちぼち。小さいタスクからいこう。")
    elif mood >= 20:
        print("省エネでOK。休憩を挟もう。")
    else:
        print("今日は守りの日。まず深呼吸。")
except ValueError:
    print("数字で入力してね。")
