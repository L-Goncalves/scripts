Get-ChildItem -Path "D:\" -Directory -Recurse -Filter "node_modules" -ErrorAction SilentlyContinue | ForEach-Object {
    Write-Host "Found: $($_.FullName)" -ForegroundColor Green
    $size = (Get-ChildItem $_.FullName -Recurse -ErrorAction SilentlyContinue | Measure-Object -Property Length -Sum).Sum / 1GB
    Write-Host "  Size: $([math]::Round($size, 2)) GB" -ForegroundColor Yellow
    
    Write-Host "  Deleting..." -ForegroundColor Red
    Remove-Item -Path $_.FullName -Recurse -Force -ErrorAction SilentlyContinue
    Write-Host "  ✓ Deleted !`n" -ForegroundColor Cyan
}

Write-Host "=== CLEAN COMPLETE ===" -ForegroundColor Green