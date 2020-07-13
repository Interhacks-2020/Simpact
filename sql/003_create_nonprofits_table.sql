CREATE TABLE `non_profits` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `city` varchar(45) NOT NULL,
  `zipcode` int NOT NULL,
  `points` int NOT NULL,
  `total_volunteers` int NOT NULL,
  `total_hours` int NOT NULL,
  `approved_hours` int NOT NULL,
  `pending_hours` int NOT NULL,
  `notifications` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
