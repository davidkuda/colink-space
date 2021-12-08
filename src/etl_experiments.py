from pprint import pprint

from colinkspace.data_quality_checker import DataQualityChecker


def transform_posts_to_json(posts: list):
    new_ds = []
    for post in posts:
        new_ds.append({
            "comment": post[0],
            "url": post[1],
            "title": post[2],
            "description": post[3],
            "image_url": post[4],
            "date": str(post[5])
        })
    data = {
        "data": new_ds
    }
    return data

if __name__ == "__main__":
    posts = DataQualityChecker.get_sample_posts_of_space()
    d = transform_posts_to_json(posts)
    pprint(d)