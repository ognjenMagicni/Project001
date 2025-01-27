-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: properties
-- ------------------------------------------------------
-- Server version	8.0.40-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `search`
--

DROP TABLE IF EXISTS `search`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `search` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(200) DEFAULT NULL,
  `description` text,
  `price_min` decimal(10,0) DEFAULT NULL,
  `price_max` decimal(10,0) DEFAULT NULL,
  `square_min` int DEFAULT NULL,
  `square_max` int DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `search`
--

LOCK TABLES `search` WRITE;
/*!40000 ALTER TABLE `search` DISABLE KEYS */;
INSERT INTO `search` VALUES (47,'Podgorica Full','Stanovi U podgorici',0,1100000,5,400,'2024-12-20'),(51,'Novi Sad Full','Stanovi u Novom Sadu',20000,5000000,10,500,'2024-12-22'),(56,'Beograd','Stanovi u Beogradu',20000,5000000,10,500,'2024-12-24'),(57,'Niksic','Svi stanovi u Niksicu',100000000,0,3000,0,'2024-12-27'),(68,'Nis','A lot of properties in Nis',20000,5000000,10,500,'2025-01-03'),(69,'Valjevo','Valjevo',20000,5000000,10,500,'2025-01-03'),(70,'Zabljak','Sve nekretnine na Zabljaku',100000000,0,3000,0,'2025-01-04'),(72,'Kragujevac','EEEEEEJ',20000,500000,10,500,'2025-01-04'),(106,'Danilovgrad Full','',30000,230000,50,6400,'2025-01-19'),(107,'Danilovgrad Full','',100000000,0,3000,0,'2025-01-19'),(108,'Danilovgrad Full','',100000000,0,3000,0,'2025-01-19'),(109,'Danilovgrad Full','',100000000,0,3000,0,'2025-01-19'),(110,'Krusevac','',20000,500000,10,500,'2025-01-24');
/*!40000 ALTER TABLE `search` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-26 20:49:01
