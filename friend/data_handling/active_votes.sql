DECLARE @Author VARCHAR(50) = 
DECLARE @TopRecentPosts INT = 500

SELECT TOP(@TopRecentPosts) author, permlink, active_votes, reblogged_by, children
    FROM Comments (NOLOCK)
  WHERE author = @Author AND
    parent_author = '' AND
    active_votes != '[]'
    ORDER BY id DESC
