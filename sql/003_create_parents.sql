CREATE TABLE `parents` (
  `idparents` int NOT NULL,
  `telephone` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `parent_name` varchar(45) NOT NULL,
  `parents_child` varchar(45) NOT NULL,
  PRIMARY KEY (`idparents`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
