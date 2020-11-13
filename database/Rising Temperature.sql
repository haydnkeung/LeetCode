SELECT t1.id FROM Weather t1, Weather t2 WHERE DATE_SUB(t1.recordDate, INTERVAL 1 DAY) = DATE(t2.recordDate) AND t2.temperature < t1.temperature