from database.database_manager import DatabaseManager

database = DatabaseManager()

# Get top 3 articles 
top_three_articles = database.get_popular_three_articles()

print("1. What are the most popular three articles of all time?")

for article in top_three_articles:
    print("\"" + article[0] + "\" -- " + str(article[1]) + " views")

# Get top authors of all time

print("2. Who are the most popular article authors of all time?")

top_authors = database.get_popular_authors()

for authors in top_authors:
    print(authors[0] + " -- " + str(authors[1]) + " views")


# Get error requests which are more than 1%

print("3. On which days did more than 1% of requests lead to errors?");

fail_request = database.get_error_requests();

for bad_request in fail_request:
    print(bad_request[0] + " -- " + str(bad_request[1]) + "% errors")
