from src.utils.generate_mock_data import (
    generate_random_users, create_hacker_news_links_csv_file, write_app_data_files
)

def main():
    create_hacker_news_links_csv_file()
    generate_random_users(100)
    # delete tables
    # create tables
    # insert into tables
    # -- insert new user
    # -- create a new default space for new user
    # get a list of space_ids 
    write_app_data_files(100)
    # join and see which user has most shares
    # join and see which links was shared most

if __name__ == "__main__":
    # main()
    pass
