from src.generate_mock_data import (generate_users, create_hacker_news_links_csv_file,
                                    write_app_data_files)


def main():
    generate_users(100)
    create_hacker_news_links_csv_file()
    write_app_data_files(100)
    
    # delete tables
    # create tables
    # insert into tables
    # join and see which user has most shares
    # join and see which links was shared most

if __name__ == "__main__":
    # main()
    pass
