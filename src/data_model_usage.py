from pprint import pprint
import json

from colinkspace.backend import get_sample_posts_of_space


if __name__ == "__main__":
    space_content = get_sample_posts_of_space()
    space_content_as_json = json.dumps(space_content, ensure_ascii=False)
    print(json.dumps(space_content, ensure_ascii=False))
