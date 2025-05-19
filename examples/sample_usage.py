# examples/sample_usage.py

import os
import argparse
import logging
from dotenv import load_dotenv
from naver_searchad import (
    SearchAdClient,
    list_campaigns,
    suggest_keywords,
    get_stat,
    fetch_release_notes
)

def parse_args():
    parser = argparse.ArgumentParser(description="Naver Search Ads 샘플 실행기")
    parser.add_argument("-t", "--term", type=str, default="실버바", help="키워드 제안 검색어")
    return parser.parse_args()

def main(term):
    load_dotenv()
    client = SearchAdClient(
        os.getenv("NAVER_ACCESS_KEY"),
        os.getenv("NAVER_SECRET_KEY"),
        os.getenv("NAVER_CUSTOMER_ID")
    )

    logging.info("▶ 캠페인 목록 요청 중...")
    campaigns = list_campaigns(client)
    logging.info(f"✅ Campaigns: {campaigns}")

    logging.info(f"▶ ‘{term}’ 키워드 제안 요청 중...")
    suggestions = suggest_keywords(client, term=term)
    logging.info(f"✅ Suggestions: {suggestions}")

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S"
    )
    args = parse_args()
    main(args.term)
