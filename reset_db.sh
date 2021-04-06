sudo rm -r mysql/data
mkdir mysql/data
printf "*\n!.gitignore" > mysql/data/.gitignore

# rm datum/project/db.sqlite3
rm -r datum/project/accounts/migrations
mkdir datum/project/accounts/migrations
touch datum/project/accounts/migrations/__init__.py

rm -r datum/project/api/migrations
mkdir datum/project/api/migrations
touch datum/project/api/migrations/__init__.py
