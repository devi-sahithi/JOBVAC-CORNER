-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: jobvac_db
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `job`
--

DROP TABLE IF EXISTS `job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `job` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(45) NOT NULL,
  `company` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  `salary` decimal(10,0) NOT NULL,
  `created_at` date DEFAULT NULL,
  `location` varchar(45) NOT NULL,
  `qualification` varchar(45) NOT NULL,
  `recruiter_id` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `job`
--

LOCK TABLES `job` WRITE;
/*!40000 ALTER TABLE `job` DISABLE KEYS */;
INSERT INTO `job` VALUES (1,'helper','srinivasa medico','8 working hrs.should pass b-pharmacy',12000,'2023-07-06','Beside Axis Bank, shamshabad','10th',2),(2,'server','airport bawarchi','8 working hrs',8000,'2023-06-09','Beside Shamshabad Bus Depot, Opp.BataShowroom','SSC',1),(3,'security','kashish palace','12 hrs',9000,'2023-09-17','Near Airport, Satamrai Colony-Shamshabad','Degree',2),(5,'manager','SSSM','experienced good ',120000,'2023-08-13','hyd','Btech',1),(22,'Plumber','Sam','zomato',1200,'2023-08-13','US','-',69),(52,'private hostel','R group','all facilities\r\n',5000,'2023-08-13','shamshabad','-',5),(66,'Server/Cleaner','SSSM','8 working hours',12000,'2023-08-13','shamshabad','-',1),(69,'police','R group','cdccbjks',150,'2023-08-13','shamashabad','-',6),(88,'puncher','Sahithi','dfkb',500,'2023-08-13','knr','-',22),(89,'Driver','R group','needed driver',14000,'2023-08-13','warangal','-',4),(90,'Barber','SSSM','murari haircut',150,'2023-08-13','shamshabad','-',1),(99,'olive','SSSM','nothing',1233,'2023-08-13','hyd','Btech',1);
/*!40000 ALTER TABLE `job` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-14 11:14:03
