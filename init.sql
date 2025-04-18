CREATE DATABASE IF NOT EXISTS properties /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `properties`;


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


CREATE TABLE IF NOT EXISTS `search` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(200) DEFAULT NULL,
  `description` text,
  `price_min` decimal(10,0) DEFAULT NULL,
  `price_max` decimal(10,0) DEFAULT NULL,
  `square_min` int DEFAULT NULL,
  `square_max` int DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=112 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE IF NOT EXISTS `property` (
  `id_property` int NOT NULL AUTO_INCREMENT,
  `fk_search` int DEFAULT NULL,
  `no_room` int DEFAULT NULL,
  `square` int DEFAULT NULL,
  `price` decimal(15,2) DEFAULT NULL,
  `location` varchar(200) DEFAULT NULL,
  `city` varchar(200) DEFAULT NULL,
  `country` varchar(200) DEFAULT NULL,
  `link` varchar(200) DEFAULT NULL,
  `on_off` int DEFAULT NULL,
  `description` text,
  `square_price` int DEFAULT NULL,
  PRIMARY KEY (`id_property`),
  KEY `fk_search_idx` (`fk_search`),
  CONSTRAINT `fk_search` FOREIGN KEY (`fk_search`) REFERENCES `search` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58115 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `settlements4zid` (
  `id_settlements` int NOT NULL AUTO_INCREMENT,
  `fk_property` int NOT NULL,
  `settlement` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_settlements`),
  KEY `property_settlements4zid_idx` (`fk_property`),
  CONSTRAINT `property_settlements4zid` FOREIGN KEY (`fk_property`) REFERENCES `property` (`id_property`)
) ENGINE=InnoDB AUTO_INCREMENT=20314 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `type` (
  `id_type` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id_type`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type`
--

LOCK TABLES `type` WRITE;
/*!40000 ALTER TABLE `type` DISABLE KEYS */;
INSERT INTO `type` VALUES (1,'Home'),(2,'Apartment'),(3,'Land'),(4,'Commercial'),(5,'Hotel'),(6,'Residential_lot'),(7,'Agricultural_land'),(9,'Campground'),(10,'Garage');
/*!40000 ALTER TABLE `type` ENABLE KEYS */;
UNLOCK TABLES;

