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
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `location` (
  `id_location` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `country` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_location`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES (1,'Andrijevica','Montenegro'),(2,'Bar','Montenegro'),(3,'Berane','Montenegro'),(4,'Bijelo Polje','Montenegro'),(5,'Budva','Montenegro'),(6,'Cetinje','Montenegro'),(7,'Danilovgrad','Montenegro'),(8,'Kolašin','Montenegro'),(9,'Kotor','Montenegro'),(10,'Mojkovac','Montenegro'),(11,'Nikšić','Montenegro'),(12,'Plav','Montenegro'),(13,'Pljevlja','Montenegro'),(14,'Plužine','Montenegro'),(15,'Rožaje','Montenegro'),(16,'Šavnik','Montenegro'),(17,'Tivat','Montenegro'),(18,'Ulcinj','Montenegro'),(19,'Žabljak','Montenegro'),(20,'Budva Okolina','Montenegro'),(21,'Herceg Novi','Montenegro'),(22,'Podgorica','Montenegro'),(23,'Podgorica Okolina','Montenegro'),(24,'Beograd','Serbia'),(25,'Bor','Serbia'),(26,'Valjevo','Serbia'),(27,'Vranje','Serbia'),(28,'Vršac','Serbia'),(29,'Zaječar','Serbia'),(30,'Zrenjanin','Serbia'),(31,'Jagodina','Serbia'),(32,'Kikinda','Serbia'),(33,'Kragujevac','Serbia'),(34,'Kraljevo','Serbia'),(35,'Kruševac','Serbia'),(36,'Leskovac','Serbia'),(37,'Loznica','Serbia'),(38,'Niš','Serbia'),(39,'Novi Pazar','Serbia'),(40,'Novi Sad','Serbia'),(41,'Pančevo','Serbia'),(42,'Pirot','Serbia'),(43,'Požarevac','Serbia'),(44,'Priština','Serbia'),(45,'Prokuplje','Serbia'),(46,'Smederevo','Serbia'),(47,'Sombor','Serbia'),(48,'Sremska Mitrovica','Serbia'),(49,'Subotica','Serbia'),(50,'Užice','Serbia'),(51,'Čačak','Serbia'),(52,'Šabac','Serbia');
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
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
