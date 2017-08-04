import psycopg2
class DatabaseManager:
    """ This class contains methods used for getting connection and getting data """

    DATABASE_NAME = "news"
    DATABASE_USER = "vagrant"
    DATABASE_PASSWORD = "root"
    
    QUERY_POPULAR_THREE_ARTICLES = "select a.title, ratingtable.total from articles a join (select a.slug, count(*) total from log l join articles a on '/article/' || a.slug = l.path GROUP BY a.slug order by total desc) ratingtable on a.slug = ratingtable.slug order by total desc limit 3"
    QUERY_POPULAR_AUTHORS = "select au.name, tableauthorlog.totalview from authors au join (select author, sum(tablearticlelog.total) totalview from (select a.author, ratingtable.total from articles a join (select a.slug, count(*) total from log l join articles a on '/article/' || a.slug = l.path GROUP BY a.slug order by total desc) ratingtable on a.slug = ratingtable.slug order by total desc) tablearticlelog group by author) tableauthorlog on au.id = tableauthorlog.author order by totalview desc"
    QUERY_ERROR_REQUEST = "select onlydate, errorpercent from (select successfultable.onlydate , round( CAST(float8 (failtable.count::float/(successfultable.count+failtable.count)) as numeric), 2) as errorpercent from (select status, to_char(time, 'YYYY-MM-DD') onlydate, count(*) from log where status = '200 OK' group by status, onlydate) as successfultable, (select status, to_char(time, 'YYYY-MM-DD') onlydate, count(*) from log where status != '200 OK' group by status, onlydate ) as failtable where successfultable.onlydate = failtable.onlydate order by onlydate) as errorlogtable where errorpercent > 0.01"

    # This method is used to get connection to database
    def get_connection(self):
#        db = psycopg2.connect(database=DATABASE_NAME)
        db = psycopg2.connect(database=self.DATABASE_NAME)
        return db

    # This method is used for all queries
    def execute_query(self, query_name):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query_name)
        results = cursor.fetchall()
        conn.close()
        return results

    def get_popular_three_articles(self):
        return self.execute_query(self.QUERY_POPULAR_THREE_ARTICLES)

    def get_popular_authors(self):
        return self.execute_query(self.QUERY_POPULAR_AUTHORS)

    def get_error_requests(self):
        return self.execute_query(self.QUERY_ERROR_REQUEST)
