-- Schema: CREATE TABLE "darts" ("x" REAL, "y" REAL, score INTEGER);
-- Task: update the darts table and set the score based on the x and y values.
UPDATE darts SET score = CASE WHEN SQRT(POWER(x, 2) + POWER(y, 2)) <= 1 THEN 10 WHEN SQRT(POWER(x, 2) + POWER(y, 2)) <= 5 THEN 5 WHEN SQRT(POWER(x, 2) + POWER(y, 2)) <= 10 THEN 1 ELSE 0 END;