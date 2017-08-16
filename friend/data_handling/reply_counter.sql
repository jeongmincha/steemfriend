DECLARE @Author VARCHAR(50) = 
DECLARE @TopRecentPosts INT = 150

;WITH a AS (
    SELECT author, permlink
      FROM Comments (NOLOCK)
     WHERE parent_author = @Author AND parent_permlink IN (
             SELECT TOP(@TopRecentPosts) permlink
               FROM Comments (NOLOCK)
              WHERE author = @Author
                AND depth = 0
                AND title > ''
              ORDER BY Id DESC
           )
       AND author <> @Author

     UNION ALL

    SELECT c.author, c.permlink
      FROM Comments c (NOLOCK), a
     WHERE c.parent_author = a.author AND c.parent_permlink = a.permlink
       AND c.author <> @Author
)
SELECT author, COUNT(*) replies
  FROM a
 GROUP BY author
 ORDER BY replies DESC
