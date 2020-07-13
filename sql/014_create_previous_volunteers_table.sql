CREATE TABLE `previous_volunteers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `opportunity` varchar(45) NOT NULL,
  `location` varchar(45) NOT NULL,
  `time` datetime DEFAULT NULL,
  `points_earned` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
