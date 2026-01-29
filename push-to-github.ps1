# Push to GitHub script - run in PowerShell: .\push-to-github.ps1

$ErrorActionPreference = "Stop"
$projectPath = $PSScriptRoot

Set-Location $projectPath

# Clean lock files if any
if (Test-Path ".git\index.lock") { Remove-Item ".git\index.lock" -Force }
if (Test-Path ".git\config.lock") { Remove-Item ".git\config.lock" -Force }

# Init if no .git
if (-not (Test-Path ".git\config")) {
    Write-Host "Initializing Git..."
    git init
    git remote add origin https://github.com/Tai-Ju/Django-part1.git
}

# Ensure remote
if (-not (git remote get-url origin 2>$null)) {
    git remote add origin https://github.com/Tai-Ju/Django-part1.git
}

Write-Host "Adding files and committing..."
git add .
git status

$msg = "Initial commit: Django ecommerce project"
git commit -m $msg

Write-Host "Pushing to GitHub (origin main)..."
git branch -M main
git push -u origin main

Write-Host "Done. Check: https://github.com/Tai-Ju/Django-part1"
