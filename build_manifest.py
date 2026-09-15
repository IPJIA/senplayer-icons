# -*- coding: utf-8 -*-
"""SenPlayer 图标库清单生成器
扫描 icons/ 目录，生成带绝对地址的 manifest.json。
用法：python build_manifest.py [基础地址，如 http://192.168.1.5:8000]（不填则自动检测局域网 IP）
"""
import json, os, re, socket, sys, urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))
ICONS_DIR = os.path.join(ROOT, "icons")

def lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"
    finally:
        s.close()

BASE = (sys.argv[1] if len(sys.argv) > 1 else "http://%s:8000" % lan_ip()).rstrip("/")

TAG_RULES = [
    ("导航", ["activity", "back", "bottom", "front", "menu", "home"]),
    ("体位", ["anal", "cowgirl", "doggy", "dog", "licking", "oral", "sex"]),
    ("用品", ["condom", "dildo", "penis", "toy", "ring", "lube"]),
    ("人物", ["man", "woman", "prostitution", "worker", "girl", "boy"]),
]

def tags_for(name):
    low = name.lower()
    return [t for t, kws in TAG_RULES if any(k in low for k in kws)]

def main():
    entries = []
    for fn in sorted(os.listdir(ICONS_DIR)):
        if not fn.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg", ".ico")):
            continue
        name = re.sub(r"^icons8[-_]?", "", fn)
        name = re.sub(r"\.(png|jpg|jpeg|webp|gif|svg|ico)$", "", name, flags=re.I)
        rel = "icons/" + urllib.parse.quote(fn)
        url = BASE + "/" + rel
        entry = {
            "name": name,
            "file": rel,
            "url": url,
            "src": url,
            "icon": url,
            "path": url,
            "tags": tags_for(name),
        }
        entries.append(entry)
    manifest = {
        "name": "SenPlayer 图标库",
        "description": "本地图标清单，与 index.html 中的 ICONS 数组保持同步维护",
        "base": "icons/",
        "icons": entries,
        "list": entries,
    }
    with open(os.path.join(ROOT, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    print("OK 已生成 manifest.json，共 %d 个图标，基础地址：%s" % (len(entries), BASE))

if __name__ == "__main__":
    main()
