CREATE TABLE `non_profit_org` (
  `n_name` varchar(45) NOT NULL,
  `n_city` varchar(45) NOT NULL,
  `n_services_offered` varchar(45) NOT NULL,
  `n_telephone` varchar(45) NOT NULL,
  `number_of_volunteers` int NOT NULL,
  PRIMARY KEY (`n_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
