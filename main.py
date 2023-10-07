import sys
import markdown


def get_template():
    """テンプレートの読み込み"""
    with open("./base.txt", "r", encoding="utf-8") as f:
        template = f.read()

    return template


def main() -> None:
    with open(sys.argv[2], "r", encoding="utf-8") as rf:
        f_string = rf.read()
    md = markdown.Markdown()
    convert_txt = md.convert(f_string)

    html_base = get_template()
    new_text = html_base.replace("{{insert_text}}", convert_txt)

    with open(sys.argv[3], "w", encoding="utf-8", errors="xmlcharrefreplace") as wf:
        wf.write(new_text)


if __name__ == '__main__':
    # 起動コマンド：python3 file-converter.py markdown inputfile outputfile
    try:
        if sys.argv[2] != "markdown" and len(sys.argv) != 4:
            print("引数が正しく入力されてません。再度実行してください。")
            sys.exit()
    except IndexError:
        print("引数が正しく入力されてません。再度実行してください。")
        sys.exit()

    main()
