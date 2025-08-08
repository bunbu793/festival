import streamlit as st
import os

# 問題と選択肢を設定
questions = [
    {"question": "グイド・ミッキーのアニメーションを最初に書いたのは誰でしょう？", "options": ["マーク・ディヴィス", "ジョン・ヘイチ", "アブ・アイワークス"], "answer": "アブ。アイワークス"},
    {"question": "世界初のミッキーの商品は何でしょうか？", "options": ["食器", "ぬいぐるみ", "ノート"], "answer": "ノート"},
    {"question": "ミッキーの名付け親は誰？？", "options": ["たかし", "ディズニー", "リリアン"], "answer": "リリアン"}
]

# セッションステートにスコアと現在の問題インデックスを保存
if 'score' not in st.session_state:
    st.session_state['score'] = 0
if 'current_question' not in st.session_state:
    st.session_state['current_question'] = 0
if 'answered' not in st.session_state:
    st.session_state['answered'] = False

# 現在の問題を取得
if st.session_state['current_question'] < len(questions):
    current_question = questions[st.session_state['current_question']]

    # 問題を表示
    st.write(current_question["question"])
    user_answer = st.radio("選択肢から選んでください:", current_question["options"], key=st.session_state['current_question'])

    # 回答ボタン
    if st.button('回答を確認') and not st.session_state['answered']:
        st.session_state['answered'] = True
        if user_answer == current_question["answer"]:
            st.success('正解です！')
            st.session_state['score'] += 1  # 正解ならスコアを増やす
        else:
            st.error('残念！不正解です。')

    # 次の問題に進むボタン（最後の問題では表示しない）
    if st.session_state['answered']:
        if st.session_state['current_question'] < len(questions) - 1:
            if st.button('次の問題に進む'):
                st.session_state['current_question'] += 1  # 次の問題に進む
                st.session_state['answered'] = False
        else:
            st.write(f"クイズ終了！あなたのスコア: {st.session_state['score']} 点")
            # 満点の場合にGIFを表示
            if st.session_state['score'] == len(questions):
                st.balloons()  # Streamlitのバルーンアニメーション
                # 正しいパスを指定してください
                gif_path = os.path.abspath("path_to_your_congratulations_gif.gif")
                if os.path.exists(gif_path):
                    st.image(gif_path, use_container_width=True)  # GIFを表示

else:
    st.write(f"現在のスコア: {st.session_state['score']} 点")