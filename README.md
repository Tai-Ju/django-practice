# 電商小站 (Django Part1)

以 Django 6 打造的簡易電商前端專案，包含首頁、商品列表、會員頁等，適合作為 Django 入門練習。
🌐 **GitHub Page 預覽**：[tai-ju.github.io/django-practice](https://tai-ju.github.io/django-practice/)

## 功能

- **首頁**：歡迎頁與精選商品展示
- **商品首頁**：商品卡片展示（含圖片）
- **商品列表**：從資料庫讀取 Product，以網格卡片呈現
- **會員 / 更多**：延伸頁面
- **後台**：Django Admin 管理商品

## 技術棧

- **Python** 3.12
- **Django** 6.0
- **資料庫**：SQLite（開發）/ 可選 PostgreSQL（如 Railway 部署）
- **靜態檔**：Whitenoise
- **字體**：Google Fonts（Noto Sans TC、Outfit）

## 專案結構

```
djangoproject/
├── djangoproject/     # 專案設定 (settings, urls)
├── ecommerce/         # 電商 app (models, views, urls)
├── templates/         # 全站模板
│   ├── base.html
│   ├── components/    # navbar, footer
│   ├── home.html
│   ├── product.html
│   └── ...
├── static/            # CSS、圖片
├── manage.py
└── requirements.txt
```

## 本地運行

### 1. 克隆專案

```bash
git clone https://github.com/Tai-Ju/Django-part1.git
cd Django-part1
```

### 2. 建立虛擬環境並安裝依賴

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # macOS / Linux

pip install -r requirements.txt
```

### 3. 資料庫遷移

```bash
python manage.py migrate
```

### 4. 建立超級用戶（可選，用於後台）

```bash
python manage.py createsuperuser
```

### 5. 啟動開發伺服器

```bash
python manage.py runserver
```

瀏覽 [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 即可看到首頁。

## 主要網址

| 路徑 | 說明 |
|------|------|
| `/` | 自動導向 `/ecommerce/` |
| `/ecommerce/` | 首頁 |
| `/ecommerce/home/` | 商品首頁 |
| `/ecommerce/product/` | 商品列表（資料庫） |
| `/ecommerce/member/` | 會員頁 |
| `/admin/` | Django 後台 |

## 環境變數（選填）

部署時可設定：

- `DJANGO_SECRET_KEY`：密鑰（正式環境必設）
- `DJANGO_DEBUG`：`False` 關閉除錯
- `ALLOWED_HOSTS`：允許的網域
- `DATABASE_URL`：資料庫連線（如 Railway 提供的 PostgreSQL）
- `CSRF_TRUSTED_ORIGINS`：表單/登入信任來源

## 部署

專案內含 `Procfile`、`railway.json`，可部署至 [Railway](https://railway.app)。詳細步驟見 `DEPLOY_RAILWAY.md`。

## 授權與用途

本專案僅供學習使用。

---

**Django Part1 · 電商小站**
