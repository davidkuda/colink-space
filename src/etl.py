from colinkspace.postgres_connection import PostgresConnection
from colinkspace.backend import write_new_users
from utils.generate_mock_data import generate_random_users

def main():
    pg = PostgresConnection()
    generate_random_users(10)
    pg.init_tables()
    users = read_users_from_csv()
    write_new_users(users)
    
    # join and see which user has most shares
    # join and see which links was shared most


def read_users_from_csv():
    PATH_USERS_CSV = "data/users.csv"
    users = []
    with open(PATH_USERS_CSV, "r") as file:
        headers = file.readline()
        for line in file:
            name, email = line.strip().split(",")
            users.append({
                "name": name,
                "email": email
            })
    return users
            

if __name__ == "__main__":
    main()
