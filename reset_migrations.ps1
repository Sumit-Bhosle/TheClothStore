Write-Host "🚀 Deleting migration files (except __init__.py)..."

Get-ChildItem -Recurse -Include *.py -Path *\migrations\ | Where-Object Name -ne '__init__.py' | Remove-Item -Force
Get-ChildItem -Recurse -Include __pycache__ -Path *\migrations\ | Remove-Item -Recurse -Force

Write-Host "✅ All migration files deleted."

Write-Host "🎉 Migration reset complete."
