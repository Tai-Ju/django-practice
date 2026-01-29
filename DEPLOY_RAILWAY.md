# 部署到 Railway 說明

## 已完成的專案設定

- **requirements.txt**：已加入 `gunicorn`、`whitenoise`、`dj-database-url`
- **settings.py**：依環境變數切換 DEBUG、ALLOWED_HOSTS、資料庫、靜態檔
- **Procfile**：指定用 Gunicorn 啟動
- **railway.json**：部署時自動執行 migrate 與 collectstatic

## 在 Railway 上要做的設定

### 1. 建立專案並連線 Git

1. 到 [railway.app](https://railway.app) 登入，New Project → Deploy from GitHub repo，選此專案。
2. 部署成功後，Railway 會給一個網址，例如：`https://你的專案.up.railway.app`。

### 2. 設定環境變數（Variables）

在 Railway 專案 → 你的 Service → **Variables** 裡新增：

| 變數名稱 | 建議值 | 說明 |
|----------|--------|------|
| `DJANGO_SECRET_KEY` | 一串隨機密鑰（可於本機用 `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` 產生） | 生產環境必設，勿用預設值 |
| `DJANGO_DEBUG` | `False` | 正式環境請設為 False |
| `ALLOWED_HOSTS` | `你的專案.up.railway.app`（或你自訂網域） | 多個用逗號分隔，不要加空白 |
| `CSRF_TRUSTED_ORIGINS` | `https://你的專案.up.railway.app` | 與網址一致，用 https |

**若使用 Railway 內建 PostgreSQL：**

- 在專案裡新增 **PostgreSQL** 服務，Railway 會自動產生 `DATABASE_URL`。
- 在 **Variables** 中把 `DATABASE_URL` 加進「同一個 Service」的變數（若已自動帶入則不用再設）。
- 本專案已支援：有 `DATABASE_URL` 時會自動改用 PostgreSQL。

**若暫時不裝資料庫：**

- 不設定 `DATABASE_URL` 會使用 SQLite。注意：Railway 重啟或重新部署後 SQLite 資料會清空，僅適合測試。

### 3. 靜態檔案

已使用 **WhiteNoise**，部署時會依 `railway.json` 執行 `collectstatic`，不需額外設定。

### 4. 自訂網域（選用）

在 Railway Service → **Settings** → **Networking** → **Generate Domain** 可取得預設網域；若要綁自己的網域，在此加入 **Custom Domain** 後，記得把該網域加進 `ALLOWED_HOSTS` 和 `CSRF_TRUSTED_ORIGINS`。

---

## 本機測試生產模式（選用）

```bash
# 安裝依賴
pip install -r requirements.txt

# 收集靜態檔
python manage.py collectstatic --noinput

# 用 Gunicorn 跑（需先設好 PORT，例如 8000）
# Windows 可設：set PORT=8000
gunicorn djangoproject.wsgi --bind 0.0.0.0:8000
```

確認沒錯誤後再推到 Railway 部署。
