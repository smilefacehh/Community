DROP TABLE IF EXISTS notice;

CREATE TABLE notice (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  content TEXT NOT NULL
);
