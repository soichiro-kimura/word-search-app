import re

def convert_vocabulary_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as f:
            # 全行読み込んで、空行を除去したリストを作る
            lines = [line.strip() for line in f if line.strip()]
        
        results = []
        
        # 3行1セット（1:番号, 2:単語, 3:意味）で処理
        # 万が一データが欠けていてもエラーにならないよう range を調整
        for i in range(0, len(lines) - 2, 3):
            # 数字の行であることを確認（念のため）
            if lines[i].isdigit():
                word = lines[i+1]
                meaning = lines[i+2]
                
                # ダブルクォーテーションをエスケープ（意味の中に " が含まれる場合への対処）
                meaning = meaning.replace('"', '\\"')
                
                entry = f'{{ word: "{word}", meaning: "{meaning}", book: "鉄壁" }},'
                results.append(entry)

        # ファイルに書き出し
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(results))
            
        print(f"変換が完了しました！ {len(results)}語を {output_filename} に保存しました。")

    except FileNotFoundError:
        print(f"エラー: {input_filename} が見つかりません。")
    except Exception as e:
        print(f"予期せぬエラーが発生しました: {e}")

# 実行
if __name__ == "__main__":
    # 元のデータが入ったファイル名を指定してください
    convert_vocabulary_file('input.txt', 'output.txt')