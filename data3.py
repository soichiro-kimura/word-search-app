import json

def convert_json_to_js_file(input_filename, output_filename):
    try:
        # JSONファイルを読み込む
        with open(input_filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        results = []
        for item in data:
            word = item.get("word", "")
            # 意味の中にダブルクォーテーションがある場合に備えてエスケープ処理
            meaning = item.get("meaning", "").replace('"', '\\"')
            
            # 指定の形式に整形
            entry = f'{{ word: "{word}", meaning: "{meaning}", book: "鉄壁" }},'
            results.append(entry)
            
        # ファイルに書き出し
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(results))
            
        print(f"変換完了！ {len(results)}件を {output_filename} に保存しました。")

    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    # 元のJSONファイル名を指定してください
    convert_json_to_js_file('data.json', 'output.txt')