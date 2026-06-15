# push.ps1 — Script push harian ke GitHub
# Cara pakai: klik kanan > Run with PowerShell, atau jalankan di terminal:
#   .\push.ps1

# Pindah ke direktori tempat script ini berada
Set-Location -Path $PSScriptRoot

Write-Host ""
Write-Host "===============================" -ForegroundColor Cyan
Write-Host "  Git Push Harian ke GitHub" -ForegroundColor Cyan
Write-Host "===============================" -ForegroundColor Cyan
Write-Host ""

# Cek apakah ada perubahan yang perlu di-commit
$status = git status --porcelain
if ([string]::IsNullOrWhiteSpace($status)) {
    Write-Host "[INFO] Tidak ada perubahan. Working tree bersih." -ForegroundColor Yellow
    Write-Host "       Tidak ada yang perlu di-push." -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Tekan Enter untuk keluar"
    exit
}

# Tampilkan ringkasan perubahan
Write-Host "[INFO] Perubahan terdeteksi:" -ForegroundColor Green
git status --short
Write-Host ""

# Stage semua perubahan
git add .
Write-Host "[OK] Semua perubahan telah di-stage." -ForegroundColor Green
Write-Host ""

# Minta commit message dari user
$commitMessage = Read-Host "Masukkan commit message (contoh: Latihan hari ini - loop & fungsi)"

# Validasi: commit message tidak boleh kosong
if ([string]::IsNullOrWhiteSpace($commitMessage)) {
    $tanggal = Get-Date -Format "yyyy-MM-dd HH:mm"
    $commitMessage = "Latihan Python - $tanggal"
    Write-Host "[INFO] Commit message kosong, menggunakan default: $commitMessage" -ForegroundColor Yellow
}

# Commit
git commit -m $commitMessage
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Commit gagal!" -ForegroundColor Red
    Read-Host "Tekan Enter untuk keluar"
    exit 1
}

Write-Host ""
Write-Host "[OK] Commit berhasil." -ForegroundColor Green
Write-Host ""

# Push ke GitHub
Write-Host "[INFO] Pushing ke origin/main..." -ForegroundColor Cyan
git push origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "===============================" -ForegroundColor Green
    Write-Host "  Push berhasil! Selamat!" -ForegroundColor Green
    Write-Host "===============================" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "[ERROR] Push gagal. Cek koneksi internet atau auth git kamu." -ForegroundColor Red
}

Write-Host ""
Read-Host "Tekan Enter untuk keluar"
