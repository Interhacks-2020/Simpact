CREATE TABLE `perks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  `point_price` int NOT NULL,
  `starts` date NOT NULL,
  `ends` date NOT NULL,
  `combination with other offers` tinyint NOT NULL,
  `perk photo` varchar(100) NOT NULL,
  `status` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
