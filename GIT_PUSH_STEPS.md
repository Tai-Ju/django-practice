# 推送到 GitHub 的步驟

請在專案資料夾 **djangoproject** 裡開啟終端機（PowerShell 或 CMD），然後依序執行：

## 1. 進入專案目錄（若尚未在此）

```powershell
cd "c:\ruruproject\django part1\djangoproject"
```

## 2. 若尚未初始化 Git（或 .git 不完整），先初始化

```powershell
git init
```

## 3. 加入遠端

```powershell
git remote add origin https://github.com/Tai-Ju/Django-part1.git
```

若出現「remote origin already exists」，可先刪除再加：

```powershell
git remote remove origin
git remote add origin https://github.com/Tai-Ju/Django-part1.git
```

## 4. 加入所有檔案並提交

```powershell
git add .
git commit -m "Initial commit: Django ecommerce project with Railway deploy config"
```

## 5. 設為 main 分支並推送到 GitHub

```powershell
git branch -M main
git push -u origin main
```

若 GitHub 要求登入，請用 **Personal Access Token** 當密碼，或使用 GitHub Desktop / Git Credential Manager。

---

**說明：** 專案已包含 `.gitignore`，會排除 `db.sqlite3`、`__pycache__`、`.venv`、`staticfiles` 等，不會被推上去。
