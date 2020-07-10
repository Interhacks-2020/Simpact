CREATE TABLE `business_posting` (
  `business_name` varchar(45) NOT NULL,
  `age_requirements` varchar(45) NOT NULL,
  `description` varchar(700) NOT NULL,
  `points_available` int NOT NULL,
  `logo` varchar(100) NOT NULL,
  PRIMARY KEY (`business_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
