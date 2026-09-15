# SenPlayer 图标库

自用图标订阅，在 SenPlayer / Emby 客户端「图标库」入口填入订阅地址即可加载。

**订阅地址（jsDelivr，国内可直连）**

```
https://cdn.jsdelivr.net/gh/IPJIA/senplayer-icons@main/manifest.json
```

**备用（GitHub Raw，即时生效）**

```
https://raw.githubusercontent.com/IPJIA/senplayer-icons/main/manifest.json
```

图标原样保存在 icons/ 目录，清单为标准格式：`{"name", "description", "icons":[{"name","url"}]}`。
更新图标：把新图放进本地 icons/ 后，重跑 `python upload_github.py` 即可。
