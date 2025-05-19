# reorganize.py

import os
import shutil
import textwrap

def main():
    # 1) 프로젝트 루트 경로
    root = os.path.abspath(os.path.dirname(__file__))

    # 2) 패키지 소스가 들어갈 디렉터리(src/naver_searchad) 생성
    src_pkg = os.path.join(root, "src", "naver_searchad")
    os.makedirs(src_pkg, exist_ok=True)

    # 3) 루트에 있던 모듈 파일들 이동
    modules = [
        "auth.py","accounts.py","adgroups.py","ads.py","campaigns.py",
        "keywords.py","targets.py","stats.py","statreports.py",
        "updates.py","utils.py"
    ]
    for m in modules:
        src = os.path.join(root, m)
        if os.path.exists(src):
            shutil.move(src, src_pkg)
            print(f"Moved module: {m} → src/naver_searchad/{m}")

    # 4) 패키지 인식용 __init__.py 생성
    for pkg_dir in (src_pkg, os.path.join(root, "examples")):
        init_f = os.path.join(pkg_dir, "__init__.py")
        if not os.path.exists(init_f):
            open(init_f, "a").close()
            print(f"Created: {os.path.relpath(init_f, root)}")

    # 5) setup.py 덮어쓰기
    setup_py = os.path.join(root, "setup.py")
    setup_content = textwrap.dedent("""\
        from setuptools import setup, find_packages

        setup(
            name="naver_searchad",
            version="0.1.0",
            description="Wrapper for Naver Search Ads API",
            author="Your Name",
            package_dir={"": "src"},
            packages=find_packages("src"),
            install_requires=[
                "requests>=2.25.0",
                "beautifulsoup4>=4.9.0",
                "python-dotenv>=0.21.0"
            ],
            python_requires=">=3.7",
        )
    """)
    with open(setup_py, "w", encoding="utf-8") as f:
        f.write(setup_content)
    print("Overwritten: setup.py")

    # 6) requirements.txt 덮어쓰기
    req_txt = os.path.join(root, "requirements.txt")
    req_content = textwrap.dedent("""\
        requests>=2.25.0
        beautifulsoup4>=4.9.0
        python-dotenv>=0.21.0
    """)
    with open(req_txt, "w", encoding="utf-8") as f:
        f.write(req_content)
    print("Overwritten: requirements.txt")

    print("✅ Reorganization complete!")

if __name__ == "__main__":
    main()
