SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

CREATE DATABASE `todo` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `todo`;

DROP TABLE IF EXISTS `tasks`;
CREATE TABLE `tasks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `task` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `due_date` date NOT NULL,
  `category` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `done` tinyint(1) unsigned zerofill NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `tasks` (`id`, `task`, `due_date`, `category`, `done`) VALUES
(1,	'Install new door',	'2021-04-30',	'house',	0),
(2,	'Deliver amazing demo',	'2021-04-26',	'bootcamp',	0),
(3,	'Buy donuts for new team',	'2021-05-06',	'work',	0),
(4,	'Remove dinosaur from bathroom',	'2021-04-20',	'house',	0),
(5,	'Book holiday days off',	'2021-05-21',	'holidays',	0),
(6,	'Book train and hotel',	'2021-05-24',	'holidays',	0);