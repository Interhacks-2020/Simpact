CREATE TABLE `volunteers` (
  `volunteer_id` int NOT NULL,
  `volunteer_name` varchar(45) NOT NULL,
  `hours_worked` int NOT NULL,
  `ranking` int NOT NULL,
  `telephone` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `points` int NOT NULL,
  PRIMARY KEY (`volunteer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
