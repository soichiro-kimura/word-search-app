import re

def convert_vocabulary_file(input_filename, output_filename):
    results = []
    
    try:
        with open(input_filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                
                # 正規表現で「数字」「英単語」「それ以降（意味）」に分割
                # パターン: 数字 - 空白 - 英単語 - 空白 - 意味
                match = re.match(r'^\d+\s+([a-zA-Z\-\s\']+)\s+(.*)$', line)
                
                if match:
                    word = match.group(1).strip()
                    meaning = match.group(2).strip()
                    
                    # ダブルクォーテーションをエスケープ
                    meaning = meaning.replace('"', '\\"')
                    
                    entry = f'{{ word: "{word}", meaning: "{meaning}", book: "鉄壁" }},'
                    results.append(entry)
                else:
                    # パターンに合わなかった行を特定するために表示（デバッグ用）
                    print(f"スキップされた行: {line}")

        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(results))
            
        print(f"\n変換完了！ {len(results)}語を {output_filename} に保存しました。")

    except FileNotFoundError:
        print(f"エラー: {input_filename} が見つかりません。")

if __name__ == "__main__":
    convert_vocabulary_file('input.txt', 'output.txt')