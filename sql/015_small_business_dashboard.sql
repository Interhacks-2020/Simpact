CREATE TABLE `small_business_dashboard` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `total_redeemed` int NOT NULL,
  `extra purchases` int NOT NULL,
  `perk_increase` int NOT NULL,
  PRIMARY KEY (`id`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
