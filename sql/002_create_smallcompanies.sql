CREATE TABLE `companies` (
  `c_id` int NOT NULL,
  `c_name` varchar(45) NOT NULL,
  `services_offered` varchar(50) NOT NULL,
  `city` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `company_phone` varchar(45) NOT NULL,
  `number_of_volunteers` int NOT NULL,
  `perks` varchar(45) NOT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
