from google_play_scraper import reviews, Sort
import pandas as pd
import time
import random

def scrape_app_reviews(app_id, app_name, lang, country, total_count):
    all_reviews = []
    token = None

    print(f" Scraping {total_count} '{lang}' reviews for {app_name}...")
    
    while len(all_reviews) < total_count:
        try:
            batch, token = reviews(
                app_id,
                lang=lang,
                country=country,
                sort=Sort.NEWEST,
                count=min(200, total_count - len(all_reviews)),
                continuation_token=token
            )

            for r in batch:
                all_reviews.append({
                    'review_text': r['content'],
                    'rating': r['score'],
                    'date': r['at'],
                    'app_name': app_name,
                    'source': 'Google Play'
                })

            print(f"   {len(all_reviews)} reviews fetched so far for {app_name} ({lang})")

            if not token:
                break

            time.sleep(random.uniform(1, 2))

        except Exception as e:
            print(f"⚠️ Error scraping {app_name}: {e}")
            time.sleep(5)
            continue

    return pd.DataFrame(all_reviews)


def scrape_multiple_apps(apps_dict, lang, country, total_count, save_each=False, output_dir='data'):
    all_data = pd.DataFrame()

    for app_name, app_id in apps_dict.items():
        df = scrape_app_reviews(app_id, app_name, lang, country, total_count)
        all_data = pd.concat([all_data, df], ignore_index=True)

        if save_each:
            file_path = f"{output_dir}/{app_name.replace(' ', '_')}_{lang}.csv"
            df.to_csv(file_path, index=False)
            print(f" Saved {file_path}")

    return all_data


def deduplicate_reviews(df):
    return df.drop_duplicates(subset=["review_text", "date", "app_name"])
