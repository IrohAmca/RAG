import dotenv
import argparse

from os import getenv
from torch import cuda

dotenv.load_dotenv(".env")
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--device", type=str, help="Device to use", default="cuda" if cuda.is_available() else "cpu", choices=["cuda", "cpu"])
parser_db = parser.add_argument_group("Database Arguments")
parser_db.add_argument("--uselocal", action="store_true", help="Use local database instead of server. (uses: MONGO_LOCAL in .env)", default=False)
parser_db.add_argument("--db", type=str, help="Database name (default: DATABASE in .env)", default=getenv("DATABASE"))
parser_db.add_argument("--collection", type=str, help="Collection name (default: COLLECTION in .env)", default=getenv("COLLECTION"))
args = parser.parse_args()

mongo_uri = getenv("MONGO_LOCAL") if args.uselocal else getenv("MONGO_SERVER")
args.mongo_uri = mongo_uri

if __name__ == "__main__":
    import main
    main.main(args)
