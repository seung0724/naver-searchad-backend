# reorganize.ps1
# 프로젝트 루트 경로
$root = "C:\Users\user\Desktop\naver_searchad"

# 1) src\naver_searchad 폴더 생성
$pkg = Join-Path $root "src\naver_searchad"
New-Item -ItemType Directory -Path $pkg -Force | Out-Null

# 2) 최상위 .py 모듈 파일 이동
Get-ChildItem -Path $root -File -Filter "*.py" `
  | Where-Object { $_.Name -notin @("setup.py","requirements.txt","README.md") } `
  | Move-Item -Destination $pkg

# 3) 패키지용 __init__.py 생성
New-Item -ItemType File -Path (Join-Path $pkg "__init__.py") -Force | Out-Null

# 4) examples 폴더에도 __init__.py (optional)
$ex = Join-Path $root "examples"
New-Item -ItemType File -Path (Join-Path $ex "__init__.py") -Force | Out-Null

# 5) setup.py 내용을 src 기반으로 교체
$setup = Join-Path $root "setup.py"
@"
from setuptools import setup, find_packages

setup(
    name="naver_searchad",
    version="0.1.0",
    description="Wrapper for Naver Search Ads API",
    author="Your Name",
    package_dir={ "": "src" },
    packages=find_packages("src"),
    install_requires=[
        "requests>=2.25.0",
        "beautifulsoup4>=4.9.0",
        "python-dotenv>=0.21.0"
    ],
    python_requires=">=3.7",
)
"@ | Set-Content -Path $setup -Encoding UTF8

Write-Host "✅ 프로젝트가 src 기반 구조로 재정리 되었습니다."
